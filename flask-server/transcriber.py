import whisper

def transcribe_vid(original_name):
    model = whisper.load_model("small")
    #trying to transcribe and if not possible, sending an error
    try:
        result = model.transcribe(original_name)
        if "language" not in result or not result["language"]:
            raise ValueError("Language could not be detected.")
        return result
    except Exception as e:
        raise RuntimeError(f"Transcription failed: {e}")
