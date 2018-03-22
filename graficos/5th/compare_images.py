import numpy as np
from PIL import Image

images = []
flag = False

for i in range(1, 11):
    pic = Image.open("images/%d.jpg" % i)
    pix = np.array(pic)
    images.append(pix.astype(np.int16))

errors = []

#for i in xrange(10):
#    print images[i][540][1000]

mean_pix = np.copy(images[9])

for i in xrange(9):
    mean_pix += images[i]

mean_pix = mean_pix / 10.0
dev_pix = mean_pix - images[9]

for i in xrange(9):
    dev_pix += (mean_pix - images[i])

sqr_dev_pix = np.square(dev_pix)

variance_pix = sqr_dev_pix / 10.0
std_dev_pix = np.sqrt(variance_pix)

mean_pic = Image.fromarray(mean_pix.astype(np.uint8))
mean_pic.save("images/mean_pic.jpeg")

print mean_pix[100][100]
print variance_pix[100][100]
print std_dev_pix[100][100]


"""
for i in xrange(10):
    this_error = 0
    for j in xrange(10):
        if i != j:
            subtracted = images[i] - images[j]
            print i, j
            print subtracted
            this_error += np.mean(subtracted)
    this_error /= 9.0
    errors.append(this_error)

print errors
"""