from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from data import qa_data
import re

def preprocess(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    return text

questions = [preprocess(item["question"]) for item in qa_data]
answers = [item["answer"] for item in qa_data]

vectorizer = TfidfVectorizer(ngram_range=(1, 2))
tfidf_matrix = vectorizer.fit_transform(questions)

def get_answer(user_question):
    user_question = preprocess(user_question)
    user_vec = vectorizer.transform([user_question])
    similarities = cosine_similarity(user_vec, tfidf_matrix)

    best_idx = similarities.argmax()
    confidence = similarities[0][best_idx]

    if confidence < 0.25:
        return "🤖 Xin lỗi, tôi chưa hiểu rõ câu hỏi của bạn."

    return f"{answers[best_idx]} (Độ tin cậy: {confidence:.2f})"
