"""Q5: Print the NumPy data type of the image matrix."""

from cv_helpers import arguments, load_image

args = arguments(__doc__)
image = load_image(args.image)
print(f"Image matrix dtype: {image.dtype}")
