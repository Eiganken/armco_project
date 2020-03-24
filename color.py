#差分とって浮き出たところの色を確認する
import cv2
import numpy as np

class Color():
  def __init__(self, low_color=np.array([0, 0, 100]), high_color=np.array([180, 45, 255]), area_ratio_threshold=0.01):

    self.low_color = low_color
    self.high_color = high_color
    self.area_ratio_threshold = area_ratio_threshold

  def detect_color(self, img='./img/diff.jpg'):
    img_diff = cv2.imread(img)
    h, w, c = img_diff.shape
    hsv = cv2.cvtColor(img_diff, cv2.COLOR_BGR2HSV)
    ex_img = cv2.inRange(hsv, self.low_color, self.high_color)
    contours, hierarchy = cv2.findContours(
        ex_img,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
        )

    #面積計算
    areas = np.array(list(map(cv2.contourArea, contours)))

    if len(areas) == 0 or np.max(areas) / (h*w) < self.area_ratio_threshold:
      print('NONE')
      return None
    else:
      max_idx = np.argmax(areas)
      max_area = areas[max_idx]
      result = cv2.moments(contours[max_idx])
      x = int(result["m10"]/result["m00"])
      y = int(result["m01"]/result["m00"])
#      cv2.circle(img_diff, (x, y), 10, (0, 0, 255), -1)
#      cv2.imwrite('./img/diff.jpg', img_diff)
#      while True:
#        cv2.imshow('w', img_diff)
#        key = cv2.waitKey(1) & 0xFF
#        if key == 27:
#          cv2.destroyWindow('w')
#          break
    return (x, y)

  #カラーと比較する
  def compare(self, x, y):
    img = cv2.imread('./img/front.jpg')
    pixelValue = img[x, y]

    print('B:'+str(pixelValue[0])+"\n"+
        'G:'+str(pixelValue[1])+"\n"+
        'R:'+str(pixelValue[2])
        )
    #点を打つ
    cv2.putText(img, 'detected color:', (5, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), thickness=2)
    cv2.circle(img, (x, y), 10, (0, 0, 255))
    cv2.circle(img, (220, 15), 10, (int(pixelValue[0]), int(pixelValue[1]), int(pixelValue[2])), -1)
    #img
    cv2.imwrite('./img/front_.jpg', img)
    img_ = cv2.imread('./img/front_.jpg')

    while True:
      cv2.imshow('img_', img_)
      key = cv2.waitKey(1) & 0xFF
      if key == 27:
        break

#Color().detect_color('./img/diff.jpg')

