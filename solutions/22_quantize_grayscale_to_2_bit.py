"""Q22: Quantize an 8-bit grayscale image to 2-bit (4-level) intensity."""

import cv2

from cv_helpers import arguments, load_image, save_preview

args = arguments(__doc__)
grayscale = load_image(args.image, grayscale=True)
quantized = (grayscale // 64) * 85
save_preview("Q22: 2-bit grayscale (4 levels)", [("Quantized", quantized)], args.output_dir, "q22_2bit.png", args.display)
