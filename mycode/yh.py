# ?????,????????????
import Image  
import ImageEnhance  
import ImageFilter  
import sys
import os
#from pytesseract import *

try:
    from pyocr import pyocr
    from PIL import Image
except ImportError:
    print '??????,???pip??,pytesseract?????:'
    print 'http://www.lfd.uci.edu/~gohlke/pythonlibs/#pil'
    print 'http://code.google.com/p/tesseract-ocr/'
    raise SystemExit

# ???  
threshold = 140  
table = []  
for i in range(256):  
    if i < threshold:  
        table.append(0)  
    else:  
        table.append(1)  
  
#??????  
#???????? ????????  
rep={'O':'0',  
    'I':'1','L':'1',  
    'Z':'2',  
    'S':'8'  
    };  
  
def  getverify1(name):
    tools = pyocr.get_available_tools()[:]
    if len(tools) == 0:
        print("No OCR tool found")
        sys.exit(1)
    print("Using '%s'" % (tools[0].get_name()))
    # print tools[0].image_to_string(Image.open('123.png'),lang='eng')#D:\\
    # print tools[0].image_to_string(Image.open('3434.png'),lang='chi_sim')#D:\\
  #  while (1):

    #????  
    im = Image.open(name)  
    #??????
    imgry = im.convert('L')
    #????
    imgry.save('g'+name)  
    #???,???????,threshold???? 
    out = imgry.point(table,'1')  
    out.save('b'+name)  
    #??  
    text = tools[0].image_to_string(out,lang='eng')
    #????  
    text = text.strip()  
    text = text.upper();    
    for r in rep:  
        text = text.replace(r,rep[r])   
    #out.save(text+'.jpg')  
    print text  
    return text

getverify1('xxx.png')  #??????????????????,??????????