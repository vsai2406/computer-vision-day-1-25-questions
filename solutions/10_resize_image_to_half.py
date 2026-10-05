"""Q10: Resize an image to 50 percent of its original width and height."""

import cv2

from cv_helpers import arguments, load_image, save_preview

args = arguments(__doc__)
image = load_image(args.image)
resized = cv2.resize(image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
print(f"Original: {image.shape[1]}x{image.shape[0]}")
print(f"Resized: {resized.shape[1]}x{resized.shape[0]}")
save_preview("Q10: Image resized to 50%", [("Resized", resized)], args.output_dir, "q10_resized.png", args.display)
