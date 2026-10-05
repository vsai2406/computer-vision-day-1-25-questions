"""Q14: Split a color image into B, G, and R channels and display them."""

import cv2

from cv_helpers import arguments, load_image, save_preview

args = arguments(__doc__)
image = load_image(args.image)
blue, green, red = cv2.split(image)
channels = [("Blue channel", blue), ("Green channel", green), ("Red channel", red)]
save_preview("Q14: Split BGR channels", channels, args.output_dir, "q14_channels.png", args.display)
