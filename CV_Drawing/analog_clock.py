def main():
  import cv2
  import numpy as np
  import datetime
  import math


  def array_to_tuple(arr):
    return tuple(arr.reshape(1, -1)[0])

  colors = {'blue': (255, 0, 0), 'green': (0, 255, 0), 'red': (0, 0, 255), 'yellow': (0, 255, 255),
          'magenta': (255, 0, 255), 'cyan': (255, 255, 0), 'white': (255, 255, 255), 'black': (0, 0, 0),
          'gray': (125, 125, 125), 'rand': np.random.randint(0, high=256, size=(3,)).tolist(),
          'dark_gray': (50, 50, 50), 'light_gray': (220, 220, 220)}

  image = np.zeros((640, 640, 3), dtype="uint8")

  image[:] = colors['black']

  # Coordinates to define the origin for the hour markings:
  hours_orig = np.array(
    [(620, 320), (580, 470), (470, 580), (320, 620), (170, 580), (60, 470), (20, 320), (60, 170), (169, 61), (319, 20),
     (469, 60), (579, 169)])

  # Coordinates to define the destiny for the hour markings:
  hours_dest = np.array(
    [(600, 320), (563, 460), (460, 562), (320, 600), (180, 563), (78, 460), (40, 320), (77, 180), (179, 78), (319, 40),
     (459, 77), (562, 179)])

# We draw the hour markings:
  for i in range(0, 12):
    cv2.line(image, array_to_tuple(hours_orig[i]), array_to_tuple(hours_dest[i]), colors['light_gray'], 3)

  cv2.circle(image, (320, 320), 310, colors['dark_gray'], 8)

  # We make a copy of the image with the "static" information
  image_original = image.copy()

  while True:
    # Get current time from the date:
    time_now = datetime.datetime.now().time()

    hour = math.fmod(time_now.hour, 12)
    minute = time_now.minute
    second = time_now.second

    # Get the hour, minute and second angles:
    second_angle = math.fmod(second * 6 + 270, 360)
    minute_angle = math.fmod(minute * 6 + 270, 360)
    hour_angle = math.fmod((hour * 30) + (minute / 2) + 270, 360)

    # Draw the lines corresponding to the hour, minute and second needles
    second_x = round(320 + 310 * math.cos(second_angle * 3.14 / 180))
    second_y = round(320 + 310 * math.sin(second_angle * 3.14 / 180))
    cv2.line(image, (320, 320), (second_x, second_y), colors['red'], 2)

    minute_x = round(320 + 260 * math.cos(minute_angle * 3.14 / 180))
    minute_y = round(320 + 260 * math.sin(minute_angle * 3.14 / 180))
    cv2.line(image, (320, 320), (minute_x, minute_y), colors['light_gray'], 8)

    hour_x = round(320 + 220 * math.cos(hour_angle * 3.14 / 180))
    hour_y = round(320 + 220 * math.sin(hour_angle * 3.14 / 180))
    cv2.line(image, (320, 320), (hour_x, hour_y), colors['light_gray'], 6)

    # Finally, a small circle, corresponding to the point where the three needles joint, is drawn:
    cv2.circle(image, (320, 320), 10, colors['white'], -1)

    # Show image:
    cv2.imshow("clock", image)

    # We get the image with the static information:
    image = image_original.copy()

    if cv2.waitKey(1000) & 0xFF == ord('q'):
        break

  cv2.destroyAllWindows()
if __name__ == '__main__':
  main()
