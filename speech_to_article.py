# importing libraries
import sys 
import speech_recognition as sr 
import os 
from pydub import AudioSegment
from pydub.silence import split_on_silence

# create a speech recognition object
r = sr.Recognizer()

# a function that splits the audio file into chunks
# and applies speech recognition
def get_large_audio_transcription(path):
    """
    Splitting the large audio file into chunks
    and apply speech recognition on each of these chunks
    """
    # open the audio file using pydub
    sound = AudioSegment.from_wav(path)

    # split audio sound where silence is 700 miliseconds or more and get chunks
    chunks = split_on_silence(sound,
        min_silence_len = 500,
        silence_thresh = sound.dBFS-16,
        keep_silence=400,
    )

    folder_name = "audio-chunks"
    # create a directory to store the audio chunks
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
    whole_text = ""
    # process each chunk 
    for i, audio_chunk in enumerate(chunks, start=1):
       
        # Create 0.5 seconds silence chunk
        chunk_silent = AudioSegment.silent(duration = 10)
        
        # add 0.5 sec silence to beginning and 
        # end of audio chunk. This is done so that
        # it doesn't seem abruptly sliced.
        audio_chunk = chunk_silent + audio_chunk + chunk_silent
        
        # export audio chunk and save it in
        # the `folder_name` directory.
        chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
        audio_chunk.export(chunk_filename ,format="wav")
        
        # recognize the chunk
        with sr.AudioFile(chunk_filename) as source:
          r.adjust_for_ambient_noise(source, duration=0.1)
          audio_listened = r.record(source)
          
          # try converting it to text
          try:
              text = r.recognize_google(audio_listened)
          except sr.UnknownValueError as e:
              print("Error:", str(e))
          else:
              text = f"{text.capitalize()}. "
            #   print(chunk_filename, ":", text)
              whole_text += text + '\n'
    # return the text for all chunks detected
    return whole_text

# path = "/home/hiren/Desktop/speech_audios/Welcome.wav"

path = sys.argv[1]
final_text = get_large_audio_transcription(path)

with open("transcription.txt", "w") as fout:
    fout.write(final_text)

