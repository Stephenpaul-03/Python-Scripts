import os
from transformers import pipeline, AutoModelForSeq2SeqLM, AutoTokenizer

def load_text(file_path):
    ext = os.path.splitext(file_path)[-1].lower()
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

def chunk_text(text, max_length):
    words = text.split()
    return [' '.join(words[i:i + max_length]) for i in range(0, len(words), max_length)]

def summarize_chunk(summarizer, chunk, max_length):
    chunk_len = len(chunk.split())
    max_len = min(max_length, chunk_len // 4)  
    min_len = max(20, max_len // 2)            
    return summarizer(chunk, max_length=max_len, min_length=min_len, do_sample=False)[0]['summary_text']

def summarize_text(file_path):
    cache_dir = os.path.join("models", "distilBART")
    model = AutoModelForSeq2SeqLM.from_pretrained("sshleifer/distilbart-cnn-12-6", cache_dir=cache_dir)
    tokenizer = AutoTokenizer.from_pretrained("sshleifer/distilbart-cnn-12-6", cache_dir=cache_dir)
    summarizer = pipeline("summarization", model=model, tokenizer=tokenizer)

    text = load_text(file_path)
    token_limit = 1024
    chunk_size = 500  
    chunks = chunk_text(text, chunk_size)
    summaries = [summarize_chunk(summarizer, chunk, token_limit) for chunk in chunks]
    final_summary_text = ' '.join(summaries)
    
    # Further summarize if necessary
    while len(final_summary_text.split()) > token_limit:
        final_summary_text = summarize_chunk(summarizer, final_summary_text, token_limit)
    
    # Save summary to file
    base_name = os.path.splitext(os.path.basename(file_path))[0]
    summary_file_path = os.path.join(os.path.dirname(file_path), f"{base_name}_summary.txt")
    with open(summary_file_path, 'w', encoding='utf-8') as summary_file:
        summary_file.write(final_summary_text)
    
    print(f"\nSummary saved to: {summary_file_path}")

if __name__ == "__main__":
    file_name = input("Enter the file name (including extension): ")
    username = os.getlogin()
    file_path = os.path.join(f"C:/Users/{username}/Documents", file_name)
    if not os.path.exists(file_path):
        print(f"Error: The file '{file_name}' does not exist in 'C:/Users/{username}/Documents'.")
    else:
        summarize_text(file_path)
