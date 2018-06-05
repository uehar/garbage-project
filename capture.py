mport cv2
from time import sleep

def capturecamera(mirror=True, size=None):
    """Capture video from camera"""
    sleep(1)    

    cap = cv2.VideoCapture(0) 


    ret, frame = cap.read()


    if mirror is True:
        frame = frame[:,::-1]



    if size is not None and len(size) == 2:
        frame = cv2.resize(frame, size)


    cv2.imwrite('gomi.jpg', frame)

    cv2.waitKey(0)
    cv2.destroyAllWindows()     


if __name__ =='__main__':
        capturecamera()


