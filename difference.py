#2つの画像の差分をとって保存

import cv2
import os

class Difference():
  def __init__(self, img_back, img_front, roop_time):
    self.roop_time = roop_time
    self.img_back = img_back
    self.img_front = img_front

  #画像の読み込み, 差分, 保存
  def read_img(self):
    #読み込み
    img_src1 = cv2.imread(self.img_back, 1)
    img_src2 = cv2.imread(self.img_front, 1)

    #差分
    fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()
    fgmask = fgbg.apply(img_src1)
    fgmask = fgbg.apply(img_src2)

    while self.roop_time > 1:
      fgmask = cv2.medianBlur(fgmask, ksize=3)
      self.roop_time = self.roop_time - 1

    cv2.imwrite('./img/diff.jpg', fgmask)
