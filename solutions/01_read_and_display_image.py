"""Q1: Read an image with OpenCV and display it."""

from cv_helpers import arguments, load_image, save_preview

args = arguments(__doc__)
image = load_image(args.image)
save_preview("Q1: Read and display an image", [("Image", image)], args.output_dir, "q01_original.png", args.display)
