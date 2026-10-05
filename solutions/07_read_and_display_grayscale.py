"""Q7: Read an image directly in grayscale mode and display it."""

from cv_helpers import arguments, load_image, save_preview

args = arguments(__doc__)
grayscale = load_image(args.image, grayscale=True)
save_preview("Q7: Read directly as grayscale", [("Grayscale", grayscale)], args.output_dir, "q07_grayscale.png", args.display)
