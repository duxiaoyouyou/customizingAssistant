from src.version_manager import VersionManager
from src.code_generator import CodeGenerator
from src.code_integrator import CodeIntegrator 
from termcolor import colored  
import os
import javalang
from src.voice_collector import VoiceCollector
from flask import Flask, render_template 
from src.voice_input_ui import VoiceInputUI
from src.gpt_connector import GPTConnector
import tkinter as tk



def main():
    print(colored("\nCustomizing assistant is starting...\n", 'green'))
         
    file_path = "C:\\work\\EWM\\WarehouseInsights\\wr-core\\src\\main\\java\\com\\sap\\wi\\core\\application\\impl\\GWLServiceImpl.java"; 
    class_name = 'GWLServiceImpl'  
    method_name = 'getBinObj'  
    method_signature = get_method_signature(file_path, class_name, method_name) 
    
    window = tk.Tk()  
    voiceInputUI = VoiceInputUI(window)  
    window.mainloop()  
      
    # Get voice input from user  
    #voice_input = #voiceInputUI.voice_input
    voice_input =  " We have to move 60 handling units from storage bin C to storage bin D in warehouse 100. " \
         f"This should be completed by 8 p.m. tomorrow." \
         f"Therefore, I need you to create a warehouse task for me."
           
    requirement = voice_input + "in the method: " + method_signature
    requirement += ".\nEnsure only standard EWM fields are included."      
         
         
    system_message = f"You are a very senior JAVA developer." \
        f"You will simply generate the jave codes." \
                f"You will NOT generate the method signature, returning statement, big brackets, or comments. " 
    messages = [{"role": "system", "content": system_message}]  
    
      
    gptConnector = GPTConnector(messages)
    codeGenerator = CodeGenerator(method_signature, gptConnector)
    
    customized_code = codeGenerator.generate_code(requirement);

    feedback = "Can you add detailed comments on the generated code to make it more readable?"  
    customized_code = codeGenerator.generate_code(feedback)  

    integrator = CodeIntegrator(file_path)   
    integrator.integrate_enhancement(class_name, method_name, customized_code) 
        
    file_dir = os.path.dirname(file_path)  
    file_name = os.path.basename(file_path) 
    backup_directory = os.path.join(file_dir, "customization")   
    
    manager = VersionManager(file_dir, backup_directory, file_name)   
    manager.backup_code()  
    
    # simulating version upgrade....
    
    manager.restore_code()  


def get_method_signature(file_path, class_name, method_name):  
        with open(file_path, 'r') as file:  
            java_code = file.read()  
    
        tree = javalang.parse.parse(java_code)  
    
        for path, node in tree.filter(javalang.tree.MethodDeclaration):  
            if node.name == method_name:  
                params = ', '.join(param.type.name for param in node.parameters)  
                return_type = node.return_type.name if node.return_type else 'void'  
                return f"{return_type} {class_name}.{method_name}({params})"  
    
        return None  

  
if __name__ == '__main__':  
    #app.run(debug=True) 
    main() 
