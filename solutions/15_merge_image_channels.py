"""Q15: Merge three separate grayscale image channels into a color image."""

import cv2

from cv_helpers import arguments, load_image, save_preview

args = arguments(__doc__)
image = load_image(args.image)
blue, green, red = cv2.split(image)
merged = cv2.merge((blue, green, red))
save_preview("Q15: Merge three channels", [("Merged color image", merged)], args.output_dir, "q15_merged.png", args.display)
