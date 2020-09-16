			from typing import List, Union
			
			from container_packing.dimension import Dimension
			from container_packing.largest_area_fit_first_packager import LargestAreaFitFirstPackager
			from container_packing.box import Box
			from container_packing.box_item import BoxItem
			
			
			def pack_products_into_restrictions(products: List[Union[tuple, dict]],
			restrictions: tuple) -> Union[tuple, None]:
			"""Pack product into container with given restrictions.
			
			:param products: list with tuples of width, depth and height of product
			or with dicts with with (key x), depth (y), height (z) and quantity,
			:param restrictions: tuple with width, depth and height of container,
			:return: tuple with minimal width, depth and height of container
			that can hold all products or None if there is no container with
			given restrictions."""
			
			container_x, container_y, container_z = restrictions
			containers = [Dimension.new_instance(container_x, container_y, container_z)]
			packager = LargestAreaFitFirstPackager(containers)
			
			box_items = []
			for product in products:
			if isinstance(product, tuple):
			x, y, z = product
			box_items.append(BoxItem(Box(x, y, z)))
			elif isinstance(product, dict):
			box_items.append(BoxItem(
			Box(product['x'], product['y'], product['z']),
			product.get('quantity', 1)
			))
			
			match = packager.pack(box_items)
			
			if not match:
			return None
			
			# calculating width, depth and height of gotten container
			max_width = max_depth = max_height = 0
			for levels_by_height in match.levels:
			for level in levels_by_height:
			max_width = max(level.space.x + level.box.width, max_width)
			max_depth = max(level.space.y + level.box.depth, max_depth)
			
			if levels_by_height is match.levels[-1]:
			max_height = max(level.space.z + level.box.height, max_height)
			
			return max_width, max_depth, max_height
			
from container_packing.shortcuts import pack_products_into_restrictions

boxes = [{
'x': 27,
'y': 27,
'z': 120,
'quantity': 3819
}, {
'x': 24,
'y': 24,
'z': 80,
'quantity': 5132
}, {
'x': 21,
'y': 21,
'z': 60,
'quantity': 4031
}]

conataner_max_sizes = (6060, 2160, 240)

container_x, container_y, container_z = pack_products_into_restrictions(
boxes,
conataner_max_sizes
)

print(container_x, container_y, container_z)