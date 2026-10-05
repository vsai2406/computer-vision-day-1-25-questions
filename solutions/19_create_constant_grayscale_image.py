"""Q19: Create a 256x256 grayscale image with every pixel set to 128."""

import numpy as np

from cv_helpers import arguments, save_preview

args = arguments(__doc__)
image = np.full((256, 256), 128, dtype=np.uint8)
save_preview("Q19: Constant grayscale value 128", [("Intensity 128", image)], args.output_dir, "q19_constant.png", args.display)
