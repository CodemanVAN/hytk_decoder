import cv2
import math
import struct
import time
import os
def decode(path,pics,single=True):
    starttime = time.time()
    if single:
        imgfile = os.path.join(path,pics)
        try:
            img = cv2.imread(imgfile,cv2.IMREAD_UNCHANGED)
            imgdata = []
            rawdata = dict()
            #print("图像的形状,返回一个图像的(行数,列数,通道数):",img.shape)
            n = img.size
            
            a = 1
            mode = 4
            
            for i in range(img.shape[0]):
                for j in range(img.shape[1]):
                    p = img[i][j]
                    #BGRA
                    rawdata = dict()
                    rawdata['R'] = p[0]
                    rawdata['G'] = p[1]
                    rawdata['B'] = p[2]
                    imgdata.append(rawdata)
            aa = math.ceil(3*mode/8)
            n = img.size
            j = 0
            k = ""
            current_pixel_index = 1
            word = ""
            blist = []
            blength = 0
            while(current_pixel_index < n and (len(word) == 0 or ord(word[-1])>0 )):
                k = k+str(bin(imgdata[current_pixel_index]['B'] + 256))[-mode:]
                k = k+str(bin(imgdata[current_pixel_index]['G'] + 256))[-mode:]
                k = k+str(bin(imgdata[current_pixel_index]['R'] + 256))[-mode:]
                current_pixel_index = current_pixel_index +1
                for i in range(0,aa):
                    if(len(k) >= 8 and (len(word) == 0 or ord(word[-1]) > 0)):
                        word = word + chr(int(k[0:8],2))
                        k = k[8:]
            #ref to lines#139
            blength = int(word.split(chr(1))[0])
            if(blength <= -1 or not (len(word.split(chr(1))) >2)):
                endtime = time.time()
                print('[!-2]无法处理未知的隐写参数。耗时', str(round(endtime - starttime, 2)),'秒')
                return 0
            blist = []
            if(len(k) >= 8 and j < blength):
                blist.append(int(k[0:8],2))
                k = k[8:]
                j = j + 1
            while (current_pixel_index < n and j < blength):
                k = k+str(bin(imgdata[current_pixel_index]['B'] + 256))[-mode:]
                k = k+str(bin(imgdata[current_pixel_index]['G'] + 256))[-mode:]
                k = k+str(bin(imgdata[current_pixel_index]['R'] + 256))[-mode:]
                current_pixel_index = current_pixel_index +1
                for i in range(0,aa):
                    if(len(k) >= 8 and j<blength):
                        blist.append(int(k[0:8],2))
                        k = k[8:]
                        j = j + 1
            with open(os.path.join('decode_pic',str(word.split(chr(1))[1])),'wb')as fp:
                for x in blist:
                    a = struct.pack('B', x)
                    fp.write(a)
            endtime = time.time()
            print("已经向源文件 " + str(word.split(chr(1))[1]) + "\t写入了 " + str(word.split(chr(1))[0]) + "\t字节,耗时 " + str(round(endtime - starttime, 2))+ "\t秒")
            return 1
        except:
            return 0
    nl=len(pics)
    sf=0
   #os.makedirs('decode_pic')
    for pic in pics:
        imgfile = os.path.join(path,pic)
        try:
            img = cv2.imread(imgfile,cv2.IMREAD_UNCHANGED)
            imgdata = []
            rawdata = dict()
            #print("图像的形状,返回一个图像的(行数,列数,通道数):",img.shape)
            n = img.size
            
            a = 1
            mode = 4
            
            for i in range(img.shape[0]):
                for j in range(img.shape[1]):
                    p = img[i][j]
                    #BGRA
                    rawdata = dict()
                    rawdata['R'] = p[0]
                    rawdata['G'] = p[1]
                    rawdata['B'] = p[2]
                    imgdata.append(rawdata)
            aa = math.ceil(3*mode/8)
            n = img.size
            j = 0
            k = ""
            current_pixel_index = 1
            word = ""
            blist = []
            blength = 0
            while(current_pixel_index < n and (len(word) == 0 or ord(word[-1])>0 )):
                k = k+str(bin(imgdata[current_pixel_index]['B'] + 256))[-mode:]
                k = k+str(bin(imgdata[current_pixel_index]['G'] + 256))[-mode:]
                k = k+str(bin(imgdata[current_pixel_index]['R'] + 256))[-mode:]
                current_pixel_index = current_pixel_index +1
                for i in range(0,aa):
                    if(len(k) >= 8 and (len(word) == 0 or ord(word[-1]) > 0)):
                        word = word + chr(int(k[0:8],2))
                        k = k[8:]
            #ref to lines#139
            blength = int(word.split(chr(1))[0])
            if(blength <= -1 or not (len(word.split(chr(1))) >2)):
                endtime = time.time()
                print('[!-2]无法处理未知的隐写参数。耗时', str(round(endtime - starttime, 2)),'秒')
                continue
            blist = []
            if(len(k) >= 8 and j < blength):
                blist.append(int(k[0:8],2))
                k = k[8:]
                j = j + 1
            while (current_pixel_index < n and j < blength):
                k = k+str(bin(imgdata[current_pixel_index]['B'] + 256))[-mode:]
                k = k+str(bin(imgdata[current_pixel_index]['G'] + 256))[-mode:]
                k = k+str(bin(imgdata[current_pixel_index]['R'] + 256))[-mode:]
                current_pixel_index = current_pixel_index +1
                for i in range(0,aa):
                    if(len(k) >= 8 and j<blength):
                        blist.append(int(k[0:8],2))
                        k = k[8:]
                        j = j + 1
            with open(os.path.join('decode_pic',str(word.split(chr(1))[1])),'wb')as fp:
                for x in blist:
                    a = struct.pack('B', x)
                    fp.write(a)
            endtime = time.time()
            print("已经向源文件 " + str(word.split(chr(1))[1]) + "\t写入了 " + str(word.split(chr(1))[0]) + "\t字节,耗时 " + str(round(endtime - starttime, 2))+ "\t秒")
            sf+=1
            continue
        except:
            continue
    endtime = time.time()
    print("[!-5]" + '耗时', str(round(endtime - starttime, 2)),'秒') 
    return (nl,sf)