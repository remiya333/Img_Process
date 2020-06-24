import sys
import os
from PIL import Image

'''
This Code Converts the images in JPG to PNG format. It takes the input and output path from the commandline as commandline args.
@input folder = args[1]
@output folder = args[2]
'''
#get the input folder and output folder from commandline
input_folder = sys.argv[1]
output_folder = sys.argv[2]

#check if output folder exists if not create the folder
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

#loop through the input file and save the converted file to output folder
for filename in os.listdir(input_folder):

    img = Image.open(input_folder+filename)
    cleanname = os.path.splitext(filename)[0]
    img.save(output_folder+cleanname+'.png','png')
    print('all done')

#img = Image.open(f'{input_folder}{filename}')