"""Q24: Crop a rectangular ROI using its top-left coordinate and dimensions."""

from cv_helpers import arguments, load_image, save_preview

args = arguments(__doc__)
if args.roi_width <= 0 or args.roi_height <= 0:
    raise ValueError("--roi-width and --roi-height must be positive.")
image = load_image(args.image)
height, width = image.shape[:2]
x = min(max(args.x, 0), width - 1)
y = min(max(args.y, 0), height - 1)
right = min(x + args.roi_width, width)
bottom = min(y + args.roi_height, height)
roi = image[y:bottom, x:right]
print(f"ROI: x={x}, y={y}, width={right - x}, height={bottom - y}")
save_preview("Q24: Cropped region of interest", [("ROI", roi)], args.output_dir, "q24_roi.png", args.display)
