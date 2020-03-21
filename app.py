import os

from parser import parser
from redraw import transfer
from generator import generate_video
from cfg import newdir, videodir, parsedir, output_path


basedir = os.path.dirname(__file__)

def _remove_files_under_dir(dir):
    for file in os.listdir(dir):
        os.remove(dir + '/' + file)

def _preprocess():
    if os.path.exists(newdir):
        print('{} 已存在，删除旧文件中...'.format(newdir))
        _remove_files_under_dir(newdir)
        print('{} 清理完毕'.format(newdir))
    else:
        print('创建 {} 中...'.format(newdir))
        os.mkdir(newdir)
        print('创建 {} 完毕'.format(newdir))
    if os.path.exists(parsedir):
        print('{} 已存在，删除旧文件中...'.format(parsedir))
        _remove_files_under_dir(parsedir)
        print('{} 清理完毕'.format(parsedir))
    else:
        print('创建 {} 中...'.format(parsedir))
        os.mkdir(parsedir)
        print('创建 {} 完毕'.format(parsedir))
    if os.path.exists(output_path):
        print('删除旧输出视频中...')
        os.remove(output_path)
        print('删除完毕')

def run():
    try:
        _preprocess()
        # video在运行程序之前是必须存在的，用户需要提供初始video
        # 可以在cfg.py里配置，没有配置的话，需要抛出异常
        if not os.path.exists(videodir):
            raise Exception('video path not exists')
        # 开始主程序
        print('开始解码原始视频...')
        parser()
        print('解码完毕，开始转码...')
        transfer()
        print('转码完毕，开始生成新视频...')
        generate_video(newdir)
    except Exception as e:
        print('失败: \n{}'.format(e))
    else:
        print('视频转换成功')

if __name__ == "__main__":
    run()
