#Face class with isFace method to count number of faces in image
#Counts number of faces

#computer vision library. Recognizes a face from camera feed
import cv2

class Face:

    @staticmethod
    #Checks how many faces can be recognized
    def isFace(imagePath):
        #Data used to train cv2 to recognize faces
        frontal_face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        #cv2 used to read image path
        img = cv2.imread(imagePath)
        #convert color fomat into a readable format for the AI
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        #Detect how many faces are in the image
        faces = frontal_face_cascade.detectMultiScale(gray, 1.1, 5)
        #print("faces: " + str(len(faces)))
        #print(faces)
        #return number of faces
        return str(len(faces))
