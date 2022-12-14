import asyncio
from subprocess import PIPE, STDOUT

class MediaConverter:
    @staticmethod
    async def execute_ffmpeg_command(cmd: str):
        cmd = f"ffmpeg -nostdin -loglevel quiet {cmd}"
        process = await asyncio.create_subprocess_shell(cmd, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
        await process.wait()


    @staticmethod
    async def from_any_to_wav(input_file: str, output_file: str):
        await MediaConverter.execute_ffmpeg_command(f"-i {input_file} -acodec pcm_s16le -ac 1 -ar 16000 {output_file}")

    @staticmethod
    async def extract_audio(input_file: str, output_file: str):
        await MediaConverter.execute_ffmpeg_command(f"-i {input_file} -map 0:a {output_file}")