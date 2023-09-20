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
from tkinter import simpledialog, messagebox 
from tkinter import Text, Scrollbar, Button, Entry, Label, Toplevel, END  
from tkinter.font import Font  
from src.version_checker import VersionChecker

requirement =  " We have a new storage bin in warehouse 100. " \
         f"This storage bin is 50 cm long and 60 cm wide, located at the center of the warehouse." \
         f"Create such a storage bin instance and return it"
    
def main():
    print(colored("\nCustomizing assistant is starting...\n", 'green'))
         
    file_path = "C:\\work\\EWM\\WarehouseInsights\\wr-core\\src\\main\\java\\com\\sap\\wi\\core\\application\\impl\\GWLServiceImpl.java"; 
    class_name = 'GWLServiceImpl'  
    method_name = 'getBinObj'  
    method_signature = get_method_signature(file_path, class_name, method_name) 
    
    messages = [{"role": "system", "content": "You are a senior java developer."}]      
    gptConnector = GPTConnector(messages)
    codeGenerator = CodeGenerator(method_signature, gptConnector)
   
    window = tk.Tk()  
    window.attributes('-topmost', True)   
    voiceInputUI = VoiceInputUI(window)  
    window.mainloop()  
      
    # Get voice input from user  
    #requirement = #voiceInputUI.voice_input
    requirement = requirement + "in the method: " + method_signature
  
    prompt = f"""
        You will be provided with the user requirement to generate codes in a java method. \
        The requirement is delimited by triple quotes. \
        You task is to generate code in a consistant style, following the criteria below: \
        1. Your answer should only contain the java codes and comments, which makes the method grammartically correct
        2. DO NOT generate anything other than the codes, no method signature, no expressions ahead, no big brackets. \      
        3. Ensure the generated code compatible with the method signature \
        4. Ensure the returning object compatible with the output of the method \
        5. Ensure there are no bugs or security issues in the code \
        6. Ensure only standard EWM fields are included \
            

        Examples delimited by triple hyphens
        --- 
            Requirement: simply return null
            code generated: return null
            Requirement: get the current time
            code generated: Instant currentTime = Instant.now()
            Requirement: \"\"\"  {requirement} \"\"\" \
        ---     
        
       """   
     
    # generate code
    customized_code = codeGenerator.generate_code(prompt);
    
    # feedback = "add more comments."
    feedback = show_code_and_get_feedback(customized_code)
    customized_code = codeGenerator.generate_code(feedback)  
    
    # feedback = "OK, replace the code in the method with the newly generated one." 
    feedback = show_code_and_get_feedback(customized_code)
    prompt = f"""
        You will be provided with the user feedback delimited by triple quotes. \
        You task is to generate answer to tell the if the user wants to replace the new code with the old one
        Your answer will be in a consistant format, following the criteria below: \
        1. If the user wants to replace his code with the newly generated code, simply return \"replace\". \
        2. If the user does not want to take the new code, simply return \"keep\". \      
       
        
        Examples delimited by triple hyphens \
        --- 
            feedback: Fine, I will take the new code \
            answer: replace \
            feedback: I want to discard the new code \
            answer: keep \
            feedback: \"\"\" {feedback} \"\"\" \
        --- 
       """
    command = codeGenerator.generate_code(prompt)
    if "replace" in command:
        integrator = CodeIntegrator(file_path) 
        integrator.replace_method(class_name, method_signature, customized_code)
    
    file_dir = os.path.dirname(file_path)  
    file_name = os.path.basename(file_path) 
    backup_directory = os.path.join(file_dir, "customization")   
    
    manager = VersionManager(file_dir, backup_directory, file_name)   
    manager.backup_code()  
    
    # rolling back the code to simulate version upgrade....
    
    manager.restore_code()  


def get_method_signature(file_path, class_name, method_name):  
    with open(file_path, 'r') as file:  
        java_code = file.read()  
  
    tree = javalang.parse.parse(java_code)  
  
    for path, node in tree.filter(javalang.tree.MethodDeclaration):  
        if node.name == method_name:  
            params = ', '.join(f"{param.type.name} {param.name}" for param in node.parameters)  
            return_type = node.return_type.name if node.return_type else 'void'  
            return f"{return_type} {class_name}.{method_name}({params})"  
  
    return None  

    

def show_code_and_get_feedback(code):       
    if code is None:      
        return None      
      
    root = tk.Tk()        
    root.title("Generated Code")      
      
    # Use a larger font for the code and feedback prompt      
    font = Font(family="Courier New", size=12)      
      
    # Create a Text widget to display the code      
    text = Text(root, width=80, height=20, font=font, padx=10, pady=10)      
    text.insert(END, code)      
    text.pack(side="left", fill="both", expand=True)      
      
    # Create a Scrollbar widget for the Text widget      
    scrollbar = Scrollbar(root, command=text.yview)      
    scrollbar.pack(side="left", fill="y")      
      
    # Link the Text widget and the Scrollbar widget      
    text.config(yscrollcommand=scrollbar.set)      
      
    # Create a Label widget for the feedback prompt      
    label = Label(root, text="Please enter your feedback:", font=font, padx=10, pady=10)      
    label.pack()      
      
    # Create a Text widget for the feedback input      
    feedback_input = Text(root, width=40, height=10, font=font, wrap="word", padx=10, pady=10)      
    feedback_input.pack()      
      
    # Create a Button widget to submit the feedback      
    button = Button(root, text="Submit", command=root.quit, padx=10, pady=10)      
    button.pack(side='right')      
      
    root.mainloop()        
      
    # Get the feedback from the Text widget      
    feedback = feedback_input.get("1.0", "end-1c")      
      
    root.destroy()        
    return feedback   


def display_code(code):  
    if code == None:
        pass
    root = tk.Tk()  
    root.withdraw()  # Hide the main window  
    messagebox.showinfo("Generated Code", code)  
    
    
def checkUpgradeCompatibility():
    checker = VersionChecker()  
    
    file_path = "C:\\work\\EWM\\AI\\customizingAssistant\\wr_upgrade.xlsx";  
    relevance = checker.check_version(file_path, requirement)
    print(colored(relevance, 'blue'))
    
    file_path = "C:\\work\\EWM\\AI\\customizingAssistant\\wi_upgrade.xlsx"; 
    relevance = checker.check_version(file_path, requirement)
    print(colored(relevance, 'blue'))
    
    
if __name__ == '__main__':  
    checkUpgradeCompatibility()
