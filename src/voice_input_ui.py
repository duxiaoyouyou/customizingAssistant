import tkinter as tk  
from .voice_collector import VoiceCollector  

class VoiceInputUI:        
    def __init__(self, window):        
        self.window = window        
        self.window.title("Voice Input")        
        self.window.geometry('400x200')  # Set window size  
        self.center_window()  # Center the window  
        self.window.configure(bg='lightblue')  # Set window background color  
        self.voice_collector = VoiceCollector()        
        self.voice_input = ""    
        self.create_widgets()        
  
    def center_window(self):  
        # Get screen width and height  
        screen_width = self.window.winfo_screenwidth()  
        screen_height = self.window.winfo_screenheight()  
  
        # Calculate position  
        x = (screen_width / 2) - (400 / 2)  
        y = (screen_height / 2) - (200 / 2)  
  
        # Set window position  
        self.window.geometry('+%d+%d' % (x, y))  
        
    def create_widgets(self):        
        self.instructions_label = tk.Label(self.window, text="Press the button and speak your requirement:", bg='lightblue')        
        self.instructions_label.pack(pady=10)  # Add vertical padding  
        
        self.record_button = tk.Button(self.window, text="Record", command=self.record_voice, bg='lightgreen')        
        self.record_button.pack(pady=10)  # Add vertical padding  
        
        self.result_label = tk.Label(self.window, text="", bg='lightblue')        
        self.result_label.pack(pady=10)  # Add vertical padding  
        
    def record_voice(self):        
        self.voice_input = self.voice_collector.get_voice_input()    
        self.result_label['text'] = "Received voice requirement from user: \n" + self.voice_input  

