# GifMaker
A script to quickly create gifs from your images.
Using python's imageIO library.
### Prerequisites
Installed python3 with pip
https://www.python.org/downloads/

The image files need to be in the same folder and named like so:
`basePicName-XX.jpg`

Examples:
```
Flowers-52.JPG
NewYork_8112.png
BasketballU12 1.jpg
```
## Instructions
### Setup
Download .zip file and unzip the files with the green download button above
Open a terminal within the unziped folder. For example: `cd C:\Users\matas\Downloads\gifMaker`
Run: `pip install -r requirements.txt`
### Working with the script:
You need to 1. edit the **config.json** file, 2. run **gifMaker.py** with `python gifMaker.py` via a terminal that has the folder where the file is located. Example:
`C:\Users\matas\Programos\GifMaker> python gifMaker.py`
>Note: the config.json file and gifMaker.py need to be in the same folder.

### Editing config.json
*Full example config.json file provided below*
Open config.json with notepad or a code editor to change its contents.
#### config.json values:
"exportPath": "\<path where to store the resulting gifs>",
>A path from the root folder (drive) of your computer to the folder where you want the gifs to be stored.
>Or a string like `"result/"`, which will create the directory "result" in the same folder as the .exe is located.

"pathToPics": "\<path to the image folder>"
>A path from the root folder (drive) of your computer to the folder where the images are located

"basePicName": "\<image collection name + delimiter >"
>Start of the file names without its number. Like: `"Summer2024_"`

"picExtension": "\<file extensions>",
>`".jpg" / ".png", ...`

"imageRangesString": "\<one or more image number ranges (start and end included)>",
>Format: image numbers separated by `-`. And for multiple ranges (and in turn resulting gifs), they need to be separated by a comma (`,`)
>All the images in a single specified range need to have the same resolution or an error will be thrown.
>Note: A range's start and end numbers (images) are included

"numberFill": \<length of the numbers in the file names>
>If the numbers in the range are `"83-85"` but the files names are ...0083.jpg and ...0085.jpg, the value would be `4`
>The code fills in `0`'s before the the range numbers so that the length of the number is equal this attribute's value
>Note: if you specified a range like `"0083-0085"`, you still need to specify the number length, which in this case would be `4`

"duration": \<duration of a single frame in the gif (in seconds)>,
> `0.1` - 100ms for a single image in the gif 

"loop": \<amount of times the gif plays back>,

> `0` - infinite 

"stutter": \<extends the final frame's duration by n seconds>,
> `0` - for no incrase in duration to the final frame

"paletteSize": \<color amount (2-256)>,
>`256` - maximum amount of different colors in the gif

"quantizer": "\<the method used to reduce the number of colors in the image>",
>**Possible values:**
>NeuQuant (`"nq"`):
Generally provides high-quality color reduction by effectively distributing colors across the palette. NeuQuant is good at preserving image quality, especially for images with gradients and smooth color transitions, but it can be slower than other methods.
\
Wu quantizer (`"wu"`):
Tends to produce good results for images with distinct regions of color. It is faster than NeuQuant and often provides a good balance between quality and performance, making it a common choice for many applications.
\
Octree (`"octree"`):
Efficient and fast, suitable for real-time applications. It works well with images that have a large number of colors and can quickly produce a color palette. However, it might not always produce as high quality as NeuQuant or Wu for certain images.
\
Median cut (`"mediancut"`):
Simple and fast, making it a good choice for quickly reducing colors. However, it might not handle images with complex color variations as well as NeuQuant or Wu.

"subrectangles": \<whether to save each frame as a subrectangle>,
> Value: `true` / `false`
When `true`, the GIF file size can be reduced by only saving the changed areas of each frame. This can be particularly effective for animations with minimal changes between frames. When `false`, each frame is stored in full, which might be simpler but less efficient in terms of file size.

"maxFileSize": \<maximum file size of the gif (in MB)>
>`0` - no maximum size

### Example config.json

```
{
"exportPath": "export/",

"pathToPics": "C:/Users/matas/Downloads/Jake20Bday",

"basePicName": "Jake20-",

"picExtension": ".jpg",

"imageRangesString": "2294-2295, 2278-2280, 2297-2298, 2326-2327",

"numberFill": 4,

"gifSettings": {

	"duration": 0.25,

	"loop": 0,

	"stutter": 0.15,

	"paletteSize": 256,

	"quantizer": "nq",

	"subrectangles": true,

	"maxFileSize": 3

	}

}
```