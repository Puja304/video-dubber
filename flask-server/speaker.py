from TTS.api import TTS
import wave
import contextlib
import uuid
import os

tts = TTS(model_name = "tts_models/multilingual/multi-dataset/your_tts", progress_bar=False, gpu=False)

def tts_converter(text, language, original_name):
    name_only = os.path.splitext(os.path.basename(original_name))[0]
    snippet_dir = f"{name_only}_snippets"
    os.makedirs(snippet_dir, exist_ok=True)  # <- This creates the folder if it doesn't exist
    output_path = f"{snippet_dir}/{uuid.uuid4()}.wav"
    if(language == "French"):
        tts.tts_to_file(text=text, file_path=output_path, language="fr-fr", speaker=tts.speakers[0] )   
        return output_path
    elif(language == "English"):
        tts.tts_to_file(text=text, file_path=output_path, language="en", speaker=tts.speakers[0] )   
        return output_path
    elif(language == "Portugese"):
        tts.tts_to_file(text=text, file_path=output_path, language="pt-br", speaker=tts.speakers[0] )   
        return output_path

def get_audio_duration(audio_path):
    with contextlib.closing(wave.open(audio_path, 'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
    return duration

