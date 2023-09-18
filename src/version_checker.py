import csv  
import spacy  
from sklearn.feature_extraction.text import CountVectorizer  
from sklearn.metrics.pairwise import cosine_similarity  
from sklearn.svm import SVC  
from sklearn.model_selection import train_test_split  
from .gpt_connector import GPTConnector
  
class VersionChecker:  
    def __init__(self, csv_file, requirement):  
        self.csv_file = csv_file  
        self.requirement = requirement
        self.nlp = spacy.load('en_core_web_sm')  
        self.model = self._train_model()  
        self.feature_description = self.get_feature_description(requirement) 
  
  
    def check_version(self):  
        with open(self.csv_file, 'r') as file:  
            reader = csv.DictReader(file)  
            for row in reader:  
                similarity_score = self._get_similarity(row['description'], self.feature_description)  
                if similarity_score > 0.8:  # assuming a threshold of 0.8 for similarity  
                    return f"The method might be affected by the version update. Similarity score: {similarity_score}"  
        return f"The method is not affected by the version update."  
  
      
    def _get_similarity(self, text1, text2):  
        vectorizer = CountVectorizer().fit_transform([text1, text2])  
        vectors = vectorizer.toarray()  
        return cosine_similarity(vectors)[0][1]  
  
  
    def _train_model(self):  
        dataset = self.mock_dataset()
        texts, labels = zip(*dataset)  
        X_train, X_test, y_train, y_test = train_test_split(texts, labels, test_size=0.2, random_state=42)  
        vectorizer = CountVectorizer().fit(X_train)  
        X_train = vectorizer.transform(X_train)  
        X_test = vectorizer.transform(X_test)  
        model = SVC().fit(X_train, y_train)  
        print(f"Model accuracy: {model.score(X_test, y_test)}")  
        return model  
    
    
    def get_feature_description(self, requirement):
         messages = [{"role": "system", "content": "You are a senior EWM consultant."}]      
         gptConnector = GPTConnector(messages)
         prompt = f"""
        You will be provided with the user requirement delimited by triple quotes. \
        You task is to extract the EWM key words from the requirement and seperate them by ; \

        Examples delimited by triple hyphens
        --- 
            Requirement: I want to create a warehouse task which starts tomorrow
            key words: warehouse task
            Requirement: I have to move the resources from here to there
            key words: resource
            Requirement: \"\"\"  {requirement} \"\"\" \
        ---     
        
       """   
         feature_descrption = gptConnector.transform(prompt)
         return feature_descrption
   
    
    def mock_dataset(self):
        dataset =  [  
            ("The warehouse layout has been updated with new bin locations.", 1),  
            ("New API methods have been added for integration with fleet management systems.", 0),  
            ("The warehouse now supports long and wide bins.", 1),  
            ("The bin management system has been updated.", 1),  
            ("The warehouse now supports a new type of product.", 0),  
            ("The center of the warehouse has been redesigned.", 1),  
            ("The warehouse now supports a new type of bin.", 1),  
            ("The warehouse layout has been updated.", 1),  
            ("The bin management system now supports a new type of bin.", 1),  
            ("The warehouse now supports a new type of robot.", 0),  
            ("The storage type for the new bins has been updated.", 1),  
            ("The storage section for the new bins has been updated.", 1),  
            ("The storage unit for the new bins has been updated.", 1),  
            ("The warehouse now supports a new type of storage type.", 0),  
            ("The warehouse now supports a new type of storage section.", 0),  
            ("The warehouse now supports a new type of storage unit.", 0),  
            ("The user interface of the warehouse management system has been updated.", 0),  
            ("New safety protocols have been implemented in the warehouse.", 0),  
            ("The warehouse now supports a new type of forklift.", 0),  
            ("The warehouse has implemented a new inventory counting system.", 0),  
            ("The warehouse has updated its operating hours.", 0),  
            ("The warehouse has implemented a new system for tracking employee hours.", 0),  
            ("The warehouse has updated its policies for handling hazardous materials.", 0),  
            ("The warehouse has implemented a new system for managing product returns.", 0),  
            ("The warehouse has updated its policies for handling perishable goods.", 0),  
            ("The warehouse has implemented a new system for managing outbound shipments.", 0),  
            ("The warehouse task management system has been updated.", 1),  
            ("The warehouse now supports a new type of warehouse task.", 1),  
            ("The warehouse task system now supports a new type of bin.", 1),  
            ("The warehouse task system now supports long and wide bins.", 1),  
            ("The warehouse task system has been updated to support a new type of storage type.", 1),  
            ("The warehouse task system has been updated to support a new type of storage section.", 1),  
            ("The warehouse task system has been updated to support a new type of storage unit.", 1),  
            ("The warehouse task system now supports a new type of product.", 0),  
            ("The warehouse task system now supports a new type of forklift.", 0),  
            ("The warehouse task system has implemented a new safety protocol.", 0),  
            ("The warehouse task system has implemented a new inventory counting system.", 0),  
            ("The warehouse task system has updated its operating hours.", 0),  
            ("The warehouse task system has implemented a new system for tracking employee hours.", 0),  
            ("The warehouse task system has updated its policies for handling hazardous materials.", 0),  
            ("The warehouse task system has implemented a new system for managing product returns.", 0),  
            ("The warehouse task system has updated its policies for handling perishable goods.", 0),  
            ("The warehouse task system has implemented a new system for managing outbound shipments.", 0),  
        ]  
        return dataset

