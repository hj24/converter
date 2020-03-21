import os
import re

import cv2
from PIL import Image

from cfg import output_path, newdir


def read_img_size(img):
    """
    根据输入视频解码后的图片的尺寸觉得输出视频的尺寸
    fix 原代码硬编码尺寸
    """
    _img = Image.open(img)
    return _img.size[0], _img.size[1]

def generate_video(path):
    # 重排文件列表
    filelist = os.listdir(path)
    filelist.sort(key=lambda x: int(re.findall(r'\d+', x)[0]))

    if len(filelist) == 0:
        raise

    size = read_img_size(path + '/' + filelist[0])

    # fps:
    # 帧率：1秒钟有n张图片写进去[控制一张图片停留5秒钟，那就是帧率为1，重复播放这张图片5次]
    # 如果文件夹下有50张 534*300的图片，这里设置1秒钟播放5张，那么这个视频的时长就是10秒
    fps = 24
    # 导出路径
    file_path = output_path

    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    video = cv2.VideoWriter(file_path, fourcc, fps, size)
    

    for item in filelist:
        if item.endswith('.jpg'):
            item = path + '/' + item
            # 使用opencv读取图像，直接返回numpy.ndarray 对象，通道顺序为BGR ，注意是BGR，通道值默认范围0-255
            img = cv2.imread(item)
            # 把图片写进视频
            video.write(img)

    video.release()


if __name__ == "__main__":
    generate_video(newdir)
