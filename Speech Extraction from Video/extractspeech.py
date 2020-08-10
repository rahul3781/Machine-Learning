import speech_recognition as sr
import moviepy.editor as mp

#loading the video clip that is to be used
video = mp.VideoFileClip(r"4.mp4")
#i have used .wav format but we can make the audio file in any audio supported format
#converting the video to audio
video.audio.write_audiofile(r"converted.wav")

#defining recogniser
rec = sr.Recognizer()

aud = sr.AudioFile("converted.wav")


#this open the file and read its content and stores it in a audio file called 'source'
#record() method then records the data from that file into an AudioData instance.
#we can also pass a parameter duration in record method if we want to capture a portion of speech.
with aud as source:
    #to remove noise in the audio
    #rec.adjust_for_ambient_noise(source, duration=0.25)
    audio_file = rec.record(source)

#use type(audio_file) to check
#recognising the speech in audio file
result = rec.recognize_google(audio_file)

#the result
with open('recognised.txt', mode='w') as file:
    file.write("Recognised Speech:")
    file.write("\n")
    file.write(result)
    print("ready!")

