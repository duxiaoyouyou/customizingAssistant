import json  
  
  
class DataCollector:
    def generate_relevance_data(self):
        dataset = [  
            ("Introduced a new feature for bin management in the warehouse", {"warehouse": 1, "bin": 1, "create": 0, "storage": 1, "long": 0, "wide": 0, "center": 0}),  
            ("Implemented a new system for tracking warehouse tasks", {"warehouse": 1, "bin": 0, "create": 0, "storage": 0, "long": 0, "wide": 0, "center": 0}),  
            ("Updated the layout of the warehouse to improve efficiency", {"warehouse": 1, "bin": 0, "create": 0, "storage": 0, "long": 0, "wide": 0, "center": 1}),  
            ("Added a new type of storage bin to the warehouse", {"warehouse": 1, "bin": 1, "create": 0, "storage": 1, "long": 0, "wide": 0, "center": 0}),  
            ("Improved the resource allocation algorithm for warehouse tasks", {"warehouse": 1, "bin": 0, "create": 0, "storage": 0, "long": 0, "wide": 0, "center": 0}),  
            ("Implemented a new system for managing outbound shipments", {"warehouse": 0, "bin": 0, "create": 0, "storage": 0, "long": 0, "wide": 0, "center": 0}),  
            ("Updated the warehouse management system user interface", {"warehouse": 1, "bin": 0, "create": 0, "storage": 0, "long": 0, "wide": 0, "center": 0}),  
            ("Introduced a new feature for managing perishable goods in the warehouse", {"warehouse": 1, "bin": 0, "create": 0, "storage": 0, "long": 0, "wide": 0, "center": 0}),  
            ("Implemented a new system for tracking employee hours in the warehouse", {"warehouse": 1, "bin": 0, "create": 0, "storage": 0, "long": 0, "wide": 0, "center": 0}),  
            ("Updated the safety protocols for warehouse operations", {"warehouse": 1, "bin": 0, "create": 0, "storage": 0, "long": 0, "wide": 0, "center": 0}),  
            ("Introduced a new type of forklift for warehouse operations", {"warehouse": 1, "bin": 0, "create": 0, "storage": 0, "long": 0, "wide": 0, "center": 0}),  
            ("Implemented a new inventory counting system in the warehouse", {"warehouse": 1, "bin": 0, "create": 0, "storage": 0, "long": 0, "wide": 0, "center": 0}),  
            ("Updated the warehouse operating hours", {"warehouse": 1, "bin": 0, "create": 0, "storage": 0, "long": 0, "wide": 0, "center": 0}),  
            ("Implemented a new system for managing product returns in the warehouse", {"warehouse": 1, "bin": 0, "create": 0, "storage": 0, "long": 0, "wide": 0, "center": 0}),  
            ("Updated the policies for handling hazardous materials in the warehouse", {"warehouse": 1, "bin": 0, "create": 0, "storage": 0, "long": 0, "wide": 0, "center": 0}),  
            ("Implemented a new system for managing outbound shipments in the warehouse", {"warehouse": 1, "bin": 0, "create": 0, "storage": 0, "long": 0, "wide": 0, "center": 0}),  
            ("Updated the warehouse task management system", {"warehouse": 1, "bin": 0, "create": 0, "storage": 0, "long": 0, "wide": 0, "center": 0}),  
            ("Introduced a new type of warehouse task", {"warehouse": 1, "bin": 0, "create": 0, "storage": 0, "long": 0, "wide": 0, "center": 0}),  
            ("Updated the bin management system to support a new type of bin", {"warehouse": 1, "bin": 1, "create": 0, "storage": 0, "long": 0, "wide": 0, "center": 0}),  
            ("Updated the warehouse task system to support long and wide bins", {"warehouse": 1, "bin": 1, "create": 0, "storage": 0, "long": 1, "wide": 1, "center": 0}),  
            ("Updated the warehouse task system to support a new type of storage type", {"warehouse": 1, "bin": 0, "create": 0, "storage": 1, "long": 0, "wide": 0, "center": 0}),  
            ("Updated the warehouse task system to support a new type of storage section", {"warehouse": 1, "bin": 0, "create": 0, "storage": 1, "long": 0, "wide": 0, "center": 0}),  
            ("Updated the warehouse task system to support a new type of storage unit", {"warehouse": 1, "bin": 0, "create": 0, "storage": 1, "long": 0, "wide": 0, "center": 0}),  
            ("Updated the warehouse task system to support a new type of product", {"warehouse": 1, "bin": 0, "create": 0, "storage": 0, "long": 0, "wide": 0, "center": 0}),  
            ("Updated the warehouse task system to support a new type of forklift", {"warehouse": 1, "bin": 0, "create": 0, "storage": 0, "long": 0, "wide": 0, "center": 0}),  
            ("Updated the warehouse task system to implement a new safety protocol", {"warehouse": 1, "bin": 0, "create": 0, "storage": 0, "long": 0, "wide": 0, "center": 0}),  
            ("Updated the warehouse task system to implement a new inventory counting system", {"warehouse": 1, "bin": 0, "create": 0, "storage": 0, "long": 0, "wide": 0, "center": 0}),  
            ("Updated the warehouse task system operating hours", {"warehouse": 1, "bin": 0, "create": 0, "storage": 0, "long": 0, "wide": 0, "center": 0}),  
            ("Updated the warehouse task system to implement a new system for tracking employee hours", {"warehouse": 1, "bin": 0, "create": 0, "storage": 0, "long": 0, "wide": 0, "center": 0}),  
            ("Updated the warehouse task system policies for handling hazardous materials", {"warehouse": 1, "bin": 0, "create": 0, "storage": 0, "long": 0, "wide": 0, "center": 0}),  
            ("Updated the warehouse task system to implement a new system for managing product returns", {"warehouse": 1, "bin": 0, "create": 0, "storage": 0, "long": 0, "wide": 0, "center": 0}),  
            ("Updated the warehouse task system policies for handling perishable goods", {"warehouse": 1, "bin": 0, "create": 0, "storage": 0, "long": 0, "wide": 0, "center": 0}),  
            ("Updated the warehouse task system to implement a new system for managing outbound shipments", {"warehouse": 1, "bin": 0, "create": 0, "storage": 0, "long": 0, "wide": 0, "center": 0}),  
        ]  
        return dataset  
