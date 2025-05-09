import sys, os, shutil
from transcriber import transcribe_vid
from translator import translate_text
from speaker import tts_converter, get_audio_duration
from fit import fit_audio
from audio_merger import combine_with_timing, strip_audio, merge_audio_video


#name of the video to be dubbed and its dubbed version
original_name = sys.argv[1]
dubbed_name = sys.argv[2]
language = sys.argv[3]

#convert it timestamped transcriptions, as long as the langauge spoken in the video is valid
try:
    script = transcribe_vid(original_name)
except RuntimeError as e:
    print(f"Error: {e}")
    sys.exit(1)  # Exit the program with error code

dubbed_script = []

#for each line in the script, 
total_duration = 0
for line in script['segments']:
    #info from the original that we want to match
    start = line['start']
    end = line['end']
    duration = end - start
    total_duration += duration

    #whether or not a successful translation has been found 
    success = False

    #thins to give my translate function to help it give the best result
    current_translation = ""
    short = False
    long = False

    for i in range(5):
        #changes it if the translation was already done at least once
        translated_text = translate_text(line['text'], current_translation, short, long, language) #generate a new translation every run
        print(f"translation = {translated_text}")
        current_translation = translated_text
        short  = False
        long = False
        dubbed_audio_path = tts_converter(translated_text, language, original_name)
        new_duration = get_audio_duration(dubbed_audio_path) 

        #if the new tts is within 0.2* the original duration, it's good enough
        if ((duration - new_duration) > 0.2*duration):
            short = True 
        elif ((new_duration - duration) > 0.2*duration):
            long = True
        else:
            success = True
            break
    #if a satisfactory translation wasn't found after 5 tries, strech or compress speed
    if(success == False):
        fit_audio(dubbed_audio_path, duration)
    

    #add to the list
    dubbed_script.append({
        "start": start,
        "end": start + get_audio_duration(dubbed_audio_path),
        "text": translated_text,
        "audio": dubbed_audio_path
    })


#ONCE THE WHOLE VIDEO HAS BEEN PROCESSED:
#stitch together the new audio:
combine_with_timing(dubbed_script,total_duration,dubbed_name)

#remove current audio
strip_audio(original_name, (dubbed_name.split("."))[0] + "_noaudio.mp4")

#add tts of the whole list at each start duration 
merge_audio_video((dubbed_name.split("."))[0] + "_noaudio.mp4", (dubbed_name.split("."))[0] + "_audio.wav", dubbed_name)

#get rid of the snippets directory so that videos of the same name are still accurate when processed one after another'
name_only = os.path.splitext(os.path.basename(original_name))[0]
snippet_dir = f"{name_only}_snippets"

if os.path.exists(snippet_dir):
    shutil.rmtree(snippet_dir)  # This completely deletes the folder and its contents
    print(f"Deleted temporary directory: {snippet_dir}")
else:
    print(f"No temporary directory found: {snippet_dir}")

    
