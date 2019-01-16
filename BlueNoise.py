# !/usr/bin/python
#  -*- coding: utf-8 -*-
"""
    Author:Shen Weijie
    Date:2018/12/30
    Software:生成Blue Noise
"""
from utils import *
from scipy.misc import imsave
import cv2

# 生成高斯白噪声
def CreateWhiteNoise(width,height,pointsNum):
    # 保存像素点的list
    points = []
    for num in range(pointsNum):
        # 随机生成像素点坐标
        x = int(random.uniform(0,width))
        y = int(random.uniform(0,height))
        points.append([x,y])
    print("生成高斯白")
    return points

def BlueNoise(blursigma,width,height,num,scale):
    blurSize = int(PixelsForSigam(blursigma)|1)
    WhiteNoise = CreateWhiteNoise(width, height,num)
    img = np.ones([width,height])
    # 测试一下用0~255
    for i in range(width):
        for j in range(height):
            img[i][j]=255
    print("测试用0~255成功")
    for point in WhiteNoise:
        point_x = point[0]
        point_y = point[1]
        img[point_x,point_y] = 0
    print("将像素点的灰度值设为0")
    for iter in range(BlursIter):
        print("blursigma:",blursigma)
        img -= cv2.GaussianBlur(img, (blurSize,blurSize), blursigma)
        print("第",iter,"次迭代")
    point_img = AddBias(img,scale)
    print("通过滤波器成功")
    # Spectrum(point_img)
    spectrum_img = Fourier(point_img)
    print("傅里叶变换成功")
    plt = Spectrum(spectrum_img)
    plt.savefig('./BlueNoiseSpectrumPlot.jpg')
    plt.close()
    print("生成波形图")
    imsave('./BlueNoise.jpg', point_img)
    print("生成点阵图")
    imsave('./BlueNoiseSpectrum.jpg',spectrum_img)
    print("生成频谱图")


if __name__ == '__main__':
    BlueNoise(1.0,200,200,2457,0.05)