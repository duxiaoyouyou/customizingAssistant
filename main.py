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
  

def main():
    print(colored("\nCustomizing assistant is starting...\n", 'green'))
         
    file_path = "C:\\work\\EWM\\WarehouseInsights\\wr-core\\src\\main\\java\\com\\sap\\wi\\core\\application\\impl\\GWLServiceImpl.java"; 
    class_name = 'GWLServiceImpl'  
    method_name = 'getBinObj'  
    method_signature = get_method_signature(file_path, class_name, method_name) 
    
    window = tk.Tk()  
    window.attributes('-topmost', True)   
    voiceInputUI = VoiceInputUI(window)  
    window.mainloop()  
      
    # Get voice input from user  
    #voice_input = #voiceInputUI.voice_input
    voice_input =  " We have to move 60 handling units from storage bin C to storage bin D in warehouse 100. " \
         f"This should be completed by 8 p.m. tomorrow." \
         f"Therefore, I need you to create a warehouse task for me."
           
    requirement = voice_input + "in the method: " + method_signature
    requirement += ".\nEnsure only standard EWM fields are included."      
         
    integrator = CodeIntegrator(file_path) 
         
    system_message = f"You will simply generate the jave codes." \
                f"You will NOT generate the method signature, returning statement, or big brackets. "  \
                    f"Everytime the newly generated code MUST be compliant with the original code. " 
    messages = [{"role": "system", "content": system_message}]  
    
    original_code = integrator.read_method_code(class_name, method_name)
    messages.append({"role": "assistant", "content": "original code: \n" + original_code})  
    
      
    gptConnector = GPTConnector(messages)
    codeGenerator = CodeGenerator(method_signature, gptConnector)
    
    # generate code
    customized_code = codeGenerator.generate_code(requirement);
    
    # generate comments
    feedback = show_code_and_get_feedback(customized_code)
    # feedback = "add more comments."  
    customized_code = codeGenerator.generate_code(feedback)  
    integrator.integrate_enhancement(class_name, method_name, customized_code) 
    
    # unit test
    feedback = show_code_and_get_feedback(customized_code)
    # feedback = "add a ut method for the code with imports"  
    ut_code = codeGenerator.generate_code(feedback)  
    
    display_code(ut_code)
  
    integrator.add_method_to_class(class_name, ut_code)
    
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
    

def show_code_and_get_feedback(code):     
    if code is None:    
        return None    
    
    root = tk.Tk()      
    root.title("Generated Code")    
    
    # Use a larger font for the code and feedback prompt    
    font = Font(family="Courier New", size=12)    
    
    # Create a Text widget to display the code    
    text = Text(root, width=80, height=20, font=font)    
    text.insert(END, code)    
    text.pack(side="left", fill="both", expand=True)    
    
    # Create a Scrollbar widget for the Text widget    
    scrollbar = Scrollbar(root, command=text.yview)    
    scrollbar.pack(side="left", fill="y")    
    
    # Link the Text widget and the Scrollbar widget    
    text.config(yscrollcommand=scrollbar.set)    
    
    # Create a Label widget for the feedback prompt    
    label = Label(root, text="Please enter your feedback:", font=font)    
    label.pack()    
    
    # Create a Text widget for the feedback input    
    feedback_input = Text(root, width=40, height=10, font=font, wrap="word")    
    feedback_input.pack()    
    
    # Create a Button widget to submit the feedback    
    button = Button(root, text="Submit", command=root.quit)    
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

    
if __name__ == '__main__':  
    #app.run(debug=True) 
    main() 
