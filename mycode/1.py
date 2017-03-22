#encoding=utf-8
###���õ���ܶȼ���
import image,imageenhance,imagefilter,imagedraw
import sys
from pytesser import *
#���㷶Χ�ڵ�ĸ���
def numpoint(im):
    w,h = im.size
    data = list( im.getdata() )
    mumpoint=0
    for x in range(w):
        for y in range(h):
            if data[ y*w + x ] !=255:#255�ǰ�ɫ
                mumpoint+=1
    return mumpoint
                
#����5*5��Χ�ڵ���ܶ�
def pointmidu(im):
    w,h = im.size
    p=[]
    for y in range(0,h,5):
        for x in range(0,w,5):
            box = (x,y, x+5,y+5)
            im1=im.crop(box)
            a=numpoint(im1)
            if a<11:##���5*5��Χ��С��11���㣬��ô���ò���ȫ����Ϊ��ɫ��
                for i in range(x,x+5):
                    for j in range(y,y+5):
                        im.putpixel((i,j), 255)
    im.save(r'img.jpg')
        
def ocrend():##ʶ��
    image_name = "img.jpg"
    im = image.open(image_name)
    im = im.filter(imagefilter.medianfilter())
    enhancer = imageenhance.contrast(im)
    im = enhancer.enhance(2)
    im = im.convert('1')
    im.save("1.tif")
    print image_file_to_string('1.tif')    
    
if __name__=='__main__':
    image_name = "1.png"
    im = image.open(image_name)
    im = im.filter(imagefilter.detail)
    im = im.filter(imagefilter.medianfilter())
    
    enhancer = imageenhance.contrast(im)
    im = enhancer.enhance(2)
    im = im.convert('1')
    ##a=remove_point(im)
    pointmidu(im)
    ocrend()