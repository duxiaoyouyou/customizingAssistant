import os  
import shutil  
import time  
import win32security  
import ntsecuritycon as con  
import stat
import filecmp
from termcolor import colored
from .text_to_speech import TextToSpeech
import ctypes
  
  
class VersionManager:  
    def __init__(self, code_directory, backup_directory, file_name):  
        self.code_directory = code_directory  
        self.backup_directory = backup_directory 
        self.file_name = file_name 
        
  
    def add_everyone_full_control(self, folder):  
        everyone, domain, type = win32security.LookupAccountName("", "Everyone")  
        sd = win32security.GetFileSecurity(folder, win32security.DACL_SECURITY_INFORMATION)  
        dacl = sd.GetSecurityDescriptorDacl()  
        dacl.AddAccessAllowedAce(win32security.ACL_REVISION, con.FILE_ALL_ACCESS, everyone)  
        sd.SetSecurityDescriptorDacl(1, dacl, 0)  
        win32security.SetFileSecurity(folder, win32security.DACL_SECURITY_INFORMATION, sd)  
  
  
    def backup_code(self):  
        # backup the code before updating  
        if os.path.exists(self.backup_directory):  
            shutil.rmtree(self.backup_directory)  
  
        try:  
            os.makedirs(self.backup_directory, exist_ok=True)  
            time.sleep(1)  # wait for a second before changing the permissions  
            #self.add_everyone_full_control(self.backup_directory)      
            os.chmod(self.backup_directory, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)
        except OSError as e:  
            print(f"Error creating directory or changing permissions: {e}")  
  
        for filename in os.listdir(self.code_directory):  
           full_path = os.path.join(self.code_directory, filename)  
           if os.path.isfile(full_path) and filename == self.file_name:  
               #print("backing up file: " + filename +" to: " + self.backup_directory)
               shutil.copy(full_path, self.backup_directory)  
   
  
    def restore_code(self):  
        # restore the code after updating  
        for filename in os.listdir(self.backup_directory):  
            customer_file = os.path.join(self.backup_directory, filename)
            sap_file = os.path.join(self.code_directory,filename)
            if self.are_files_equal(sap_file, customer_file) == False:
                text = "\nDetected file: " + filename +" has been changed!"
                print(colored(text,'yellow'))  
                tts = TextToSpeech(text)
                tts.convert_text_to_speech()

                # Ask the user if they want to restore the file    
                result = ctypes.windll.user32.MessageBoxW(0, f"Do you want to restore {filename}?", "Restore File", 1 + 4096)  
                if result == 1:  # If the user clicked "OK"  
                    shutil.copy(os.path.join(self.backup_directory, filename), self.code_directory)    
                    text = "\nFile: " + filename +" successfully restored to customizated version!\n"    
                    print(colored(text,'blue'))      
                    tts = TextToSpeech(text)    
                    tts.convert_text_to_speech() 
                    
        shutil.rmtree(self.backup_directory)  
 
    
    def are_files_equal(self, file1, file2):  
        equal = filecmp.cmp(file1, file2, shallow=False)
        return equal
    