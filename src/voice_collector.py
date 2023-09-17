import speech_recognition as sr  
from termcolor import colored
  
class VoiceCollector:  
    def __init__(self):  
        self.recognizer = sr.Recognizer()  
  
    def get_voice_input(self):  
        with sr.Microphone() as source:  
            print("\nListening to user's requirement...pls tell...")  
            audio = self.recognizer.listen(source)  
            try:  
                voice_input = self.recognizer.recognize_google(audio)   
                print(colored("\nReceived voice requirement from user: " , 'green'))  
                print(voice_input);
                return voice_input  
            except sr.UnknownValueError:  
                print(colored("Google Speech Recognition could not understand audio", 'red') ) 
            except sr.RequestError as e:  
                print(colored("Could not request results from Google Speech Recognition service; ", 'red'))   
  
  