imdata=imread('01.tif');
imshow(imdata);
flag=0;
Min=min(min(imdata));
Max=max(max(imdata));
h=medfilt2(imdata);%È¥Ôë
for i=1:size(imdata,1)
    for j=1:size(imdata,2)
        if (h(i,j)>200)
            h(i,j)=255;
        end
    end
end
h1=histeq(h);%ÔöÇ¿
subplot(221);imshow(imdata);
subplot(222);imshow(h);
subplot(223);imshow(h1);





for i=1:size(imdata,1)
    for j=1:size(imdata,2)
        if (imdata(i,j)<255)
            fringe_x1=i;
             flag=1;
            break;
        end
    end
    if(flag==1)
        flag=0;
        break;
    end
end
for i=size(imdata,1):-1:1
    for j=1:size(imdata,2)
        if (imdata(i,j)<255)
            fringe_x2=i;
               flag=1;
            break;
        end
    end
    if(flag==1)
        flag=0;
        break;
    end
end
for i=1:size(imdata,2)
    for j=1:size(imdata,1)
        if (imdata(j,i)<255)
            fringe_y1=i;
                 flag=1;
            break;
        end
    end
    if(flag==1)
        flag=0;
        break;
    end
end
for i=size(imdata,2):-1:1
    for j=1:size(imdata,1)
        if (imdata(j,i)<255)
            fringe_y2=i;
            flag=1;
            break;
        end
    end
    if(flag==1)
        flag=0;
        break;
    end
end
% image=imdata(  fringe_x1:   fringe_x2 ,fringe_y1:  fringe_y2);
% subplot(224); imshow(image);