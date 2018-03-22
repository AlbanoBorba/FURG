import numpy as np
from PIL import Image


pix = np.asarray(Image.open('imgglauber/Mamografia_01.jpg'))

edited = pix
edited.setflags(write=1)

mini = np.amin(pix)
maxi = np.amax(pix) - 40

A = 255.0 / (maxi - mini)
B = A * mini


edited = np.clip(A * pix - B, 0, 255)

im = Image.fromarray(np.uint8(edited))
im.save('/home/puf3zin/FURG/graficos/imgglauber/Mamografia_02.jpg')
