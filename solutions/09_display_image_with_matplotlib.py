"""Q9: Display an image with Matplotlib and hide the axes."""

from cv_helpers import arguments, load_image, save_preview

args = arguments(__doc__)
image = load_image(args.image)
save_preview("Q9: Matplotlib display without axes", [("Image", image)], args.output_dir, "q09_matplotlib.png", args.display)
