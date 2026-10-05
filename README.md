# Computer Vision Day 1: 25 Python + OpenCV solutions

This project contains 25 separate, independently runnable Python scripts for
the Computer Vision Day 1 worksheet. The numbered filenames match the question
order. It uses Python, OpenCV, NumPy, and Matplotlib.

## Setup

```powershell
python -m pip install -r requirements.txt
```

## Run each question separately

```powershell
python solutions\01_read_and_display_image.py
python solutions\02_check_image_loaded.py
python solutions\03_print_image_dimensions.py
```

Continue with `04_count_image_pixels.py` through
`25_rotate_image_90_degrees.py` in the same `solutions\` folder. Each script
runs just its matching question. No image is needed to start: a generated demo
image is used by default. Previews and generated images are saved in `outputs/`.
Add `--display` to open Matplotlib preview windows.

To use your own image:

```powershell
python solutions\01_read_and_display_image.py --image "C:\path\to\image.jpg"
```

For example, run question 11 with a custom pixel coordinate:

```powershell
python solutions\11_read_pixel_at_coordinate.py --image "C:\path\to\image.jpg" --x 50 --y 40
```

The pixel coordinates use `(x, y)` order, while NumPy indexes image arrays as
`image[y, x]`. Questions 11 and 13 report the selected pixel; question 12 sets
it to red. Question 24 crops an ROI starting at `(x, y)`; `--roi-width` and
`--roi-height` configure its dimensions.

## Script names

Every question has its own descriptively named file: `01_read_and_display_image.py`,
`02_check_image_loaded.py`, `03_print_image_dimensions.py`,
`04_count_image_pixels.py`, `05_print_image_data_type.py`,
`06_save_image_as_new_file.py`, `07_read_and_display_grayscale.py`,
`08_convert_color_to_grayscale.py`, `09_display_image_with_matplotlib.py`,
`10_resize_image_to_half.py`, `11_read_pixel_at_coordinate.py`,
`12_change_pixel_and_save_image.py`, `13_print_bgr_pixel_values.py`,
`14_split_and_display_color_channels.py`, `15_merge_image_channels.py`,
`16_grayscale_minimum_and_maximum.py`, `17_calculate_grayscale_mean.py`,
`18_grayscale_mean_and_standard_deviation.py`,
`19_create_constant_grayscale_image.py`, `20_create_grayscale_intensity_ramp.py`,
`21_quantize_grayscale_to_4_bit.py`, `22_quantize_grayscale_to_2_bit.py`,
`23_downsample_image_by_two.py`, `24_crop_image_region_of_interest.py`, and
`25_rotate_image_90_degrees.py`. `cv_helpers.py` holds shared image loading and
preview helpers used by those scripts.

Quantized values are expanded to the full 0–255 display range while retaining
16 distinct levels (4-bit) or 4 distinct levels (2-bit).
