from moviepy.editor import *

def clip_video(video_path:str ,start_time: int, end_time: int):
    clip = VideoFileClip(video_path).subclip(start_time, end_time)
    return clip
