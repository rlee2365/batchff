import os
def replace_ext(file, ext='mp3'):
    return os.path.splitext(file)[0]+'.'+ext