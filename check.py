#チェスのコーナーの座標を出力する
import numpy as np
import cv2
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0)

while True:
  ret, frame = cap.read()
  flat_chess_board = frame
  found, corners = cv2.findChessboardCorners(flat_chess_board,(7,10))
  if found:
    print("find")
    flat_chess_copy = flat_chess_board.copy()
    #コーナーの数は7x10
    cv2.drawChessboardCorners(flat_chess_copy, (7, 10), corners, found)
    corners_relative = []
    for j in corners:
      for k in j:
        point = []
        #chessは縦長
        point.append(k[0])
        point.append(k[1])
        corners_relative.append(point)
    print(corners_relative)
    #print(corners[0][0][0])
    cv2.imshow('img',flat_chess_copy)
  else:
    print("false")
    cv2.imshow('img', frame)
  k = cv2.waitKey(1) & 0xFF

  if k == ord('q'):
    np.savetxt("corners.csv", corners_relative, delimiter=",")
    break
  elif k == ord('c'):
    cv2.imwrite('./img/00.png', frame)

