# SpeechFast  API Documentation

## SpeechFast.transcriber.AudioTranscriber()

AudioTranscriber instance create an instance of Vosk recognizer class and give highlevel simple and easy interface.

```python
from SpeechFast.transcriber import AudioTranscriber

audio_transcriber = AudioTranscriber(audio_file="path/to/your/audio_file.wav", model_name="vosk-model-name")
```

## AudioTranscriber(...).transcribe_to_text()

Returns recognized from audio file text

```python
from SpeechFast.transcriber import AudioTranscriber

audio_transcriber = AudioTranscriber(audio_file="path/to/your/audio_file.wav", model_name="vosk-model-name")
transcribed_text = audio_transcriber.transcribe_to_text()

print(transcribed_text
```

## SpeechFast.punctuator make_punctuation_in_text()

Makes punctuation in input text

```
Args:
 text (str): input text without punctuation
 lang (Lang): input text language
Returns:
 str: object with 'text' field
```

## SpeechFast.converter.audio convert_to_wav()

Converts audio file (mp3, ogg) to wav and to PCM format

```
Args:
 audio_file_path (Path): path to mp3 or ogg audio file

```

## SpeechFast.converter.video convert_to_mp3()

Cuts the audio track from mp4 video file

```
Args:
    mp4_video_file (str): path to mp4 video
    mp3_output_file (str): path to mp3 output audio
```

## SpeechFast.types Lang

Type hint for `SpeechFast.punctuator` module
