import csv  
import spacy  
from sklearn.feature_extraction.text import CountVectorizer  
from sklearn.metrics.pairwise import cosine_similarity  
from sklearn.svm import SVC  
from sklearn.model_selection import train_test_split  
  
class VersionChecker:  
    def __init__(self, csv_file, method_code, openai_key):  
        self.csv_file = csv_file  
        self.method_code = method_code  
        self.openai_key = openai_key  
        self.nlp = spacy.load('en_core_web_sm')  
        self.model = self._train_model()  
  
    def check_version(self):  
        method_description = self._generate_description(self.method_code)  
        with open(self.csv_file, 'r') as file:  
            reader = csv.DictReader(file)  
            for row in reader:  
                similarity_score = self._get_similarity(row['description'], method_description)  
                if similarity_score > 0.8:  # assuming a threshold of 0.8 for similarity  
                    return f"The method might be affected by the version update. Similarity score: {similarity_score}"  
        return f"The method is not affected by the version update."  
  
      
  
    def _get_similarity(self, text1, text2):  
        vectorizer = CountVectorizer().fit_transform([text1, text2])  
        vectors = vectorizer.toarray()  
        return cosine_similarity(vectors)[0][1]  
  
    def _train_model(self):  
        # assuming you have a labeled dataset in the format [(text, label), ...]  
        dataset = [...]    
        texts, labels = zip(*dataset)  
        X_train, X_test, y_train, y_test = train_test_split(texts, labels, test_size=0.2, random_state=42)  
        vectorizer = CountVectorizer().fit(X_train)  
        X_train = vectorizer.transform(X_train)  
        X_test = vectorizer.transform(X_test)  
        model = SVC().fit(X_train, y_train)  
        print(f"Model accuracy: {model.score(X_test, y_test)}")  
        return model  
  
# Usage  
checker = VersionChecker('your_file.csv', 'your_method_code', 'your_openai_key')  
print(checker.check_version())  
