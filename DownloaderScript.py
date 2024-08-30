import os
import sys
from yt_dlp import YoutubeDL

def download_playlist(url):

    ffmpeg_path = os.path.join(os.getcwd(), "bin", "ffmpeg.exe")
    ffprobe_path = os.path.join(os.getcwd(), "bin", "ffprobe.exe")
    output_dir = os.path.join(os.getcwd(), "Downloads")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    options = {
        'format': 'bestaudio/best',
        'extractaudio': True,
        'audioformat': "mp3", #<--- You can change the format, you can choose: AAC, M4A, Vorbis, FLAC, etc.
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
        'verbose': True,
        'ffmpeg_location': ffmpeg_path,  
        'ignoreerrors': True,# if you want that the script stop when an error occurred you can turn off this option (Deleted videos).
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3', #<--- You can change the codec too.
            'preferredquality': '192',
        }],
    }

    os.environ["FFMPEG_BINARY"] = ffmpeg_path
    os.environ["FFPROBE_BINARY"] = ffprobe_path

    with YoutubeDL(options) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("How to use: python DownloaderScript.py (playlist_url)")
        sys.exit(1)

    url_playlist = sys.argv[1]
    download_playlist(url_playlist)
