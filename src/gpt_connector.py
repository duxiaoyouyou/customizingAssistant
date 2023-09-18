import requests  
import json  
from getpass import getpass 
import inspect
from termcolor import colored
from .text_to_speech import TextToSpeech

class GPTConnector:
    
    def __init__(self, messages):  
        self.api_endpoint = "https://azure-openai-serv-i057149.cfapps.sap.hana.ondemand.com/api/v1/completions"
        self.authentication_url = "https://ewm.authentication.sap.hana.ondemand.com"
        self.client_id = "sb-2401ff09-f941-49f2-aca4-60e1589b2cc0!b2609|azure-openai-service-i057149-xs!b16730"
        self.client_secret = "fa02e9aa-4cc5-46f2-aa34-cb44a3ee2688$dROwb-37vo4vUsu6PPYX2roE9dEv_pMPD0Wm6njQuAs="
        self.deployment_id = "gpt-4-32k"
        self.max_tokens = 16000
        self.temperature = 0.01
        self.messages = messages 
         
        
    def get_access_token(self):
        print(colored("\nGetting access token to connect to BTP LLM...", 'green'))
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}  
        data = {'grant_type': 'client_credentials', 'client_id': self.client_id, 'client_secret': self.client_secret}  
        reponse = requests.post(self.authentication_url + "/oauth/token", headers = headers, data = data)
        response_json = reponse.json()
        
        return response_json['access_token']  
    
    
    
    def transform(self, requirement):  
        accessToken = self.get_access_token()   
        print(colored("\nAccess token got, start transforming requirement...", 'blue'))
        headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + accessToken} 

        requirement =  "Generate the java code block to fulfill the requirement: " + requirement 
        self.messages.append({"role": "user", "content": requirement})  
    
        data = {    
            "deployment_id": self.deployment_id,     
            "max_tokens": self.max_tokens,  
            "temperature": self.temperature,   
            "messages": self.messages
        }   
        
        response = requests.post(self.api_endpoint, headers=headers, data=json.dumps(data))    
        response_json = response.json()    
        content = response_json['choices'][0]['message']['content']    
        
        # Save the assistant's message to be the context
        self.messages.append({"role": "assistant", "content":  content})  
         
        text = "\nResult generated as below: "
        print(colored(text, 'blue'))
        tts = TextToSpeech(text)  
        tts.convert_text_to_speech() 
        print(content)
    
        return content  

  
        