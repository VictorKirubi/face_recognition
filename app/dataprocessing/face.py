import cv2

class Face:

    @staticmethod
    def isFace(imagePath):
        frontal_face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        img = cv2.imread(imagePath)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = frontal_face_cascade.detectMultiScale(gray, 1.1, 5)
        #print("faces: " + str(len(faces)))
        #print(faces)
        return str(len(faces))
