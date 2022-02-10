# pip install opencv-python

# 1) import cv2
import cv2

# 2) Select the camera by using indexing:
video = cv2.VideoCapture(1)
# 3) This is a shortcut to the data folder detecting frontal face:
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
while True:
    success, img = video.read()
    # looking for different sized faces
    faces = face_cascade.detectMultiScale(img, 1.3, 4)
    for (x,y,w,h) in faces:
        # making the face blurry
        ROI = img[y:y+h, x:x+w]

        # how blurry
        blur = cv2.GaussianBlur(ROI, (99, 99), 0)
        # putting the blurry box back into the original image
        img[y:y+h, x:x+w] = blur

    # show the video to the user
    cv2.imshow("Face Blur", img)
    # check to see if the user hit's the q for quit
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

video.release()
cv2.destroyAllWindows()