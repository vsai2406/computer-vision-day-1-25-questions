"""Q13: Print the B, G, and R values at a selected pixel."""

from cv_helpers import arguments, load_image, selected_coordinate

args = arguments(__doc__)
image = load_image(args.image)
x, y = selected_coordinate(args.x, args.y, image)
blue, green, red = image[y, x]
print(f"Pixel at (x={x}, y={y}): B={blue}, G={green}, R={red}")
