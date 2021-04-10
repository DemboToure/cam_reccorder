from logger.log import logger
from video_utils import video_utils 
from qt_utils import qt_utils as qt 
import pyautogui

if __name__ == '__main__' :
    logger.debug("Running...")
    #video_utils.read_cam_save(0)
    qt.app(pyautogui.size().width-50, pyautogui.size().height-100)
