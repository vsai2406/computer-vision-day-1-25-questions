"""Q18: Calculate grayscale mean and standard deviation with NumPy."""

import cv2

from cv_helpers import arguments, load_image

args = arguments(__doc__)
image = load_image(args.image, grayscale=True)
print(f"Mean intensity: {float(image.mean()):.2f}")
print(f"Standard deviation: {float(image.std()):.2f}")
