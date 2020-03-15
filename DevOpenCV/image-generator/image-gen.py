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

#Determining Image sizing based on number of pictures
path, dirs, files = next(os.walk(image_dir))
file_len = len(files)
print(file_len)


# Tier Information
num_tiers = 7;
tier_cat = ['S', 'A', 'B', 'C', 'D', 'E', 'F']
gray = (26,26,26)
tier_colors=[(255,127,127), (255,191,127), (255,255,127), (127,255,127),(127,191,255),(127,127,255), (255,127,255) ]


# Initial Image distance information
image_height, image_width = (1080, 1920)
v_padding = 10
h_padding = 10
ending_y_size = 152
fontsize = 30
box_size = ending_y_size - h_padding

font = ImageFont.truetype("./font/Arial.ttf", fontsize)

# Dictionary of user ratings on tier lists
danny_rate = {
	'S': [18, 27],
	'A': [3, 8, 10, 23, 25, 26, 29],
	'B': [5, 9, 17, 20, 31, 32],
	'C': [1, 2, 6, 14, 21, 22, 28, 30],
	'D': [7, 12, 15, 19, 24],
	'E': [4,13, 16],
	'F': [11]
}

longest_tier = len(danny_rate[max(danny_rate, key=lambda x:len(danny_rate[x]))])
print(longest_tier);

estimated_width = (h_padding + ending_y_size) * longest_tier + h_padding;

if  estimated_width > image_width : 
	image_width = estimated_width

tier_list = Image.new('RGBA', (image_width, image_height), 'black') 
idraw = ImageDraw.Draw(tier_list)

# Draw the base list
for x in range(num_tiers):
	idraw.rectangle((h_padding, v_padding + ending_y_size*(x)  , ending_y_size, ending_y_size*(x+1)), fill=tier_colors[x])
	idraw.rectangle((h_padding + ending_y_size, v_padding +ending_y_size*(x), image_width, ending_y_size*(x+1)), fill=gray)
	w, h = idraw.textsize(tier_cat[x])
	idraw.text(((ending_y_size - w)/2 ,ending_y_size*(x) + (ending_y_size - h)/2), tier_cat[x], font=font, fill='black')

# Add in images based on dictionary WIP
thumb_size = box_size, box_size
tier_height = 0
for tier in danny_rate:
	total_width_used = ending_y_size;
	images = danny_rate[tier]
	for image in images:
		im_name = str(image) + ".PNG"
		print(im_name)
		new_path = os.path.join(image_dir, im_name)
		im = Image.open(new_path)
		im.thumbnail(thumb_size, Image.ANTIALIAS)
		t_w, t_h = im.size
		total_width_used += h_padding;
		tier_list.paste(im, (total_width_used, tier_height + v_padding , total_width_used + t_w, tier_height + t_h + v_padding))
		
		#idraw.rectangle((total_width_used, tier_height + v_padding , total_width_used + t_w, tier_height + t_h + v_padding), fill="blue")
		total_width_used += t_w
	tier_height += ending_y_size;

tier_list.save('dannys_tierlist.png')



