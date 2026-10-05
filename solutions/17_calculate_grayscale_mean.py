"""Q17: Calculate and print the mean grayscale intensity."""

import cv2

from cv_helpers import arguments, load_image

args = arguments(__doc__)
image = load_image(args.image, grayscale=True)
print(f"Mean grayscale intensity: {float(image.mean()):.2f}")
