import csv  
import spacy  
from sklearn.feature_extraction.text import CountVectorizer  
from sklearn.metrics.pairwise import cosine_similarity  
from sklearn.svm import SVC  
from sklearn.model_selection import train_test_split  
from .gpt_connector import GPTConnector
from sklearn.model_selection import GridSearchCV, cross_val_score
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from .data_collector import DataCollector
import json
import pandas as pd
  
class VersionChecker:  
    def __init__(self):  
        # self.nlp = spacy.load('en_core_web_sm')
        # self.model, self.vectorizer = self._train_model()     
        messages = [{"role": "system", "content": "You are a senior EWM consultant."}]      
        self.gptConnector = GPTConnector(messages)
        
 
    def check_version(self, file, custom_requirement):  
        df = pd.read_excel(file)  
        feature_descriptions = list(df['Description'])  
    
        # Construct the prompt  
       
        prompt = f"""
        I have a new features description list delimited by triple quotes. \
            \"\"\" {feature_descriptions} \"\"\" \
        And I have my custom code to implement my requirement. \
        My feature descritpion is delimited by triple hyphens. \
        --- 
            {custom_requirement} 
        ---     
        You task is to judege: Will any of the new features possibly affect the functionality of my custom code? \
        If yes, list out all the features which will affect the functionality of my custom code \
        If no, return not affected  \
       """
        # Use the OpenAI API to generate a response  
        response_text = self.gptConnector.transform(prompt)  
    
        # Parse the response to extract the features that will affect the code  
        affected_features = []  
        if 'yes' in response_text.lower():  
            response_lines = response_text.split('\n')  
            for line in response_lines:  
                if 'feature:' in line.lower():  
                    affected_features.append(line)  
    
        return affected_features  


    
    def get_feature_description(self, requirement):
        prompt = f"""
        You will be provided with the user requirement delimited by triple quotes. \
        You task is to extract the EWM key words from the requirement \
        You will only return the EWM key words delimited by ; \
        Examples delimited by triple hyphens
        --- 
            Requirement: I want to create a warehouse task which starts tomorrow
            warehouse task
            Requirement: I have to move the resources from here to there
            resource
            Requirement: \"\"\"  {requirement} \"\"\" \
        ---     
        
       """   
        feature_descrption = self.gptConnector.transform(prompt)
        return feature_descrption
   
   
    def _get_similarity(self, text1, text2):    
        vectorizer = CountVectorizer().fit_transform([text1, text2])    
        vectors = vectorizer.toarray()    
        return cosine_similarity(vectors)[0][1]    
    
 
    def _train_model(self):  
        dataset = DataCollector().generate_relevance_data()
       
        # Convert the labels to strings  
        texts, labels = zip(*[(text, json.dumps(label)) for text, label in dataset])  
  
        # Encode the labels  
        label_encoder = LabelEncoder().fit(labels)  
        labels = label_encoder.transform(labels)  
  
  
        X_train, X_test, y_train, y_test = train_test_split(texts, labels, test_size=0.2, random_state=42)    
        vectorizer = CountVectorizer().fit(X_train)    
        X_train = vectorizer.transform(X_train)    
        X_test = vectorizer.transform(X_test)    
    
        # Define the parameter grid for the grid search  
        param_grid = {'C': [0.1, 1, 10, 100], 'gamma': [1, 0.1, 0.01, 0.001], 'kernel': ['rbf', 'linear']}  
    
        # Initialize the grid search  
        grid = GridSearchCV(SVC(), param_grid, refit=True, verbose=2)  
    
        # Fit the grid search  
        grid.fit(X_train, y_train)  
    
        # Print the best parameters  
        print(f"Best parameters: {grid.best_params_}")  
    
        # Initialize the model with the best parameters  
        model = SVC(C=grid.best_params_['C'], gamma=grid.best_params_['gamma'], kernel=grid.best_params_['kernel'])  
    
        # Fit the model  
        model.fit(X_train, y_train)  
    
        # Perform cross-validation and print the average score  
        scores = cross_val_score(model, X_train, y_train, cv=5)  
        print(f"Cross-validation score: {scores.mean()}")  
    
        # Print the test score  
        print(f"Test score: {model.score(X_test, y_test)}")  
    
        return model, vectorizer
    
    
    def predict(self, text):  
        # Transform the text to the format the model was trained on  
        X = self.vectorizer.transform([text])  
        
        # Use the model to predict the label  
        prediction = self.model.predict(X)  
        
        # Return the predicted label  
        return prediction  

