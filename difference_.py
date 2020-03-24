import cv2
import os

def save_frame_camera_key():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        return

    n = 0
    while True:
        ret, frame = cap.read()
        cv2.imshow('frame', frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('f'):
            cv2.imwrite('./img/frontground_image.jpg', frame)
        if key == ord('b'):
            cv2.imwrite('./img/background_image.jpg', frame)

        elif key == ord('q'):
            break
    cv2.destroyWindow('frame')

if __name__ == '__main__':
    save_frame_camera_key()
    # 画像の読み込み
    img_src1 = cv2.imread("./img/background_image.jpg", 1)
    img_src2 = cv2.imread("./img/frontground_image.jpg", 1)

    fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()

    fgmask = fgbg.apply(img_src1)
    fgmask = fgbg.apply(img_src2)

    # 表示
    i = 100
    while i > 1:
        fgmask = cv2.medianBlur(fgmask, ksize=3)
        i = i - 1
    cv2.imshow('frame',fgmask)

    # 検出画像
    bg_diff_path  = './img/diff.jpg'
    cv2.imwrite(bg_diff_path,fgmask)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
