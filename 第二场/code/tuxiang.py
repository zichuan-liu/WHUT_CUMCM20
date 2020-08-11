import torch
import torch.nn as nn
from PIL import Image
import matplotlib.pyplot as plt
import math
import numpy as np

def read_single_to_tensor(image_path, device):
    """
    read single image and convert to tensor
    Args:
        image_path: image'path with name
    Returns:
        image tensor on gpu with shape (1, 3, w, h)
    """
    # 1: read and convert to tensor on gpu
    image = Image.open(image_path).convert('RGB')
    image = torch.from_numpy(np.array(image)).to(device)
    image = image
    # image = image.expand(image.shape[0],image.shape[1],3)
    # 2:transpose from (w, h, 3) into (3, w, h)
    image = image.permute(2, 1, 0)

    # 3:add dim from (3, w, h) into (1, 3, w, h)
    image = image.unsqueeze(0).float()
    image = image/255
    print(image.shape)
    return image


class AE(nn.Module):
    """ Auto Encoder """
    def __init__(self, in_channels, out_channels, encode_dim):
        super().__init__()
        self.in_channels = in_channels
        self.out_channels = out_channels
        self.curr_dim = encode_dim
        self.en_net = nn.Sequential(*self.build_encoder())
        self.de_net = nn.Sequential(*self.build_decoder())

    def build_encoder(self):
        encoder = []
        encoder.append(nn.Conv2d(in_channels=self.in_channels, out_channels=self.curr_dim,
                                 kernel_size=3, stride=1, padding=1))
        for i in range(2):
            encoder.append(nn.Conv2d(in_channels=self.curr_dim, out_channels=self.curr_dim*2,
                                     stride=2, padding=1, kernel_size=3))
            encoder.append(nn.ReLU())
            self.curr_dim = self.curr_dim * 2
        return encoder

    def build_decoder(self):
        decoder = []
        for i in range(2):
            decoder.append(nn.ConvTranspose2d(in_channels=self.curr_dim, out_channels=int(self.curr_dim/2),
                                              kernel_size=4, stride=2, padding=1))
            decoder.append(nn.ReLU())
            self.curr_dim = int(self.curr_dim/2)
        decoder.append(nn.Conv2d(in_channels=self.curr_dim, out_channels=self.out_channels,
                                 kernel_size=3, padding=1, stride=1))
        decoder.append(nn.Sigmoid())
        return decoder

    def forward(self, x):
        x = self.en_net(x)
        out = self.de_net(x)
        return out, x

# 1: options
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
total_iterations = 200
image_save_frequency = int(total_iterations/16)

# 2:data prepare
image_tensor = read_single_to_tensor(r"C:\Users\77526\Desktop\lzc\资料\DEMO\data\result10.png", device=device)
# i_w, i_h = image_tensor.shape[2], image_tensor.shape[3]
result_images = []
result_iterations = []
record_loss = []
record_iterations = []

# 3:network define
ae_net = AE(in_channels=3, out_channels=3, encode_dim=8).to(device)
print(ae_net)
# 4:optimizer define
optimizer = torch.optim.Adam(ae_net.parameters(), lr=0.01, betas=(0.9, 0.999))

# 5:loss define
mse_loss = nn.MSELoss()

# 6: plot function
def plot_list_image(image_list, title_list):
    """
    plot a list of image with title
    Args:
        image_list: a list of image with numpy type
        title_list: a list of title with str type

    Returns:
        True after plot
    """
    plt.figure(figsize=(4, 4))
    w_h = int(math.sqrt(len(image_list)))
    for i in range(w_h*w_h):
        plt.subplot(w_h, w_h, i+1)
        plt.axis("off")
        plt.imshow(image_list[i])
        plt.title(title_list[i])
    plt.show()
    return True


if __name__ == "__main__":
    for iteration in range(total_iterations):
        recon_image, encode = ae_net(image_tensor)
        loss = mse_loss(recon_image, image_tensor)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        print("iter: {}, loss: {}".format(iteration, loss.item()))
        record_loss.append(loss.item())
        record_iterations.append(iteration)
        recon_image = recon_image.squeeze(1)
        # print(recon_image.shape)
        if iteration % image_save_frequency == 0:
            result_images.append(recon_image.detach().cpu().numpy().squeeze().transpose(2,1, 0))
            result_iterations.append(str(iteration))
    plot_list_image(result_images, result_iterations)
    plt.plot(record_iterations, record_loss)
    plt.xlabel("iterations")
    plt.ylabel("loss value")
    plt.title("Loss Curve")
    plt.show()