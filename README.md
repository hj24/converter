## 视频转换器
创意来自热搜：武大学生用程序模拟樱花绽放

## 用法
- 安装依赖
```shell script
cd /path/to/converter
pip install -r requirements.txt
```

- 替换自己的输入视频

把下面这个目录下的视频换成自己想用的
```shell script
/path/to/converter/video/input.mp4
```
在`cfg.py`里把`input_filename`修改成视频名

- 在`cfg.py`中修改其它配置
```python
# 替换视频中的像素点所用的字符
placeholder = 'love'

# 字体，不同系统使用的字体可能不同
# 想换用其他字体，在mac下的 /Library/Fonts 中查看并修改配置
phfont = 'Arial.ttf'

# 字体大小
phfontsize = 15
```



- 运行
```shell script
python app.py
```

或直接运行`app.py`的`run()`方法


