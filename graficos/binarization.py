import numpy as np
from PIL import Image


pix = np.asarray(Image.open('imgglauber/im1.tif'))

edited = pix
edited.setflags(write=1)

edited = np.where(pix > 40, 255, 0)

im = Image.fromarray(np.uint8(edited))
im.save('/home/puf3zin/FURG/graficos/imgglauber/im1_bin.tif')
