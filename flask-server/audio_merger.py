from pydub import AudioSegment
import subprocess


def combine_with_timing(dubbed_script, total_video_duration, output_name):
    final_audio = AudioSegment.silent(duration=0)

    for segment in dubbed_script:
        start = int(segment["start"] * 1000)  # ms
        audio = AudioSegment.from_wav(segment["audio"])
        current_duration = len(final_audio)

        if start > current_duration:
            silence = AudioSegment.silent(duration=start - current_duration)
            final_audio += silence

        final_audio += audio

    # Pad to match total video duration (optional, for neatness)
    if len(final_audio) < total_video_duration * 1000:
        final_audio += AudioSegment.silent(duration=(total_video_duration * 1000 - len(final_audio)))

    final_audio.export((output_name.split("."))[0] + "_audio.wav", format="wav")


def strip_audio(input_video, output_video_no_audio):
    subprocess.run([
        "ffmpeg", "-y",
        "-i", input_video,
        "-c", "copy",
        "-an",  # remove audio
        output_video_no_audio
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def merge_audio_video(silent_video_path, new_audio_path, final_output_path):
    subprocess.run([
        "ffmpeg", "-y",
        "-i", silent_video_path,
        "-i", new_audio_path,
        "-c:v", "copy",
        "-c:a", "aac",
        "-strict", "experimental",
        final_output_path
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
