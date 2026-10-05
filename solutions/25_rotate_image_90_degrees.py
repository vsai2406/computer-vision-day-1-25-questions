"""Q25: Rotate an image 90 degrees clockwise, display it, and save it."""

import cv2

from cv_helpers import arguments, load_image, save_image, save_preview

args = arguments(__doc__)
image = load_image(args.image)
rotated = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
save_image(rotated, args.output_dir / "q25_rotated.png")
save_preview("Q25: Rotate image 90 degrees clockwise", [("Rotated image", rotated)], args.output_dir, "q25_preview.png", args.display)
