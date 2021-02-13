def main():
  import numpy as np
  import cv2

  cap = cv2.VideoCapture(0) # Insert file name instead of 0 to open a video file

  # To save a video
  # fourcc = cv2.VideoWriter_fourcc(*'XVID')
  # out = cv2.VideoWriter('output.mp4',fourcc, cap.get(5), (640,480))

  while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()
    frame = cv2.flip(frame,1)

    # Convert to gray
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the frame or the gray
    cv2.imshow('frame', frame)
    print(cap.get(5))
    if cv2.waitKey(1) == ord('s'):
        cv2.imwrite('face.jpg',frame)
        break

  cap.release()
  
  # If you are saving video uncomment out.release()
  # out.release()
  
  cv2.destroyAllWindows()
if __name__ == '__main__':
  main()
