import numpy as np

def window_image(image, clip_min=-40, clip_max=100):
    return np.clip(image, clip_min, clip_max)

def normalize_image(image, clip_min=-40, clip_max=100):
    return (image - clip_min) / (clip_max - clip_min + 1e-5)  # avoid div by zero
