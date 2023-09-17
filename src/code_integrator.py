import re    
from .text_to_speech import TextToSpeech
from termcolor import colored
import os

class CodeIntegrator:  
    def __init__(self, file_path):  
        self.file_path = file_path  
  
  
    def integrate_enhancement(self, class_name, method_name, new_code_block):  
        with open(self.file_path, 'r+') as file:  
            content = file.read()  
  
            # define pattern
            pattern = re.compile(r'(class\s+' + class_name + r'.*?public\s+.*?\s+' + method_name + r'\(.*?\)\s*\{)(.*?)(\}\s*\Z)', re.DOTALL)  
  
            # insert ahead 
            def replacer(match):  
                return match.group(1) + new_code_block + "\n" + match.group(2) + match.group(3)  
                #return match.group(1) + match.group(2) + "\n" + new_code_block + match.group(3)  

  
            new_content = re.sub(pattern, replacer, content)  
  
            file.seek(0)  
            file.write(new_content)  
            file.truncate()  
            
            file_name = os.path.basename(self.file_path) 
            text = "\nFile: " + file_name + " updated with customized content!";
            print(colored(text,'green'))
            
            tts = TextToSpeech(text)  
            tts.convert_text_to_speech()  
    
