from pytubefix import YouTube
from moviepy import VideoFileClip

def download_youtube_video(url, output_path='video.mp4'):
    yt = YouTube(url)
    stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
    stream.download(filename=output_path)
    print(f'Downloaded video to {output_path}')
    return output_path

def clip_video(input_path, start_time, end_time, output_path='clip.mp4'):
    clip = VideoFileClip(input_path).subclipped(start_time, end_time)
    clip.write_videofile(output_path, codec='libx264')
    print(f'Created clip from {start_time} to {end_time} seconds as {output_path}')

if __name__ == "__main__":
    video_url = input("Enter YouTube video URL: ")
    video_path = download_youtube_video(video_url)
    start = float(input("Enter clip start time in seconds: "))
    end = float(input("Enter clip end time in seconds: "))
    clip_video(video_path, start, end)
