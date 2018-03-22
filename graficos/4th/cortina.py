import numpy as np
from PIL import Image


pix = np.asarray(Image.open('imgglauber/fotografo.tif'))
pix2 = np.asarray(Image.open('imgglauber/placa.tif'))
edited = pix
edited.setflags(write=1)
for i, col in enumerate(pix):
    edited[i] = pix2[i]
    if i % 50:
        im = Image.fromarray(np.uint8(pix))
        im.save('/home/puf3zin/FURG/graficos/imgglauber/transitions/cortina%d.tif' % i)
