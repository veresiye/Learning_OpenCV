def main():
  import numpy as np
  import cv2

  # Create a black image
  img = np.zeros((512,512,3), np.uint8)

  # Draw a diagonal blue line with thickness of 5 px
  img = cv2.line(img,(0,0),(511,511),(255,0,255),5)
  img = cv2.line(img,(0,511),(511,0),(255,0,255),5)
  img = cv2.rectangle(img,(100,100),(512-100,512-100),(255,0,255),5)
  img = cv2.rectangle(img,(3,3),(509,509),(255,0,255),5)
  cv2.imshow('imag', img)
  k = cv2.waitKey(0)
  if k == ord('s'):
    cv2.imwrite("image.jpg", img)
  cv2.destroyAllWindows()
if __name__ == '__main__':
  main()
