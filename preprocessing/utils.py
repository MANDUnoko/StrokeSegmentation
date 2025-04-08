import cv2

def resize_image(image, size=(512, 512)):
    return cv2.resize(image, size, interpolation=cv2.INTER_LINEAR)

import numpy as np

def resize_volume(volume, size=(512, 512)):
    """
    3D 볼륨 데이터를 받아 각 슬라이스를 지정한 크기로 리사이즈합니다.
    volume: 3D numpy array, shape는 (H, W, D)
    size: tuple, 리사이즈할 목표 크기 (width, height)
    """
    resized_slices = []
    # 3번째 축을 슬라이스로 가정 (예: axial 슬라이스)
    for i in range(volume.shape[2]):
        slice_ = volume[:, :, i]
        resized_slice = cv2.resize(slice_, size, interpolation=cv2.INTER_LINEAR)
        resized_slices.append(resized_slice)
    
    # 새로운 3D 배열로 스택
    return np.stack(resized_slices, axis=2)
