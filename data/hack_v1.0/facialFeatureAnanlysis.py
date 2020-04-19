import cv2
import dlib
import math

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor.dat")


def getImg(path):
    return (cv2.imread(path, 1))

def convertToGray(img):
    return(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))


def dispImg(img):
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def getLandmarks(gray, face):
    return(predictor(gray, face))

def markLandmarks(img, landmarks):

    for i in range(68):
        mark = landmarks.part(i)
        cv2.circle(img, (mark.x, mark.y), 15, (0,0,255), 2)
        cv2.putText(img, str(i), (mark.x, mark.y), cv2.FONT_HERSHEY_COMPLEX, 1, (0,225,225), 2)

def drawLines(img, landmarks, j, k):
    for i in range(j, k):
        priorPt = landmarks.part(i-1)
        currentPt = landmarks.part(i)
        cv2.line(img, (priorPt.x, priorPt.y), (currentPt.x, currentPt.y), (0,0,255), 3)

def drawNose(img, landmarks):
    drawLines(img, landmarks, 28, 36)
    endPt = landmarks.part(35)
    nodePt = landmarks.part(30)
    cv2.line(img, (endPt.x, endPt.y), (nodePt.x, nodePt.y), (0, 0, 255), 3)

def drawLips(img, landmarks):
    drawLines(img, landmarks, 49, 60)
    endPt = landmarks.part(59)
    nodePt = landmarks.part(48)
    cv2.line(img, (endPt.x, endPt.y), (nodePt.x, nodePt.y), (0, 0, 255), 3)

def getDist(pt1, pt2):
    x1 = pt1.x
    y1 = pt1.y
    x2 = pt2.x
    y2 = pt2.y

    return((math.sqrt((x2 - x1)**2 + (y2 - y1)**2)))

def onGetGoldenProportions(landmarks):
    B = getDist(landmarks.part(0), landmarks.part(16))
    C = getDist(landmarks.part(30), landmarks.part(8))
    Ew = getDist(landmarks.part(36), landmarks.part(45))
    Lw = getDist(landmarks.part(48), landmarks.part(54))
    return((float(B/C),float(Ew/Lw)))


def isOnlyOneFace(faces):
    if(len(faces)):
        return(True)
    return(False)

def drawRectsOnImg(img, faces):
    for face in faces:
        x1 = face.left()
        y1 = face.top()
        x2 = face.right()
        y2 = face.bottom()
        cv2.rectangle(img, (x1,y1), (x2,y2), (0,255,0), 3)
