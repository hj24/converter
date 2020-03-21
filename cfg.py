"""
配置文件
"""
import os

# 原始视频名称，放在 ./video目录下
input_filename = 'input.mp4'

# 转码后的占位字符
placeholder = 'love'
phfont = 'Arial.ttf'
phfontsize = 9

## 以下部分请不要修改
basedir = os.path.dirname(__file__)
videodir = os.path.join(basedir, 'video')
parsedir = os.path.join(basedir, 'middle')
newdir = os.path.join(basedir, 'new')

output_filename = 'output.avi'
input_path = os.path.join(videodir, input_filename)
output_path = os.path.join(videodir, output_filename)

