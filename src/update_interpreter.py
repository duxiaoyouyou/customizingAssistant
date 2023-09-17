import openai  
import os  
  
class UpdateInterpreter:  
    def __init__(self):  
        openai.api_key = os.getenv("OPENAI_API_KEY")  
  
    def interpret_update(self, update_content):  
        # 假设更新内容是一个列表，每个元素是一个关于API修改的句子  
        for sentence in update_content:  
            response = openai.Completion.create(  
              engine="text-davinci-002",  
              prompt=sentence,  
              temperature=0.5,  
              max_tokens=100  
            )  
            print(response.choices[0].text.strip())  
