import numpy as np
import os
import torch

from preprocessing.hu_utils import dicom_to_hu
from preprocessing.brain_mask import apply_brain_mask
from preprocessing.windowing import window_image, normalize_image
from preprocessing.utils import resize_image

# dicom 용
def preprocess_ct_with_mask(ds, brain_mask):
    image = dicom_to_hu(ds)
    image = apply_brain_mask(image, brain_mask)
    image = window_image(image, -40, 100)
    image = normalize_image(image, -40, 100)
    image = resize_image(image, (512, 512))
    return image

# nii 용 (brain mask, mask 다 nii 형식인 게 작업 편함)
def preprocess_nii_with_mask(image, brain_mask):
    image = image * brain_mask  # skull stripping
    image = window_image(image, -40, 100)
    image = normalize_image(image, -40, 100)
    image = resize_image(image, (512, 512))
    return image.astype(np.float32)


def save_preprocessed(image, save_path):
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    image = image.astype(np.float32)  # 🔥 float64 방지
    tensor = torch.tensor(image).unsqueeze(0)  # (1, H, W)
    torch.save(tensor.float(), save_path)  