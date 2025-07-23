import yt_dlp
url="https://youtu.be/dydevesm6Vk?feature=shared"
ydl_opts={}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])