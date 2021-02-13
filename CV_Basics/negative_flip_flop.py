def main():
  import cv2
  import numpy as np

  image = cv2.imread('image.jpg', 0)

  for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        image[i][j] = 255 - image[i][j]

  height, width = image.shape[:2]
  M = np.float32([[1, 0, 2], [0, 1, 2]])
  rot = cv2.warpAffine(image, M, (width+200, height+200))
  M = cv2.getRotationMatrix2D((width / 2.0, height / 2.0), 45, 0.5)
  rot = cv2.warpAffine(rot, M, (width, height))

  for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        if rot[i][j] != 0:
            image[i][j] = rot[i][j]

  cv2.imshow('im', image)
  cv2.waitKey(0)
  cv2.destroyAllWindows()
if __name__ == '__main__':
  main()
