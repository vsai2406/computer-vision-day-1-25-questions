"""Q6: Read an image and save it with a different filename."""

from cv_helpers import arguments, load_image, save_image

args = arguments(__doc__)
image = load_image(args.image)
save_image(image, args.output_dir / "q06_copy.jpg")
