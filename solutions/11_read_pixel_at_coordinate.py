"""Q11: Read and print the pixel at a user-provided (x, y) coordinate."""

from cv_helpers import arguments, load_image, selected_coordinate

args = arguments(__doc__)
image = load_image(args.image)
x, y = selected_coordinate(args.x, args.y, image)
print(f"Pixel at (x={x}, y={y}) [B, G, R]: {image[y, x].tolist()}")
