import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import random

def open_images():
    images = []
    for i in range(1, 11):
        pic = Image.open("images/%d.jpg" % i)
        pix = np.array(pic)
        images.append(pix.astype(np.int16))
    return images
    
def to_grayscale(images):
    grayscales = []
    for image in images:
        grayscales.append(np.mean(image, axis=2))
    return grayscales

def get_errors(images, mean_pix):
    error_pixs = []
    for image in images:
        error_pixs.append(np.abs(np.mean(mean_pix - image, axis=2)))
    return error_pixs

def square_set(image_set):
    squared_set = []
    for image in image_set:
        squared_set.append(np.square(image))
    return squared_set
    
def calculate_stats(images):
    mean_pix = np.mean(images, axis=0)
    var_pix = np.var(images, axis=0)
    std_pix = np.sqrt(var_pix)
    return mean_pix, var_pix, std_pix

def get_lines(mean_im, std_im):
    line = random.randint(0, len(mean_im))
    mean_line = mean_im[line]
    plus_std = mean_im[line] + std_im[line]
    minus_std = mean_im[line] - std_im[line]
    return mean_line[100:200], plus_std[100:200], minus_std[100:200]
    
def get_min_levels(image):
    dim1 = len(image)
    dim2 = len(image[0])
    lowest = [255, 255, 255]
    for channel in xrange(3):
        for i in xrange(dim1):
            for j in xrange(dim2):
                if image[i][j][channel] < lowest[channel]:
                    lowest[channel] = image[i][j][channel]
    return lowest

def get_max_levels(image):
    dim1 = len(image)
    dim2 = len(image[0])
    highest = [0, 0, 0]
    for channel in xrange(3):
        for i in xrange(dim1):
            for j in xrange(dim2):
                if image[i][j][channel] > highest[channel]:
                    highest[channel] = image[i][j][channel]
    return highest

# open images #
images = open_images()
grayscale_images = to_grayscale(images)

# letra a #
mean_im, var_im, std_im = calculate_stats(images)
mean_gs, var_gs, std_gs = calculate_stats(grayscale_images)

# letra b #
a, b, c = get_lines(mean_gs, std_gs)

t = range(100, 200)
red_line = mlines.Line2D([], [], color='red', label='mean')
green_line = mlines.Line2D([], [], color='green', label='mean + std dev')
blue_line = mlines.Line2D([], [], color='blue', label='mean - sd dev')

plt.figure(1)
plt.title('slice of random line from pixels [100:200]')
plt.plot(t, a, 'r', t, b, 'g', t, c, 'b')
plt.legend(handles=[red_line, green_line, blue_line])
plt.xlabel('pixel')
plt.ylabel('value')
plt.savefig('images/slice.png')

# letra c #
for image in images:
    print get_max_levels(image), get_min_levels(image)

histogram = np.histogram(mean_gs, range(255))
pixels = range(255)

plt.figure(2)
plt.title('mean image histogram')
plt.plot(histogram[1][1:], histogram[0])
plt.xlabel('value')
plt.ylabel('number of pixels')
plt.savefig('images/histogram.png')

# calculate each image's error #
error_ims = get_errors(images, mean_im)


# save stat images #
mean_pic = Image.fromarray(mean_im.astype(np.uint8))
mean_pic.save("images/mean_pic.jpeg")

var_pic = Image.fromarray(var_im.astype(np.uint8))
var_pic.save("images/var_pic.jpeg")

std_pic = Image.fromarray(std_im.astype(np.uint8))
std_pic.save("images/std_pic.jpeg")

# save error images #
for i, error_pix in enumerate(error_ims):
    #print np.max(error_pix)
    tmp_pic = Image.fromarray(error_pix.astype(np.uint8))
    tmp_pic.save("images/error_%d.jpeg" % (i + 1))
