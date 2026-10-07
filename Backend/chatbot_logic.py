import json 
import nltk 
from sklearn.feature_extraction.text import TfidfVectorizer 
from sklearn.metrics.pairwise import cosine_similarity 
 
# Download NLTK packages (they will be downloaded only the first time) 
nltk.download('punkt', quiet=True) 
 
# Load data from the JSON file 
def load_faqs(): 
    with open('faqs.json', 'r', encoding='utf-8') as file: 
        return json.load(file) 
 
faqs = load_faqs() 
# Collect only the questions into a list 
questions = [faq['question'] for faq in faqs] 
 
# Create a Vectorizer to convert text into numerical vectors using the TF-IDF method 
vectorizer = TfidfVectorizer() 
question_vectors = vectorizer.fit_transform(questions) 
 
def get_response(user_question): 
    # Convert the user's question into a vector 
    user_vector = vectorizer.transform([user_question]) 
     
    # Calculate cosine similarity (user question vs. questions in the database) 
    similarities = cosine_similarity(user_vector, question_vectors) 
     
    # Find the index of the most similar question 
    best_match_index = similarities.argmax() 
    best_match_score = similarities[0, best_match_index] 
     
    # If the similarity score is above 0.2, return the corresponding answer 
    if best_match_score > 0.2: 
        return faqs[best_match_index]['answer'] 
    else: 
        return "Sorry, I couldn't fully understand your question. Please try expressing it in a different way."