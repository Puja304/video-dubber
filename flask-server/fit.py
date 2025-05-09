from speaker import get_audio_duration
import subprocess

#alter the speed of audio to match the target duration
def fit_audio(audio_path, duration):
    current_duration = get_audio_duration(audio_path)
    speed_change = duration/current_duration
    #since we can only go as low as 0.5 and as high as 2, modify if required
    speed_change = max(0.5, min(2.0, speed_change))


    #change speed and replace it with the same name
    subprocess.run([
        "ffmpeg", "-y",
        "-i", audio_path,
        "-filter:a", f"atempo={speed_change}",
        audio_path
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)



