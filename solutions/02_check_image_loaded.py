"""Q2: Check that an image was loaded and report a useful error on failure."""

from cv_helpers import arguments, load_image

args = arguments(__doc__)
image = load_image(args.image)
print(f"Image loaded successfully: {image is not None}")
print(f"Image dimensions: {image.shape[1]}x{image.shape[0]}")
