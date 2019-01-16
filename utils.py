# !/usr/bin/python
#  -*- coding: utf-8 -*-
"""
    Author:Shen Weijie
    Date:2018/12/30
    Software:采样和傅里叶变换等功能函数的定义
"""
import random
import math
import pylab as pl
import numpy as np
import matplotlib.pyplot as plt

# 固定参数的设置
BlursIter = 5
BlurThreshold = 0.005
Pi = 3.14159265359
maxBlurSigma = 3.0
alpha = 0.95


def PixelsForSigam(blursigma):
    """
    :param blursigma: 模糊系数/图像如何通过低通滤波器
    :return: 返回需要使用有值高斯核的像素数
    """
    return int(math.sqrt(-2.0*math.log(BlurThreshold)*(blursigma**2))*2.0+1.0)+1

def Histeq(img, nbr_bins=256):
    """
        图像直方图均衡化
    :param img: 图像
    :param nbr_bins:像素值范围[0~255]
    :return:均衡化直方图后的图像
    """
    # 获取直方图p(r)
    imhist, bins = pl.histogram(img.flatten(), nbr_bins, normed=True)
    # 获取T(r)
    cdf = imhist.cumsum()  # cumulative distribution function
    cdf = 255 * cdf / cdf[-1]
    # 获取s，并用s替换原始图像对应的灰度值
    result = pl.interp(img.flatten(), bins[:-1], cdf)
    return result.reshape(img.shape)

def Fourier(img):
    """
        实现图像的傅里叶变换
    :param img: 图像
    :return: 傅里叶变换后的图像
    """
    f = np.fft.fft2(img)  # 快速傅里叶变换算法得到频率分布
    fshift = np.fft.fftshift(f)  # 默认结果中心点位置是在左上角，转移到中间位置
    fimg = np.log(np.abs(fshift))  # fft 结果是复数，求绝对值结果才是振幅
    return fimg

def AddBias(img,scale):
    """
        增加扰动
    :param img: 图像
    :param scale: 扰动规模
    :return: 增加扰动后的图像
    """
    # 计算图像中x方向和y方向上的像素点数
    x_pixelNum = img.shape[0]
    y_pixelNum = img.shape[1]
    max = img.max()
    bias = random.uniform(-(scale/max), (scale/max))
    for x in range(x_pixelNum):
        for y in range(y_pixelNum):
            img[x][y] += bias
    return img

def Spectrum(img):
    width = img.shape[0]
    height = img.shape[1]
    width_mid = int(width/2)
    height_mid = int(height/2)
    pixelValue = []
    for index in range(width-width_mid):
        pixelValue.append(img[width_mid+index][height_mid])
    x = [i for i in range(width-width_mid)]
    print("x:",len(x))
    plt.plot(x,pixelValue)
    return plt

