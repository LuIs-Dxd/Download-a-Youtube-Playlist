import yt_dlp as youtube_dl

def descargar_playlist(url):
    opciones = {
        'format': 'bestaudio/best',
        'extractaudio': True,  
        'audioformat': "mp3",  
        'outtmpl': '%(title)s.%(ext)s', 
        'verbose': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }


    with youtube_dl.YoutubeDL(opciones) as ydl:
        ydl.download([url])

# Put the link here
url_playlist = "---Link Here---"
descargar_playlist(url_playlist)
