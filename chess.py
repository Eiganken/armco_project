#敷かれてるchessのマスの座標を見る
import numpy  as np
import cv2
import matplotlib.pyplot as plt

class Chess():
  def __init__(self, chess_squares_type)
    self.chess_squares_type = chess_squares_type

  def check_chess(self, file_name):
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
      print('Error. Camera was not found.')
      return

    while True:
      ret, frame = cap.read()
      flat_chess_board = frame
      found, corners = cv2.findChessboardCorners(flat_chess_board, self.chess_squares_type)
      if found:
        flat_chess_copy = flat_chess_board.copy()
        cv2.drawChessboardCorners(flat_chess_copy, self.chess_squares_type, corners, found)
        corners_rerative = []
        for j in corners:
          for k in j:
            point = []
            point.append(k[0])
            point.append(k[1])
            corners_relative.append(point)
        print(corners_relative)
        cv2.imshow('img', flat_chess_copy)

      else:
        print("Not found")
        cv2.imshow('img', frame)
      k = cv2.waitKey(1) & 0xFF

      if k == ord('q'):
        np.savetxt("corners.csv", corners_relative, delimiter=",")
        break
      elif k == ord('c'):
        cv2.imwrite(filename, frame)
