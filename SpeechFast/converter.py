import subprocess
import shlex
import os


class MediaConverter:
    @staticmethod
    def _execute_ffmpeg_command(cmd: str):
        cmd = f'ffmpeg {cmd}'
        try:
            subprocess.call(shlex.split(cmd), stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        except FileNotFoundError:
            raise Exception('Please, install ffmpeg first!')

    @staticmethod
    def from_any_to_wav(input_file: str, output_file: str):
        MediaConverter._execute_ffmpeg_command(f'-i "{input_file}" -acodec pcm_s16le -ac 1 -ar 16000 "{output_file}"')

    @staticmethod
    def extract_audio(input_file: str, output_file: str):
        MediaConverter._execute_ffmpeg_command(f'-i "{input_file}" -map 0:a "{output_file}"')