"""Q21: Quantize an 8-bit grayscale image to 4-bit (16-level) intensity."""

import cv2

from cv_helpers import arguments, load_image, save_preview

args = arguments(__doc__)
grayscale = load_image(args.image, grayscale=True)
quantized = (grayscale // 16) * 17
save_preview("Q21: 4-bit grayscale (16 levels)", [("Quantized", quantized)], args.output_dir, "q21_4bit.png", args.display)
