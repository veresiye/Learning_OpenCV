def main():
  import numpy as np
  import cv2

  cap = cv2.VideoCapture(0)

  face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

  while cap.isOpened():
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        frame = frame[y:y+h, x:x+w]
    cv2.imshow('img', frame)
    k = cv2.waitKey(1)
    if k == ord('s'):
        cv2.imwrite('face.jpg', frame)
    elif k == ord('q'):
        break

  cap.release()
  cv2.destroyAllWindows()
if __name__ == '__main__':
  main()
