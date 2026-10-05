"""Q20: Create a grayscale ramp whose values increase from 0 to 255."""

import numpy as np

from cv_helpers import arguments, save_preview

args = arguments(__doc__)
ramp = np.tile(np.arange(256, dtype=np.uint8), (100, 1))
save_preview("Q20: Grayscale intensity ramp (0–255)", [("Intensity ramp", ramp)], args.output_dir, "q20_ramp.png", args.display)
