from logger.log import logger
import numpy as np
import cv2
from utils.utils import get_datetime_str


def create_screen(name_windows, height, width):
    cv2.namedWindow(name_windows, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(name_windows, height, width)

def read_image(path, mode=cv2.IMREAD_COLOR):
    return cv2.imread(path, mode)

def display_image(screen, image):
    cv2.imshow(screen, image)

def handle_image(path):
    screen_1 = 'screen_1'
    create_screen(screen_1, 840, 680)
    img = read_image(path)
    display_image( screen_1 , img)
    cv2.waitKey(0)
    cv2.destroyWindow(screen_1)

def read_cam(index):
    cap = cv2.VideoCapture(index)

    while(True):
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', gray)
        if cv2.waitKey(1) &  0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

def read_video(path):
    cap = cv2.VideoCapture(path)
    
    while(cap.isOpened()):
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

def read_cam_save(index):
    cap = cv2.VideoCapture(index)
    logger.debug('start capture for CAM => {}'.format(index) )
    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    output_path = 'output/'+get_datetime_str()+'.avi'
    out = cv2.VideoWriter(output_path,fourcc, 20.0, (640,480))
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret==True:
            out.write(frame)
            cv2.imshow('frame',frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    # Release everything if job is finished
    cap.release()
    out.release()
    cv2.destroyAllWindows()
