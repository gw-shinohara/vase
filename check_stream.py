import cv2
from datetime import datetime 
import os

host        = "172.30.0.2"
port        = 8554

os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = "rtsp_transport;udp"
cap = cv2.VideoCapture(f"rtsp://{host}:{port}/cam", cv2.CAP_FFMPEG)
cap.set(cv2.CAP_PROP_BUFFERSIZE, 3)  # Attempt to set a small buffer size
 
while True:
    try:
        ret, frame = cap.read()
        if ret == True:
            # Please modify the value to fit your PC screen size.
            frame2 = cv2.resize(frame, (1280, 720))
            now = datetime.now()
            now_str = now.strftime('%Y%m%d%H%M%S')
            # Display video.
            cv2.imshow("image", frame2)
            now = datetime.now()
            now_str = now.strftime(r'%Y%m%d%H%M%S%f')
            now_title = now.strftime(r'%Y/%m/%d %H:%M:%S.%f')
            cv2.setWindowTitle('image', now_title)
            if cv2.waitKey(1) == ord('q'):
                break
    except KeyboardInterrupt:
        # Press '[ctrl] + [c]' on the console to exit the program.
        print("KeyboardInterrupt")
        break
 
cap.release()
cv2.destroyAllWindows()