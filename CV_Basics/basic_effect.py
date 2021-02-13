def main():
  import cv2
  import numpy as np

  img = cv2.imread('photo.jpg',1)

  for i in range(img.shape[1]):
    img[:,i,2] = round((255*i)/(img.shape[1]))

  for i in range(img.shape[0]):
    img[i,:,2] = round((255*i)/(img.shape[0]))

  cv2.imshow('im',img)
  k = cv2.waitKey(0)
  if k == ord('s'):
    cv2.imwrite('image.jpg',img)
  else:
    cv2.destroyAllWindows()
if __name__ == '__main__':
  main()
