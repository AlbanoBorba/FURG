import numpy as np
from PIL import Image


pix = np.asarray(Image.open('imgglauber/fotografo.tif'))
pix2 = np.asarray(Image.open('imgglauber/placa.tif'))
edited = pix
edited.setflags(write=1)
i = 0
for j in range(1000):
    i = j * 0.001
    A = 1 - i
    B = i
    print A, B
    edited = (A * pix) + (B * pix2)
    if j % 50 == 0:
        im = Image.fromarray(np.uint8(edited))
        im.save('/home/puf3zin/FURG/graficos/imgglauber/transitions/transition%d.tif' % j)
