def apply_brain_mask(image, brain_mask):
    return image * brain_mask  # or image[brain_mask == 0] = 0