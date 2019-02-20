import cv2
import numpy as np

files = "ts.jpg"

def nothing(x):
    pass

def check_color(frame):
    Rt = 24
    St = 64
    cv2.createTrackbar("Rt","bin",49,255,nothing)
    cv2.createTrackbar("St","bin",7,255,nothing)

    Rt = cv2.getTrackbarPos("Rt","bin")
    St = cv2.getTrackbarPos("St","bin")

    blur = cv2.GaussianBlur(frame, (21, 21), 0)
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

    rows,cols,chls = frame.shape
    Bs,Gs,Rs = frame[:,:,0],frame[:,:,1],frame[:,:,2]
    Hs,Ss,Is = hsv[:,:,0],hsv[:,:,1],hsv[:,:,2]
    Bits = np.zeros((rows,cols))
    for i in range(rows):
        for j in range(cols):
            if(Rs[i,j]>Rt and Rs[i,j]>Gs[i,j] and Gs[i,j]>Bs[i,j] and (Ss[i,j]>((255-Rs[i,j])*St/Rt))):
                Bits[i,j] = 255
    cv2.imshow("bin",Bits)

cv2.namedWindow('bin')


cv2.createTrackbar("Rt","bin",24,255,nothing)
cv2.createTrackbar("St","bin",64,255,nothing)


while True:
    frame = cv2.imread(files)
    print(frame.shape)


    Rt = cv2.getTrackbarPos("Rt","bin")
    St = cv2.getTrackbarPos("St","bin")

    blur = cv2.GaussianBlur(frame, (21, 21), 0)
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

    rows,cols,chls = frame.shape
    Bs,Gs,Rs = frame[:,:,0],frame[:,:,1],frame[:,:,2]
    Hs,Ss,Is = hsv[:,:,0],hsv[:,:,1],hsv[:,:,2]
    Bits = np.zeros((rows,cols))

    for i in range(rows):
        for j in range(cols):
            if(Rs[i,j]>Rt and Rs[i,j]>Gs[i,j] and Gs[i,j]>Bs[i,j] and (Ss[i,j]>((255-Rs[i,j])*St/Rt))):
                Bits[i,j] = 255
    Bits1 = cv2.morphologyEx(Bits,cv2.MORPH_OPEN,(50,50))
    cv2.imshow("main",frame)
    cv2.imshow("bin",Bits)
    cv2.imshow("bin1",Bits1)

    #cv2.imshow("frame", frame)
    #cv2.imshow("blur", blur)
    #cv2.imshow("output", output)
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()