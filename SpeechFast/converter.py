import asyncio


class MediaConverter:
    @staticmethod
    async def execute_ffmpeg_command(cmd: str):
        cmd = f"ffmpeg -nostdin -loglevel quiet {cmd}"

        return await asyncio.create_subprocess_exec(cmd)
            

    @staticmethod
    async def from_any_to_wav(input_file: str, output_file: str):
        return await MediaConverter.execute_ffmpeg_command(f"-i {input_file} -acodec pcm_s16le -ac 1 -ar 16000 {output_file}")

    @staticmethod
    async def from_mp4_to_wav(input_file: str, output_file: str):
        return await MediaConverter.execute_ffmpeg_command(f"-i {input_file} -vn -acodec copy {output_file}")


