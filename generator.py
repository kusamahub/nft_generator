# KusamaHub
# 2022

# NFT Generator
# This script helps random generate NFTs from provided data and different variations of equpables.
# Output of script is folder OUTPUT/NFT_NAME.PNG
# For script workin you need to create right structure in you collection folder.


# Folder structure:

# Collection folder       - This is your collection folder
#   ⌙ Background          - This folder must contains backgrounds
#   ⌙ Wear                - This folder contains body wear
#   ⌙ Eyes                - This folder contains eyes
#   ⌙ Glasses             - This folder contains glasses
#   ⌙ Hair                - This folder contains hairs, caps, hats and etc.
#   ⌙ Horn                - This folder contains horns
#   ⌙ Main                - This folder contains main body
#   ⌙ Mouth               - This folder contains mouth
#   ⌙ Wings               - This folder contains wings


# Libraries
import os
import glob
import random
import argparse
from PIL import Image
from time import process_time
from datetime import datetime as dt
from colorama import Fore
from colorama import Style

# Scripts arguments and info
parser = argparse.ArgumentParser(
    prog = 'KusamaHub NFT Generator',
    description = 'This script gets all parts of nft and randomize them to one file. You can set how many randoms you want to get in output.',
    epilog = 'GitHub: https://github.com/kusamahub/nft_generator')
 
parser.add_argument("-f", "--folder", help = "Set your collection folder name")
parser.add_argument("-a", "--amount", type=int, help = "Set amount of nfts, which will be generated")
parser.add_argument("-x", "--height", type=int, help = "Set image height size")
parser.add_argument("-y", "--width", type=int, help = "Set image width size")

args = parser.parse_args()

# Collection folder path
COLLECTION_FOLDER   = args.folder

# Amount of images to generate
NFTS_AMOUNT = args.amount

# Generated image size
IMAGE_HEIGHT = args.height
IMAGE_WIDTH = args.width

# Folders with items (you can change Folders after '+' if you have another structure.)
HORN_FOLDER         = COLLECTION_FOLDER + '/Horn/'
GLASSES_FOLDER      = COLLECTION_FOLDER + '/Glasses/'
HAIR_FOLDER         = COLLECTION_FOLDER + '/Hair/'
EYES_FOLDER         = COLLECTION_FOLDER + '/Eyes/'
WEAR_FOLDER         = COLLECTION_FOLDER + '/Wear/'
MOUTH_FOLDER        = COLLECTION_FOLDER + '/Mouth/'
BODY_FOLDER         = COLLECTION_FOLDER + '/Body/'
WINGS_FOLDER        = COLLECTION_FOLDER + '/Wings/'
BACKGROUND_FOLDER   = COLLECTION_FOLDER + '/Background/'

# Console message
print(f"{Style.BRIGHT}{Fore.MAGENTA}* KusamaHub NFT Generator:>>  {Fore.GREEN}Start generation process...")

# Start count elapsed time 
runtime_start = dt.now()

# Items data
parts = [HORN_FOLDER, GLASSES_FOLDER, HAIR_FOLDER, EYES_FOLDER, WEAR_FOLDER, MOUTH_FOLDER, BODY_FOLDER, WINGS_FOLDER, BACKGROUND_FOLDER]

files = {
    part: [file for file in os.listdir(part) if file.endswith('.png')]
    for part in parts
}

# Main generator function
def generator():

        # Generated image name
        name = 0

        # Count generated image name +1
        while name <= NFTS_AMOUNT -1:
            name = name + 1

            # Create image with input size
            new_im = Image.new(mode="RGBA", size=(IMAGE_HEIGHT, IMAGE_WIDTH))

            # Get random items and resize them to one size
            background  = Image.open(BACKGROUND_FOLDER + random.choice(files[BACKGROUND_FOLDER])).resize(new_im.size).convert('RGBA')
            wings       = Image.open(WINGS_FOLDER + random.choice(files[WINGS_FOLDER])).resize(new_im.size).convert('RGBA')
            wear        = Image.open(WEAR_FOLDER + random.choice(files[WEAR_FOLDER])).resize(new_im.size).convert('RGBA')
            eyes        = Image.open(EYES_FOLDER + random.choice(files[EYES_FOLDER])).resize(new_im.size).convert('RGBA')
            glasses     = Image.open(GLASSES_FOLDER + random.choice(files[GLASSES_FOLDER])).resize(new_im.size).convert('RGBA')
            hair        = Image.open(HAIR_FOLDER + random.choice(files[HAIR_FOLDER])).resize(new_im.size).convert('RGBA')
            horn        = Image.open(HORN_FOLDER + random.choice(files[HORN_FOLDER])).resize(new_im.size).convert('RGBA')
            body        = Image.open(BODY_FOLDER + random.choice(files[BODY_FOLDER])).resize(new_im.size).convert('RGBA')
            mouth       = Image.open(MOUTH_FOLDER + random.choice(files[MOUTH_FOLDER])).resize(new_im.size).convert('RGBA')
            
            # Merge layers.
            # Layers order from first (bottom) to last (top). So 'background' - last layer, mouth - top layer.
            new_im.alpha_composite(background)
            new_im.alpha_composite(wings)
            new_im.alpha_composite(body)
            new_im.alpha_composite(wear)
            new_im.alpha_composite(eyes)
            new_im.alpha_composite(glasses)
            new_im.alpha_composite(hair)
            new_im.alpha_composite(horn)
            new_im.alpha_composite(mouth)

            # Define save location
            SAVE_LOCATION = "output/" + str(name) + ".png"

            # Save generated image
            new_im.save(SAVE_LOCATION, "PNG")
            # Console message
            print(f"{Style.BRIGHT}{Fore.MAGENTA}* KusamaHub NFT Generator:>>  {Fore.GREEN}Image created at this location: {Fore.RED}" + SAVE_LOCATION)

# Function loop
for i in range (NFTS_AMOUNT):
    generator()
    break

# Stop count elapsed time
runtime_end = dt.now()
runtime_elapsed = runtime_end - runtime_start

# Console message
print(f"{Style.BRIGHT}{Fore.MAGENTA}* KusamaHub NFT Generator:>>  {Fore.GREEN}Generation elapsed time: {Fore.CYAN}%02d:%02d:%02d:%02d" % (runtime_elapsed.days, runtime_elapsed.seconds // 3600, runtime_elapsed.seconds // 60 % 60, runtime_elapsed.seconds % 60)) 
print(f"{Style.BRIGHT}{Fore.MAGENTA}* KusamaHub NFT Generator:>>  {Fore.GREEN}Generation complete!")



