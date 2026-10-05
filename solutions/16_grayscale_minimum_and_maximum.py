"""Q16: Calculate and print the minimum and maximum grayscale intensities."""

import cv2

from cv_helpers import arguments, load_image

args = arguments(__doc__)
image = load_image(args.image, grayscale=True)
print(f"Minimum intensity: {int(image.min())}")
print(f"Maximum intensity: {int(image.max())}")
