def main():
  import numpy as np
  import cv2

  # Load an color image in grayscale
  img = cv2.imread('photo.jpg',1)

  cv2.namedWindow('image', cv2.WINDOW_KEEPRATIO)
  cv2.imshow('Image',img)
  k = cv2.waitKey(0)
  if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
  elif k == ord('s'): # wait for 's' key to save and exit
    a = 3
  # cv2.imwrite('messigray.png',img)
  else:
    cv2.destroyAllWindows()
if __name__ == '__main__':
  main()
