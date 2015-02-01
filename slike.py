from os import listdir
from os.path import isfile, join
from PIL import Image

def img_size(img):
    width, height = Image.open(img).size
    return ' width="' + str(width) + 'px" height="' + str(height) + 'px" '

onlyfiles = [ '<a href="slike/' + f + '" title="" data-gallery>\n' +
                '<img src="slike/thumbnails/' + f + '"' + img_size('slike/thumbnails/' + f) + ' >\n' +
                '</a>\n'
                for f in listdir('slike') if isfile(join('slike',f)) ]

with open('slike.txt', 'w') as file:
    for f in onlyfiles:
        file.write(f)
