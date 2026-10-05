"""Q4: Calculate and print the total number of image pixels."""

from cv_helpers import arguments, load_image

args = arguments(__doc__)
image = load_image(args.image)
height, width = image.shape[:2]
print(f"Total pixels: {height * width:,}")
