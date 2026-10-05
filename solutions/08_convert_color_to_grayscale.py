"""Q8: Convert a color image to grayscale using cv2.cvtColor."""

import cv2

from cv_helpers import arguments, load_image, save_preview

args = arguments(__doc__)
image = load_image(args.image)
grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
save_preview("Q8: Convert to grayscale", [("Grayscale", grayscale)], args.output_dir, "q08_grayscale.png", args.display)
