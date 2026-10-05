"""Small shared helpers used by the independently runnable exercise scripts."""

from __future__ import annotations

import argparse
from pathlib import Path

import cv2
import matplotlib.pyplot as plt
import numpy as np


def arguments(description: str) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("--image", help="Input image path; defaults to a generated sample.")
    parser.add_argument("--output-dir", type=Path, default=Path("outputs"))
    parser.add_argument("--display", action="store_true", help="Open a preview window.")
    parser.add_argument("--x", type=int, default=10, help="Pixel/ROI x coordinate.")
    parser.add_argument("--y", type=int, default=10, help="Pixel/ROI y coordinate.")
    parser.add_argument("--roi-width", type=int, default=100)
    parser.add_argument("--roi-height", type=int, default=80)
    return parser.parse_args()


def sample_image() -> np.ndarray:
    height, width = 240, 320
    blue = np.tile(np.linspace(0, 255, width, dtype=np.uint8), (height, 1))
    green = np.tile(np.linspace(0, 255, height, dtype=np.uint8)[:, None], (1, width))
    red = np.full((height, width), 96, dtype=np.uint8)
    return cv2.merge((blue, green, red))


def load_image(path: str | None, grayscale: bool = False) -> np.ndarray:
    if path is None:
        image = sample_image()
        if grayscale:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        print("Using the generated 320x240 sample image.")
        return image

    mode = cv2.IMREAD_GRAYSCALE if grayscale else cv2.IMREAD_COLOR
    image = cv2.imread(path, mode)
    if image is None:
        raise FileNotFoundError(f"Could not load '{path}'. Check the path and image format.")
    return image


def save_preview(
    title: str,
    images: list[tuple[str, np.ndarray]],
    output_dir: Path,
    filename: str,
    display: bool,
) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    figure, axes = plt.subplots(1, len(images), figsize=(5 * len(images), 4))
    for axis, (label, image) in zip(np.atleast_1d(axes), images):
        if image.ndim == 2:
            axis.imshow(image, cmap="gray", vmin=0, vmax=255)
        else:
            axis.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        axis.set_title(label)
        axis.axis("off")
    figure.suptitle(title)
    figure.tight_layout()
    destination = output_dir / filename
    figure.savefig(destination, bbox_inches="tight")
    if display:
        plt.show()
    plt.close(figure)
    print(f"Preview saved to: {destination}")


def save_image(image: np.ndarray, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    if not cv2.imwrite(str(destination), image):
        raise OSError(f"Could not save image to '{destination}'.")
    print(f"Image saved to: {destination}")


def selected_coordinate(x: int, y: int, image: np.ndarray) -> tuple[int, int]:
    height, width = image.shape[:2]
    return min(max(x, 0), width - 1), min(max(y, 0), height - 1)
