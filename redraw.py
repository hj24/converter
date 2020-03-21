import os
import re

import cv2
from PIL import Image, ImageDraw, ImageFont

from cfg import parsedir, newdir
from cfg import placeholder, phfont, phfontsize


def draw(pic):
    img = cv2.imread("{}/{}".format(parsedir, pic))
    print('*********************')
    img = img[:, :, (2, 1, 0)]

    blank = Image.new("RGB", [len(img[0]), len(img)], "white")
    pen = ImageDraw.Draw(blank)

    font = ImageFont.truetype(phfont, size=phfontsize - 1)
    print(len(img), len(img[0]))
    for i in range(0, len(img), phfontsize):
        for j in range(0, len(img[i]), phfontsize):
            text = placeholder
            pen.ink = img[i][j][0] + img[i][j][1] * 256 + img[i][j][2] * 256 * 256
            pen.text([j, i], text[int(j / phfontsize) % len(text)], font=font)
            print('完成处理——', i, j)

    blank.save("{}/new_{}".format(newdir, pic), 'jpeg')

def transfer():
    if not os.path.exists(newdir):
        os.mkdir(newdir)

    filelist = os.listdir(parsedir)
    filelist.sort(key=lambda x: int(re.findall(r'\d+', x)[0]))

    # 解析出来的最后一帧是打不开的，需要截掉
    for file in filelist[:len(filelist) - 1]:
        print(file)
        draw(file)

if __name__ == "__main__":
    transfer()
