import cv2

cap = cv2.VideoCapture(2)

while True:
    houve_capt, frame = cap.read()
    
    if not houve_capt:
        break
        
    cv2.imshow("Video", frame)
    if(cv2.waitKey(33) != -1):
        break
