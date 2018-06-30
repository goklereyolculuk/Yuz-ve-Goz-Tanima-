"""
ÖNEMLİ NOT: Çalıştırdıktan sonra programı kapatmak için "Q" tuşuna basın.
"""

import cv2

# Cascade yükleme
yuz = cv2.CascadeClassifier('haarcascade-frontalface-default.xml')
goz = cv2.CascadeClassifier('haarcascade-eye.xml')

# Tanıma yapacak fonksiyon
def detect(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    yuzler = yuz.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in yuzler: # x ve y  koordinat değeri olurken w ve h ise genişlikk ve yükseklik
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        gozler = goz.detectMultiScale(roi_gray, 1.1, 3)
        for (ex, ey, ew, eh) in gozler:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
    return frame


# Webcam ile tanıma yapılıyor.
# Eğer bilgisayarınızda birden fazla kamera bağlıysa 0'ı 1 yapabilirsiniz.
video_capture = cv2.VideoCapture(0)
while True:
    _, frame = video_capture.read()
    canvas = detect(frame)
    cv2.imshow('Video', canvas)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()