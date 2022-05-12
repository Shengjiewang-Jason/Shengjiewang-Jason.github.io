import moviepy.editor as mpy

# 视频文件的本地路径
content = mpy.VideoFileClip("./iros.mp4")
# 剪辑0分0秒到0分4秒的片段。resize为修改清晰度
c1 = content.subclip((0,0), (0, 5)).resize((600, 337))
# 将片段保存为gif图到python的默认路径
c1.write_gif("./iros.gif",fps=5)

