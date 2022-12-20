import cv2

cap = cv2.VideoCapture("imgs/video_ps.mp4")

while True:
    houve_capt, frame = cap.read()
    
    if not houve_capt:
        break

    cv2.imshow("Video", frame)
    cv2.waitKey(33) #video a 30 fps 1s/30fps = 0,03

