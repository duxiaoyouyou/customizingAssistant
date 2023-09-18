import re    
from .text_to_speech import TextToSpeech
from termcolor import colored
import os

class CodeIntegrator:    
    def __init__(self, file_path):    
        self.file_path = file_path    
  
  
    def _update_file(self, new_content):  
        with open(self.file_path, 'r+') as file:    
            file.seek(0)    
            file.write(new_content)    
            file.truncate()    
  
            file_name = os.path.basename(self.file_path)   
            text = "\nFile: " + file_name + " updated with customized content!";  
            print(colored(text,'green'))  
              
            tts = TextToSpeech(text)    
            tts.convert_text_to_speech()    
  
  
    def integrate_enhancement(self, class_name, method_name, new_code_block):    
        with open(self.file_path, 'r') as file:    
            content = file.read()    
    
            # Define pattern  
            pattern = re.compile(r'(class\s+' + class_name + r'.*?public\s+.*?\s+' + method_name + r'\(.*?\)\s*\{)(.*?)(\}\s*\Z)', re.DOTALL)    
    
            # Insert ahead   
            def replacer(match):    
                return match.group(1) + new_code_block + "\n" + match.group(2) + match.group(3)    
    
            new_content = re.sub(pattern, replacer, content)    
  
            self._update_file(new_content)  
  
  
    def add_method_to_class(self, class_name, new_code_block):    
        with open(self.file_path, 'r') as file:    
            content = file.read()    
    
            # Define pattern to match the end of the class  
            pattern = re.compile(r'(class\s+' + class_name + r'.*?)(\}\s*\Z)', re.DOTALL)    
    
            # Insert the new code block before the end of the class  
            def replacer(match):    
                return match.group(1) + "\n" + new_code_block + "\n" + match.group(2)    
    
            new_content = re.sub(pattern, replacer, content)    
  
            self._update_file(new_content)  
            
            
    def read_method_code(self, class_name, method_name):  
        with open(self.file_path, 'r') as file:  
            content = file.read()  
    
            # Define pattern  
            pattern = re.compile(r'(class\s+' + class_name + r'.*?public\s+.*?\s+' + method_name + r'\(.*?\)\s*\{)(.*?)(\}\s*\Z)', re.DOTALL)  
    
            # Search for the pattern  
            match = re.search(pattern, content)  
    
            if match:  
                # If the method is found, return its code  
                return match.group(2)  
            else:  
                # If the method is not found, return an appropriate message  
                return "Method not found."  


    def replace_method_code(self, class_name, method_name, new_code_block):  
        with open(self.file_path, 'r') as file:  
            content = file.read()  
    
            # Define pattern  
            pattern = re.compile(r'(class\s+' + class_name + r'.*?public\s+.*?\s+' + method_name + r'\(.*?\)\s*\{)(.*?)(\}\s*\Z)', re.DOTALL)  
    
            # Replace the old code block with the new one  
            def replacer(match):  
                return match.group(1) + "\n" + new_code_block + "\n" + match.group(3)  
    
            new_content = re.sub(pattern, replacer, content)  
    
            self._update_file(new_content)  

   
