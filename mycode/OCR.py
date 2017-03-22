# coding=utf-8
__author__ = 'syq'

#https://github.com/tesseract-ocr
import sys
import time
import datetime

reload(sys)
sys.setdefaultencoding('utf-8')

import os
import prtScrn
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
try:
    from pyocr import pyocr
    from PIL import Image
except ImportError:
    print '??????,???pip??,pytesseract?????:'
    print 'http://www.lfd.uci.edu/~gohlke/pythonlibs/#pil'
    print 'http://code.google.com/p/tesseract-ocr/'
    raise SystemExit
tools = pyocr.get_available_tools()[:]
if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1)
print("Using '%s'" % (tools[0].get_name()))
list = prtScrn.createtemplate();
rect = (0, 0, 130,110)
prtScrn.readtemplate2Mem(list)
for i in range(6000):
    print tools[0].image_to_string(prtScrn.getImgObj(i),lang='fontyp')
