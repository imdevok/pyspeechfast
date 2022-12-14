import subprocess


class MediaConverter:
    @staticmethod
    def execute_ffmpeg_command(cmd: str):
        ffmpeg_path = r"C:\\ffmpeg\\bin\\ffmpeg.exe"
        cmd = f"{ffmpeg_path} {cmd}"
        subprocess.Popen([cmd])
    
    @staticmethod
    def from_any_to_wav(input_file: str, output_file: str):
        MediaConverter.execute_ffmpeg_command(f"-i {input_file} -acodec pcm_s16le -ac 1 -ar 16000 {output_file}")

    @staticmethod
    def from_mp4_to_wav(input_file: str, output_file: str):
        MediaConverter.execute_ffmpeg_command(f"-i {input_file} -vn -acodec copy {output_file}")


