import cv2

count = 0
face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
video_capture = cv2.VideoCapture(0)

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("Trainer.yml")

name_list = ["", "Hassan"]

def detect_bounding_box(vid, count):
    gray_image = cv2.cvtColor(vid, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray_image, 1.1, 5, minSize=(40, 40))
    for (x, y, w, h) in faces:
        serial, conf = recognizer.predict(gray_image[y:y+h, x:x+w])
        if conf < 50:
            name = name_list[serial] if serial < len(name_list) else name_list[1]
            cv2.putText(vid, name, (x, y-40), cv2.FONT_HERSHEY_SIMPLEX, 1, (150, 50, 150), 2)
            cv2.rectangle(vid, (x, y), (x + w, y + h), (150, 0, 150), 4)
        else:
            cv2.putText(vid, "Bilal", (x, y-40), cv2.FONT_HERSHEY_SIMPLEX, 1, (50, 50, 255), 2)
            cv2.rectangle(vid, (x, y), (x + w, y + h), (150, 0, 150), 4)
    return faces

while True:
    result, video_frame = video_capture.read()  # read frames from the video
    if not result:
        break  # terminate the loop if the frame is not read successfully

    faces = detect_bounding_box(video_frame, count)
    count += 1  # apply the function we created to the video frame

    cv2.imshow("facial recog algo", video_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video_capture.release()
cv2.destroyAllWindows()

