from PIL import Image
import numpy as np

im = Image.open("ARTEMIS_HQ_updated_image.png")

arr = np.array(im)
im = Image.fromarray(arr*50)
im.save("ARTEMIS_DECODED.png")

