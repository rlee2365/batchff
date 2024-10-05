from batchff.utils import replace_ext
import ffmpeg

def process_mp3(file):
    of = replace_ext(file, 'mp3')
    stream = ffmpeg.input(file).output(
        of, audio_bitrate='512k')
    ffmpeg.run(stream, overwrite_output=True)