import cv2
import time
import math

video = cv2.VideoCapture("footvolleyball.mp4")

tracker = cv2.TrackerCSRT_create()

check, img = video.read()

p1 = int(530)
p2 = int(300)

list1 = []
list2 = []

bbox = cv2.selectROI("track the ball", img, False)
tracker.init(img, bbox)
print(bbox)

def drawbox(img, bbox):
    x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    cv2.putText(img,  "Tracking ", (100, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1)

def goalTrack(img, bbox):
    x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
    c1 = x+int(w/2)
    c2 = y+int(h/2)
    cv2.circle(img, (c1, c2), 2, (255, 0, 0), 5)
    cv2.circle(img, (p1, p2), 2, (255, 0, 0), 5)
    dist = math.sqrt(((c1-p1)**2)+(c2-p2)**2)

    print(dist)
    if dist <= 20:
        cv2.putText(img,  "Its a GOALLLL!!!!!!!", (200, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 1)

    list1.append(c1)
    list2.append(c2)

    for i in range(len(list1)-1):
        cv2.circle(img, (list1[i], list2[i]), 2, (255, 0, 0), 5) 

while True:
    check, img = video.read()   

    suces, bbox = tracker.update(img)

    if suces:
        drawbox(img, bbox)

    else:
        cv2.putText(img, "Lost", (100, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1)


    goalTrack(img, bbox)
    cv2.imshow("result",img)
            
    key = cv2.waitKey(25)

    if key == 32:
        print("Stopped!")
        break

video.release()
cv2.destroyALLwindows()