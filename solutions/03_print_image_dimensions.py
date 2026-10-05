"""Q3: Print an image's height, width, and number of channels."""

from cv_helpers import arguments, load_image

args = arguments(__doc__)
image = load_image(args.image)
channels = 1 if image.ndim == 2 else image.shape[2]
print(f"Height: {image.shape[0]}")
print(f"Width: {image.shape[1]}")
print(f"Channels: {channels}")
