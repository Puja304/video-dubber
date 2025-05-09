import sys
from audio_merger import combine_with_timing, strip_audio, merge_audio_video

original_name = sys.argv[1]
dubbed_name = sys.argv[2]

#remove current audio
strip_audio(original_name, (dubbed_name.split("."))[0] + "_noaudio.mp4")

#add tts of the whole list at each start duration 
merge_audio_video((dubbed_name.split("."))[0] + "_noaudio.mp4", (dubbed_name.split("."))[0] + "_audio.wav", dubbed_name)

