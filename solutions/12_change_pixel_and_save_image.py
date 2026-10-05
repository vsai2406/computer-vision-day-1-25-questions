"""Q12: Change the selected pixel to red and save the modified image."""

from cv_helpers import arguments, load_image, save_image, save_preview, selected_coordinate

args = arguments(__doc__)
image = load_image(args.image)
x, y = selected_coordinate(args.x, args.y, image)
modified = image.copy()
modified[y, x] = (0, 0, 255)
save_image(modified, args.output_dir / "q12_modified_pixel.png")
save_preview("Q12: Modified pixel", [("Modified image", modified)], args.output_dir, "q12_preview.png", args.display)
