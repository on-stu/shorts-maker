def get_youtube_video(url: str):
    from pytube import YouTube
    yt = YouTube(url)
    mp4_files = yt.streams.filter(file_extension="mp4")
    mp4_720p_files = mp4_files.get_by_resolution("720p")
    mp4_720p_files.download("./videos")
