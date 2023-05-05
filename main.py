from functions.get_youtube_video import get_youtube_video
from shorts_video import ShortsVideo

def get_seconds(time_string: str) -> int:
    result = 0
    if(':' in time_string):
        min_sec = time_string.split(':')
        min = min_sec[0]
        sec = min_sec[1]
        result = 60*int(min) + int(sec)
    else:
        result = int(time_string)
    return result

def main():
    url = input('enter url : ')
    start_time = get_seconds(input('enter start time : '))
    end_time = get_seconds(input('enter end time : '))
    
    video_title = input('enter video title : ')
    video = ShortsVideo(url, start_time, end_time, video_title)

    video.run()

main()