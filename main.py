import cv2
import camera
import difference
import color

def main():

  #back_ground撮影
  camera_module = camera.Camera('back.jpg')
  camera_module.save_frame_camera_key()

  #front_ground撮影
  camera_module = camera.Camera('front.jpg')
  camera_module.save_frame_camera_key()

  #差分を取る
  diff = difference.Difference('./img/back.jpg', './img/front.jpg', 100)
  diff.read_img()

  color_module = color.Color()
  x, y = color_module.detect_color()
  color_module.compare(x, y)

if __name__ == '__main__':
  main()
