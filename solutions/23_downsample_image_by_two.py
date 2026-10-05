"""Q23: Downsample an image by two in width and height and print both sizes."""

import cv2

from cv_helpers import arguments, load_image, save_preview

args = arguments(__doc__)
image = load_image(args.image)
downsampled = cv2.resize(image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
print(f"Original resolution: {image.shape[1]}x{image.shape[0]}")
print(f"New resolution: {downsampled.shape[1]}x{downsampled.shape[0]}")
save_preview("Q23: Downsample by a factor of two", [("Downsampled", downsampled)], args.output_dir, "q23_downsampled.png", args.display)
