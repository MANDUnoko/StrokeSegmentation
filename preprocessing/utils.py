import cv2

def resize_image(image, size=(512, 512)):
    return cv2.resize(image, size, interpolation=cv2.INTER_LINEAR)
