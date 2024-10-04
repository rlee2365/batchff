import sys
import argparse
import batchff.tasks as tasks
import os
import platform
import glob

TASK_MAPPING = {
    'mp3': tasks.process_mp3
}

def main():
    parser = argparse.ArgumentParser(prog='batchff',
        description='ffmpeg shorthand utility')
    parser.add_argument('files', nargs='+', help='List of files to process')
    parser.add_argument('-t', '--task', help='Output task', default='mp3')

    args = parser.parse_args()

    if platform.system() == "Windows":
        files = []
        for gl in args.files:
            files.extend(glob.glob(gl))
    else:
        files = args.files

    for f in files:
        TASK_MAPPING[args.task](f)