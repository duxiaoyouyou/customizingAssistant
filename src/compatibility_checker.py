class CompatibilityChecker:  
    def __init__(self, custom_code, update_interpretation):  
        self.custom_code = custom_code  
        self.update_interpretation = update_interpretation  
  
    def check_compatibility(self):  
        incompatible_items = []  
  
        # 假设update_interpretation是一个字典，包含了LLM理解的更新内容  
        for api, effect in self.update_interpretation.items():  
            if api in self.custom_code:  
                incompatible_items.append((api, effect))  
  
        if incompatible_items:  
            print("The following items are incompatible:")  
            for item in incompatible_items:  
                print(f"API: {item[0]}, Effect: {item[1]}")  
            return False  
        else:  
            print("The custom code is compatible with the cloud product update.")  
            return True  
