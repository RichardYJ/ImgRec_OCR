# -*- coding: utf-8 -*-
'''import ImageGrab
import ImageEnhance
import Image
from numpy import *
import numpy as np
import imutils
import os
import pytesseract
from PIL import Image
import cv2
import os;
import urllib;
from PIL import Image as im;
from PIL import ImageEnhance;
global gTemplateList
gTemplateList= [];

def process(img):  # 处理图片
    enhancer = ImageEnhance.Color(img);
    enhancer = enhancer.enhance(0);  
    enhancer = ImageEnhance.Brightness(enhancer);  
    enhancer = enhancer.enhance(2);  
    enhancer = ImageEnhance.Contrast(enhancer);
    enhancer = enhancer.enhance(8);  
    enhancer = ImageEnhance.Sharpness(enhancer);
    enhancer = enhancer.enhance(20);  
    return enhancer;


def delims(image, numbers=4, index=0, rect=()): 
    if len(rect):  
        image = image.crop((rect));
    width, height = image.size;
    for i in range(numbers):
        img = image.crop((int(width / numbers) * i, 0, int(width / numbers) * (i + 1), height));
        img.save("./temp/%d_%d.jpg" % (index, i));


def createtempfile(numbers=4, rect=()):  
    list = os.listdir("./number");
    for index, i in enumerate(list):
        delims(process("./number/{0}".format(i)), numbers, index, rect);


def createtemplate(): 
    list = [];
    for root, dirs, files in os.walk("./template"):
        for file in files:
            list.append(os.path.join(root, file));
    return list;

def readtemplate2Mem(template): 
    global gTemplateList
    for item in template:
        temp = im.open(item, "r");
        gTemplateList.append((temp, os.path.basename(item).split(".")[0]));
    return gTemplateList

def recognize(img, numbers, template, rect):  
    global gTemplateList
    if len(rect):
        image = process(img).crop((rect));
    if not len(template):
        print("模板列表不能为空,请先筛选作为模板的文件并放到template文件夹内!")
        return;
    width, height = image.size;
    name = "";
    for i in range(numbers):
        img = image.crop((int(width / numbers) * i, 0, int(width / numbers) * (i + 1), height));
        subwidth, subheight = img.size;
        rank = [];
        for j in range(len(gTemplateList)):
            temp = gTemplateList[j][0]#im.open(item, "r");
            diff = 0;
            for w in range(subwidth):
                for h in range(subheight):
                    if (img.getpixel((w, h)) != temp.getpixel((w, h))):
                        diff += 1;
            rank.append((diff, gTemplateList[j][1]))#os.path.basename(item).split(".")[0]));
        rank.sort();
        name += str(rank[0][1]);
    print name


def downpic(numbers=10):  
    url = "http://system.ruanko.com/validateImage.jsp";
    for i in range(numbers):
        open("./number/%d.jpg" % i, "wb").write(urllib.request.urlopen(url).read());


def createdir():
    cwd = os.getcwd() + "\\";
    try:  
        os.mkdir(cwd + "number");
    except:  
        pass;
    try:
        os.mkdir(cwd + "temp");
    except:
        pass;
    try:
        os.mkdir(cwd + "template");
    except:
        pass;
    try:
        os.mkdir(cwd + "recognized");
    except:
        pass;
'''

def getImgObj(ind=0):
    bbox = (1818, 1086, 1830, 1096)
    img = ImageGrab.grab(bbox)
    img = img.resize((130,110))
#    a = array(img)
#    for i in xrange(len(a)):
#        for j in xrange(len(a[i])):
#            if a[i][j][0] == 255:
#                a[i][j] = [0, 0, 0]
#            else:
#                a[i][j] = [255, 255, 255]
#    im = Image.fromarray(a)
    image_enhancer=img
#    image_enhancer.save("%s.tif"%ind)
    return image_enhancer

'''
def img_tesseract_detect(c_rect, im):
    # 由于使用minAreaRect获得的图像有-90~0的角度，所以给出的坐标顺序也不一定是
    # 转换时候给的，这里需要判断出图像的左上、左下、右上、右下的坐标，便于后面的变换
    pts = c_rect.reshape(4, 2)
    rect = np.zeros((4, 2), dtype="float32")

    # the top-left point has the smallest sum whereas the
    # bottom-right has the largest sum
    s = pts.sum(axis=1)
    rect[0] = pts[np.argmin(s)]
    rect[3] = pts[np.argmax(s)]

    # compute the difference between the points -- the top-right
    # will have the minumum difference and the bottom-left will
    # have the maximum difference
    diff = np.diff(pts, axis=1)
    rect[2] = pts[np.argmin(diff)]
    rect[1] = pts[np.argmax(diff)]

    dst = np.float32([[0, 0], [0, 100], [200, 0], [200, 100]])

    M = cv2.getPerspectiveTransform(rect, dst)
    warp = cv2.warpPerspective(im, M, (200, 100))

    img_show_hook("剪裁识别图像55555555555", warp)

    warp = np.array(warp, dtype=np.uint8)
    radius = 10
    selem = disk(radius)

    # 　使用局部自适应OTSU阈值处理
    local_otsu = rank.otsu(warp, selem)
    l_otsu = np.uint8(warp >= local_otsu)
    l_otsu *= 255

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (4, 4))
    l_otsu = cv2.morphologyEx(l_otsu, cv2.MORPH_CLOSE, kernel)

    img_show_hook("局部自适应OTSU图像6666666", l_otsu)

    print("7777777777识别结果：")
    print(pytesseract.image_to_string(Image.fromarray(l_otsu)))

    cv2.waitKey(0)
    return
'''