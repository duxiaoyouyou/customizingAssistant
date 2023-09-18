from .gpt_connector import GPTConnector
import inspect
import sys
import javalang
from termcolor import colored
from .text_to_speech import TextToSpeech

class CodeGenerator:  
    def __init__(self, method_signature, gptConnector): 
        self.method_signature = method_signature
        self.gptConnector = gptConnector
        
  
    def generate_code(self, requirement):
        if(requirement == None):
            return None
        
        text = "\nStart generating answer based on user's requirement... \n"
        print(colored(text, 'blue'))
        tts = TextToSpeech(text)  
        tts.convert_text_to_speech()  
        
        return self.gptConnector.transform(requirement)
        
  
