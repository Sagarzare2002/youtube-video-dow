import yt_dlp
url="https://url"
ydl_opts={}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])