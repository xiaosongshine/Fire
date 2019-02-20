import cv2
import numpy as np

video_file = "fire.jpg"




while True:
    frame = cv2.imread(video_file)

    blur = cv2.GaussianBlur(frame, (21, 21), 0)
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

    lower = np.array([1, 50, 50], dtype="uint8")
    upper = np.array([9, 255, 255], dtype="uint8")
    mask = cv2.inRange(hsv, lower, upper)

    output = cv2.bitwise_and(frame, hsv, mask=mask)
    cv2.imshow("output", output)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
