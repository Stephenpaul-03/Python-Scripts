from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os

def load_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def calculate_cosine_similarity(file_path1, file_path2):
    text1 = load_text(file_path1)
    text2 = load_text(file_path2)
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([text1, text2])
    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    return similarity[0][0]

if __name__ == "__main__":
    file_name1 = input("Enter the first file name (including extension): ")
    file_name2 = input("Enter the second file name (including extension): ")
    
    username = os.getlogin()
    file_path1 = os.path.join(f"C:/Users/{username}/Documents", file_name1)
    file_path2 = os.path.join(f"C:/Users/{username}/Documents", file_name2)

    if not os.path.exists(file_path1):
        print(f"Error: The file '{file_name1}' does not exist in 'C:/Users/{username}/Documents'.")
    elif not os.path.exists(file_path2):
        print(f"Error: The file '{file_name2}' does not exist in 'C:/Users/{username}/Documents'.")
    else:
        similarity_score = calculate_cosine_similarity(file_path1, file_path2)
        print(f"\nCosine Similarity between the two files: {similarity_score:.4f}")
