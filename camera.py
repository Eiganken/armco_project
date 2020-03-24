#キーを入力すると./img/*.jpgが保存される
#qで終了
import cv2
import os

class Camera():
    def __init__(self, name):
        self.name = name

    def save_frame_camera_key(self):
        cap = cv2.VideoCapture(0)

        if not cap.isOpened():
            print('Error. Camera was not found.')
            return

        while True:
            ret, frame = cap.read()
            cv2.imshow('frame', frame)
            key = cv2.waitKey(1) & 0xFF

            if key == ord('q'):
                break
            else:
                cv2.imwrite('./img/'+ self.name, frame)
        cv2.destroyWindow('frame')
