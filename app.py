import os

from parser import parser
from redraw import transfer
from generator import generate_video
from cfg import newdir, videodir, parsedir, output_path


basedir = os.path.dirname(__file__)

def _remove_files_under_dir(dir):
    for file in os.listdir(dir):
        os.remove(dir + '/' + file)

_remove_files_under_dir(newdir)

def _preprocess():
    print('adkljhvfb')
    os.chmod(basedir, 777)
    print('aidhkjgfs')
    if os.path.exists(newdir):
        _remove_files_under_dir(newdir)
    if os.path.exists(parsedir):
        _remove_files_under_dir(parsedir)
    if os.path.exists(output_path):
        os.remove(output_path)

def run():
    try:
        _preprocess()
        print('padojihusgyfihueijdawok;aljefhg')
        # video在运行程序之前是必须存在的，用户需要提供初始video
        # 可以在cfg.py里配置，没有配置的话，需要抛出异常
        if not os.path.exists(videodir):
            raise
        print(';[dlpksljfhbbklda')
        # 开始主程序
        print('开始解码原始视频...')
        parser()
        print('解码完毕，开始转码...')
        transfer()
        print('转码完毕，开始生产新视频...')
        generate_video(newdir)
    except Exception as e:
        print('失败: \n{}'.format(e))
    else:
        print('视频转换成功')

if __name__ == "__main__":
    run()
