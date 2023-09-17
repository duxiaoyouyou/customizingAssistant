import json  
from gtts import gTTS  
import os  
import pygame
import time
  
class TextToSpeech:  
    def __init__(self, text):  
        self.text = text
  
  
    def convert_json_to_string(self, json_object):  
        result_string = ""  
        for key, value in json_object.items():  
            if value != "null":  
                result_string += key + " is " + value + ". "  
        return result_string  
    
  
    def convert_text_to_speech(self, language='en'):  
        speech = gTTS(self.text, lang=language, slow=False)  
        speech.save("text_to_speech.mp3")  
        self.play_speech()
        

    def play_speech(self):  
        pygame.mixer.init()    
        pygame.mixer.music.load("text_to_speech.mp3")    
        pygame.mixer.music.play()    
        while pygame.mixer.music.get_busy() == True:    
            continue    
        pygame.mixer.music.stop()  
        pygame.mixer.quit()    
        time.sleep(1)  
        try:  
            os.remove("text_to_speech.mp3")  
        except PermissionError:  
            pass 

  
    def convert_json_to_speech(self):  
        text_string = self.convert_json_to_string()  
        self.convert_string_to_speech(text_string)  
        self.play_speech()  
  