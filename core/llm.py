from utils.logger import Logger

from pathlib import Path
from datetime import datetime, timedelta
import os

import whisper #openai model for audio transcription


class LLM:
    """
    To convert a video into text (srt format) using audio transcription.
    """

    def __init__(self, model_size: str = "small"):
        self._model_size: str = model_size # from documentation [tiny, base, small, medium, large and turbo], currently using small by default for only 2gb vram
        self._logger = Logger(__name__)
        self._model = whisper.load_model(self._model_size)

    def _generate_segments(self, path_to_audio: str) -> list[dict]:
        # Simulate response generation
        try: 
            transcription = self._model.transcribe(path_to_audio) # i know the variables are quite verbose, it helps me with readability
            self._logger.info(f"Transcription completed for {path_to_audio}.")
            self._logger.info(f"{transcription['segments']}")
            return transcription['segments']
        except Exception as e:
            self._logger.error(f"Error generating segments: {e}")
            return []

    def generate(self, path_to_audio: str) -> str:
        segments: list[dict] = self._generate_segments(path_to_audio)

        for segment in segments:
            # process each segment into words
            text = segment['text'].strip() 
            words = text.split() 
            word_count = len(words)

            #grab the start and end time
            start_time = float(segment['start'])
            end_time = float(segment['end'])

            duration_per_word = (end_time - start_time) / word_count

            for i, word in enumerate(words):
                word_start_time = start_time + i * duration_per_word
                word_end_time = word_start_time + duration_per_word

                # datetime(1, 1, 1) = jan first 00:00:00 then adding the time delta for each word on top of the time 
                start_time_formatted = (datetime(1, 1, 1) + timedelta(seconds=word_start_time)).strftime("%H:%M:%S,%f")[:-3]
                end_time_formatted = (datetime(1, 1, 1) + timedelta(seconds=word_end_time)).strftime("%H:%M:%S,%f")[:-3]

                segment_content = f"{i+1}\n{start_time_formatted} --> {end_time_formatted}\n{word}\n\n"

                txt_filename = path_to_audio.with_suffix('.txt')
                # Append each word to the TXT file
                with open(txt_filename, 'a', encoding='utf-8') as txt_file:
                    txt_file.write(segment_content)

                os.remove(path_to_audio)
                return os.path.join(txt_filename.parent, txt_filename.name)



Documentation = """
Internally, the transcribe() method reads the entire file and processes the audio with a sliding 30-second window, performing autoregressive sequence-to-sequence predictions on each window.
"""