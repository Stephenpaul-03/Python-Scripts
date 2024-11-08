import os
import whisper
import torch

def transcribe_audio(filename):
    model_dir = os.path.join("models", "whisper tiny.en")
    os.makedirs(model_dir, exist_ok=True)
    torch.hub.set_dir(model_dir)
    model = whisper.load_model("tiny.en")
    result = model.transcribe(filename)
    return result['text']

if __name__ == "__main__":
    filename = input("Enter the filename (without extension) to transcribe: ")
    music_folder = os.path.join(os.path.expanduser("~"), "Music", "Hermes Audio")
    audio_file_path = os.path.join(music_folder, f"{filename}.wav")
    transcription_folder = os.path.join("C:\\Users", os.getlogin(), "Documents", "Hermes Transcripts")
    os.makedirs(transcription_folder, exist_ok=True) 
    transcription_file_path = os.path.join(transcription_folder, f"{filename}.txt")
    
    if os.path.exists(audio_file_path):
        transcription = transcribe_audio(audio_file_path)
        with open(transcription_file_path, "w") as f:
            f.write(transcription)
        print(f"Transcription saved to {transcription_file_path}")
    else:
        print(f"No audio file found at {audio_file_path}. Please ensure the filename is correct.")
