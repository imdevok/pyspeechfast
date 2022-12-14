import wave

from vosk import Model, KaldiRecognizer, SetLogLevel


class Recognizer:
    """AudioTranscriber - class for transcribing audio to text
    Args: 
        audio_file (str): audio file to transcribe
        model_name (str): language model from vosk https://alphacephei.com/vosk/models 
        sample_rate (int): sample rate in audio file
    """
    def __init__(self, *, 
        audio_file: str, 
        model_name: str, 
        sample_rate: int=16000) -> None:

        self.audio_file = audio_file
        self.model = Model(model_name)
        self._recognizer = KaldiRecognizer(self.model, sample_rate)

    def set_loglevel(self, loglevel: int):
        """Sets Vosk log level

        Args:
            loglevel (int): -1 - off, 0 - on
        """
        SetLogLevel(loglevel)

    def set_words(self, new_value: bool):
        self._recognizer.SetWords(new_value)

    def set_partials_words(self, new_value: bool):
        self._recognizer.SetPartialWords(new_value)

    def set_default(self):
        """Sets default settings
        """
        self.set_loglevel(0)
        self.set_words(True)
        self.set_partials_words(True)

    def recognize(self) -> str:
        """Transcribes audio to text

        Returns:
            text (str): transcribed text
        """
        wf = wave.open(self.audio_file, "rb")

        while True:
            data = wf.readframes(4000)
            if len(data) == 0:
                break
            if self._recognizer.AcceptWaveform(data):
                self._recognizer.Result()
            else:
                self._recognizer.PartialResult()

        return self._recognizer.FinalResult()
