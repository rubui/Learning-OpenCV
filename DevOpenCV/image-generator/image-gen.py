# image-gen - generate a png containing the final result that comes from _______

import os
from PIL import Image, ImageDraw,ImageFont
from pathlib import Path

# Path walk
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
path = Path(BASE_DIR) 
print(path.parent)
image_dir = os.path.join(path.parent, "img\\look-alike")
print(image_dir)

path, dirs, files = next(os.walk(image_dir))
file_len = len(files)
print(file_len)


# Tier Information
num_tiers = 7;
tier_cat = ['S', 'A', 'B', 'C', 'D', 'E', 'F']
gray = (26,26,26)
tier_colors=[(255,127,127), (255,191,127), (255,255,127), (127,255,127),(127,191,255),(127,127,255), (255,127,255) ]


# Image distance information
image_height, image_width = (1080, 1920)
v_padding = 10
h_radding = 10
boxIsize = 152
fontsize = 30

font = ImageFont.truetype("./font/Arial.ttf", fontsize)

# Dictionary of user ratings on tier lists
danny_rate = {
	'S': [18, 27],
	'A': [3, 8, 10, 23, 25, 26, 29],
	'B': [5, 9, 17, 20, 31, 32],
	'C': [1, 2, 6, 14, 21, 22, 28, 30],
	'D': [7, 12, 15, 19, 24],
	'E': [4,13, 16]
}

tier_list = Image.new('RGBA', (image_width, image_height), 'black') 
idraw = ImageDraw.Draw(tier_list)

# Draw the base list
for x in range(num_tiers):
	idraw.rectangle((v_padding, v_padding +boxIsize*(x)  , boxIsize, boxIsize*(x+1)), fill=tier_colors[x])
	idraw.rectangle((v_padding + boxIsize, v_padding +boxIsize*(x), image_width, boxIsize*(x+1)), fill=gray)
	w, h = idraw.textsize(tier_cat[x])
	idraw.text(((boxIsize - w)/2 ,boxIsize*(x) + (boxIsize - h)/2), tier_cat[x], font=font, fill='black')

# Add in images based on dictionary WIP
# for root, dirs, files in os.walk(image_dir):
# 	for file in files:
# 		if file.endswith("png") or file.endswith("jpg"):
# 			path = os.path.join(root, file)
# 			label = os.path.basename(os.path.dirname(path)).replace(" ","-").lower()
# 			print(label, path)
# 			if label in label_ids:
# 				pass
# 			else:
# 				label_ids[label] = current_id
# 				current_id += 1
# 			id_ = label_ids[label]
# 			# y_labels.append(label)
# 			# x_train.append(path)
# 			pil_image = Image.open(path).convert("L")
# 			size = (550, 550)
# 			final_image = pil_image.resize(size, Image.ANTIALIAS)

tier_list.save('tierlist.png')



