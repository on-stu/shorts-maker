from moviepy.editor import *
from pytube import YouTube

class ShortsVideo():
    def __init__(self, url, start_time, end_time, video_title) -> None:
        self.url = url
        self.start_time = start_time
        self.end_time = end_time
        self.video_title = video_title

    def get_youtube_video(self):
        yt = YouTube(self.url)
        self.title = yt.title
        self.copyright_string = f'출처 - {yt.author}'
        mp4_files = yt.streams.filter(file_extension="mp4")
        mp4_720p_files = mp4_files.get_by_resolution("720p")
        mp4_720p_files.download("./videos", 'raw.mp4')
    
    def create_background(self):
        self.background = ColorClip((1080, 1920), (0,0,0), duration=self.end_time - self.start_time)

    def clip_video(self):
        self.video = VideoFileClip(f'./videos/raw.mp4').subclip(self.start_time, self.end_time)

    def make_video_title(self):
        self.title_text = TextClip(self.video_title,fontsize=70,color='white', font='GangwonEduPower-ExtraBold').set_duration(self.end_time - self.start_time)
    
    def resize_video(self):
        print(self.video.size)

    def make_copyright(self):
        self.copyright_text = TextClip(self.copyright_string,fontsize=50,color='white', font='GangwonEduPower-ExtraBold').set_duration(self.end_time - self.start_time)

    def compose_video(self):
        outputVideo = CompositeVideoClip([self.background, self.video.set_position(('center', 'center')), self.title_text.set_position(('center', 350)), self.copyright_text.set_position(('center', 1920 - 350))])
        outputVideo.write_videofile(f'{self.video_title}.mp4', codec='libx264', audio_codec="aac")
        self.video.close()
    
    def run(self):
        self.get_youtube_video()
        self.create_background()
        self.clip_video()
        self.make_video_title()
        self.make_copyright()
        self.resize_video()
        self.compose_video()
