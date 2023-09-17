from .gpt_connector import GPTConnector
import inspect
import sys
import javalang
from termcolor import colored
from .text_to_speech import TextToSpeech

class CodeGenerator:  
    def __init__(self, requirement, method_signature): 
        self.requirement = requirement
        self.method_signature = method_signature
        
  
    def generate_code(self):
        system_message = f"You are a very senior JAVA developer." \
            f"You will simply generate the jave codes." \
                f"You will NOT generate the method signature, returning statement, big brackets, or comments. " \
     
        text = "\nStart generating code based on user's requirement... \n"
        print(colored(text, 'blue'))
        tts = TextToSpeech(text)  
        tts.convert_text_to_speech()  
        
        gptConnector  = GPTConnector(system_message)  
        code = "\n" + gptConnector.transform(self.requirement)
        
        return code
  
