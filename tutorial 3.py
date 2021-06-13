import numpy as np
import cv2


#cap = cv2.VideoCapture(0)

url = 'http://172.20.10.3:4747/video?640x480'

while True:
    
    img_resp = requests.get(url)
    img_arr = np.array(bytrarray(img_resp.content), dtype=np.uint8)
    img  = cv2.imdecode(img_arr, -1)
    #ret, frame = url.read()
    #width = int(url.get(3))
    #height = int(url.get(4))

    image = np.zeros(frame.shape, np.uint8)
    smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    image[:height//2, :width//2] = cv2.rotate(smaller_frame, cv2.cv2.ROTATE_180)
    image[height//2:, :width//2] = smaller_frame
    image[:height//2, width//2:] = cv2.rotate(smaller_frame, cv2.cv2.ROTATE_180)
    image[height//2:, width//2:] = smaller_frame

    cv2.imshow('DroidCam', image)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
