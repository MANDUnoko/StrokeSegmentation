import numpy as np

def dicom_to_hu(ds):
    image = ds.pixel_array.astype(np.float32)
    slope = float(ds.get('RescaleSlope', 1))
    intercept = float(ds.get('RescaleIntercept', 0))
    return image * slope + intercept