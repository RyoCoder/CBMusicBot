from os import path

from youtube_dl import YoutubeDL

from config import DURATION_LIMIT
from helpers.errors import DurationLimitError

ydl_opts = {
    "format": "bestaudio[ext=m4a]",
    "format": "bestaudio/best",
    "geo-bypass": True,
    "nocheckcertificate": True,
    "outtmpl": "downloads/%(id)s.%(ext)s",
}
ydl = YoutubeDL(ydl_opts)
def download(url: str) -> str:
    info = ydl.extract_info(url, False)
    duration = round(info["duration"] / 120)
    if duration > DURATION_LIMIT:
        raise DurationLimitError(
            f"🛑 Video dài hơn {DURATION_LIMIT} phút không được phép, video được cung cấp là {duration} phút"
        )
    try:
        ydl.download([url])
    except:
        raise DurationLimitError(
            f"🛑 Video dài hơn {DURATION_LIMIT} phút không được phép, video được cung cấp là {duration} phút"
        )
    return path.join("downloads", f"{info['id']}.{info['ext']}")
