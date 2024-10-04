from batchff.utils import replace_ext
import ffmpeg

def process_mp3(file):
    of = replace_ext(file, 'mp3')
    stream = ffmpeg.input(file).output(
        of, **{'-b:a': '512k'})
    ffmpeg.run(stream, overwrite_output=True)