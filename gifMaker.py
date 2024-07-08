import imageio.v2 as imageio
from PIL import Image
import json
import os
import math
import sys

if len(sys.argv) == 1:
    try:
        with open('config.json', 'r') as f:
            config = json.load(f)
    except:
        input("Please provide a config json file name like 'config.json'. running the program: python main.py config.json")
        exit()
else:
    with open(sys.argv[1], 'r') as f:
        config = json.load(f)

exportPath = config["exportPath"]
pathToPics = config["pathToPics"]
if not os.path.exists(pathToPics):
    input(f"Image folder {pathToPics} does not exist. Adjust the value in the config.json file")
    exit()
basePicName = config["basePicName"]
picExtension = config["picExtension"]
imageRanges = config["imageRangesString"].split(",") #pvz.: 2294-2295, 2278-2280, 2297-2298, 2326-2327
numberFill = config["numberFill"]

duration = config["gifSettings"]["duration"] * 1000
loop = config["gifSettings"]["loop"]
stutter = config["gifSettings"]["stutter"]
paletteSize = config["gifSettings"]["paletteSize"]
quantizer = config["gifSettings"]["quantizer"]
subrectangles = config["gifSettings"]["subrectangles"]

maxFileSize = config["gifSettings"]["maxFileSize"] * 1024 * 1024 #MB

if not os.path.exists(exportPath):
    os.makedirs(exportPath)
    print(f"Directory '{exportPath}' created.")

def resize_image(image_path, factor):
    img = Image.open(image_path)
    img = img.resize((int(img.width * factor), int(img.height * factor)), Image.Resampling.LANCZOS)
    return img

baseImages = []
for bounds in imageRanges:
    tmp = []
    bounds = bounds.strip().split("-")
    for n in range(int(bounds[0]), int(bounds[1]) + 1):
        tmp.append(os.path.join(pathToPics, f"{basePicName}{str(n).zfill(numberFill)}{picExtension}"))

    baseImages.append(tmp)

# print(baseImages)

for i in range(len(baseImages)):
    try:
        frames = [imageio.imread(image) for image in baseImages[i]]
    except Exception as e:
        print(e)
        input("Failed to read images. Check and adjust the config.json file")
        exit()
    for frame in frames:
        if frame.shape != frames[0].shape:
            input(f"Error: the images in the range {imageRanges[i]} are not the same resolution")
            exit()
    durationList = [duration] * len(baseImages[i])
    durationList[-1] += stutter * 1000
    gifPath = os.path.join(exportPath, f"{basePicName}{imageRanges[i]}.gif")
    imageio.mimsave(
        gifPath,
        frames,
        duration=durationList,
        loop=loop,
        palettesize=paletteSize,
        quantizer=quantizer,
        subrectangles=subrectangles
    )

    if maxFileSize > 0:
        while os.path.getsize(gifPath) > maxFileSize:
            fileSize = os.path.getsize(gifPath)
            resizeFactor = math.ceil(maxFileSize / fileSize * 10) / 10
            frames = [resize_image(image, resizeFactor) for image in baseImages[i]]
            imageio.mimsave(
                gifPath,
                frames,
                duration=durationList,
                loop=loop,
                palettesize=paletteSize,
                quantizer=quantizer,
                subrectangles=subrectangles
            )
