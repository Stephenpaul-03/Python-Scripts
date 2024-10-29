import os
import shutil

FILE_CATEGORIES = {
    "Code Files": ['.py', '.js', '.html', '.css', '.cpp', '.c', '.java', '.php', '.rb', '.sql', '.sh'],
    "Images": ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.tiff'],
    "Videos": ['.mp4', '.mkv', '.flv', '.avi', '.mov', '.wmv'],
    "Audios": ['.mp3', '.wav', '.aac', '.ogg', '.flac', '.wma'],
    "Documents": ['.doc', '.docx', '.txt'],
    "Excel": ['.xls', '.xlsx'],
    "Presentations": ['.ppt', '.pptx'],
    "PDFs": ['.pdf']
}

def organizer(directory_path):
    unclassified_folder = os.path.join(directory_path, "Unclassified")
    os.makedirs(unclassified_folder, exist_ok=True)

    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        if os.path.isdir(file_path):
            continue
        _, file_extension = os.path.splitext(filename)
        folder = None
        for category, extensions in FILE_CATEGORIES.items():
            if file_extension.lower() in extensions:
                folder = category
                break
        if folder:
            target_folder = os.path.join(directory_path, folder)
            os.makedirs(target_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(target_folder, filename))
            print(f"Moved {filename} to {folder}")
        else:
            shutil.move(file_path, os.path.join(unclassified_folder, filename))
            print(f"Moved {filename} to Unclassified")


path = input("Enter the directory path to organize: ").strip()
if os.path.exists(path) and os.path.isdir(path):
    organizer(path)
    print("Directory organized successfully!")
else:
    print("The specified path is not a valid directory.")
