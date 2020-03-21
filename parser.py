import os

import cv2

from cfg import input_path, parsedir


def parser():
    if not os.path.exists(parsedir):
        os.mkdir(parsedir)

    vidcap = cv2.VideoCapture(input_path)
    success, image = vidcap.read()
    if success:
        cnt = 0
        while success:
            success, image = vidcap.read()
            cv2.imwrite("{0}/frame{1}.jpg".format(parsedir, cnt), image)
            # 按键终止事件
            if cv2.waitKey(10) == 27:
                break
            cnt += 1
    else:
        print("读取视频文件失败，请检查配置")

if __name__ == "__main__":
    parser()