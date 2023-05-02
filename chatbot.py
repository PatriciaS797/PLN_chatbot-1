# Librerías necesarias

# # for speech to text
# pip install SpeechRecognition  #(3.8.1)
# # for text to speech
# pip install gTTS  #(2.2.3)
# # for language model
# pip install transformers  #(4.11.3)
# pip install tensorflow #(2.6.0, or pytorch)


# PyAudio necesario para el micro de speech recognition
# pip install PyAudio
# da error de ficheros en parrotOS ejecutar antes
# sudo apt-get install libportaudio2 portaudio19-dev
# para reproducir sonidos en parrot
# sudo apt-get install alsa-utils
# sudo apt-get install mpg123
import numpy as np
import transformers

import speech_recognition as sr

from gtts import gTTS
import os
import datetime
import winsound

from transformers import pipeline, Conversation
current_dir = os.getcwd()
from helpers import *
from config import *
# Build the AI
# nlp = transformers.pipeline("conversational", model="microsoft/DialoGPT-medium", tokenizer="microsoft/DialoGPT-medium", padding_side="left")

# nlp = transformers.pipeline("conversational"#, model="microsoft/DialoGPT-medium"
# )
class ChatBot():
    def __init__(self, name):
        print("--- starting up", name, "---")
        self.name = name

    def wake_up(self, text):
        return True if self.name in text.lower() else False

    @staticmethod
    def text_to_speech(text):
        print("ai --> ", text)
        speaker = gTTS(text=text, lang="en", slow=False)
        speaker.save("res.mp3")
        # macbook->afplay | windows->start
        os.system("start res.mp3")
        # print(current_dir+"\\res.mp3")
        # winsound.PlaySound(current_dir+"\\res.wav", winsound.SND_FILENAME)
        # os.remove("res.mp3")

    @staticmethod
    def action_time():
        return datetime.datetime.now().time().strftime('%H:%M')
    # funcionaria si me pillara el micro :(
    # def speech_to_text(self):
    #     recognizer = sr.Recognizer()
    #     with sr.Microphone() as mic:
    #         recognizer.adjust_for_ambient_noise(mic, duration=1)
    #         print("listening...")
    #         audio = recognizer.listen(mic)
    #     try:
    #         self.text = recognizer.recognize_google(audio)
    #         print("me --> ", self.text)
    #     except:
    #         print("me -->  ERROR")


# Run the AI
if __name__ == "__main__":
    settings = loadConfig()
    ai = ChatBot(name="maya")
    # while True:
    input_text = "hello!"
    pipe = pipeline(model="facebook/opt-1.3b")
    output = pipe(input_text, do_sample=True)
    print(output)
    # nlp(transformers.Conversation(input_text),pad_token_id=50256)
    ins = "Pon musica"
    if ai.wake_up("maya"):
        res = "Hello I am Maya the AI, what can I do for you?"
        ai.text_to_speech(res)
        res = ai.action_time()
        ai.text_to_speech(res)
        ai.text_to_speech(output[0]["generated_text"])

        if ins == "Pon musica":
            playMusic(settings["musica"])
    # ai.wake_up("maya")
    #      ai.speech_to_text()
