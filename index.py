import yt_dlp
import os
from datetime import datetime

def download_audio_from_youtube(youtube_url):
    today = datetime.now()
    folder_path = today.strftime("%Y/%m/%d")
    os.makedirs(folder_path, exist_ok=True)
    with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
        info = ydl.extract_info(youtube_url, download=False)
        video_title = info.get('title', 'audio')

    output_path = os.path.join(folder_path, f"{video_title}.mp3")

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': output_path,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])

    print(f"音声が '{output_path}' に保存されました")

youtube_url = "ここにURLを指定"
download_audio_from_youtube(youtube_url)
