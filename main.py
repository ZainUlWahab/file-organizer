# Import necessary libraries
import os
import shutil
import tkinter as tk
from tkinter import messagebox

# All the extensions
document_extensions = document_extensions = ["doc", "docx", "txt", "pdf", "xls", "xlsx", "ppt", "pptx", "csv", "odt", "ods", "odp", "rtf", "md", "tex", "log"]
image_extensions = ["jpeg", "jpg", "gif", "png", "bmp", "tif", "tiff", "ico", "svg", "webp", "heic", "raw"]
video_extensions = ["mp4", "avi", "mov", "mkv", "wmv", "flv", "webm", "m4v", "mpg", "mpeg", "3gp", "3g2", "ts", "mts"]
shortcut_extension = ["lnk"]
audio_extensions = ["mp3", "wav", "ogg", "flac", "aac", "m4a", "wma", "ape", "alac", "aiff", "opus", "mid", "midi"]
code_extensions = ["py", "java", "c", "cpp", "h", "hpp", "cs", "rb", "js", "json", "html", "xml", "css", "php", "swift", "go", "lua", "pl", "sql", "sh", "bat", "ps1", "asm"]
archive_extensions = ["zip", "tar", "gz", "bz2", "xz", "7z", "rar", "iso", "dmg", "pkg"]
executable_file_extensions = ["exe", "com", "cmd", "msi", "app", "run", "jar"]
configuration_extensions = ["conf", "ini", "cfg", "properties", "yaml", "yml"]
database_extensions = ["db", "sqlite", "mdb", "accdb", "dbf"]

# Dictionary to map extension to their folders
extension_map = {
    "Document" : document_extensions,
    "Image" : image_extensions,
    "Video" : video_extensions,
    "Shortcuts" : shortcut_extension,
    "Audio" : audio_extensions,
    "Code" : code_extensions,
    "Archive" : archive_extensions,
    "Executables" : executable_file_extensions,
    "Configuration" : configuration_extensions,
    "Database" : database_extensions
}

# Function to make a folder name
def make_folder_name(extension):
    for name,extensions in extension_map.items():
        if extension in extensions:
            return f"{name}_Files_Folder"
    return "Other_Files_Folder"

# function which runs till every file is not in its designated folder
def organize_files():
    files = [f for f in os.listdir() if not f.startswith('.')]  # Exclude hidden files
    for file in files:
        try:
            if os.path.isfile(file):
                _,ext = os.path.splitext(file)
                folder_name = make_folder_name(ext[1:].lower())
                if not os.path.exists(folder_name):
                    os.mkdir(folder_name)
                shutil.move(file,folder_name)
        except Exception as e:
            print(f"Error occurred while organizing {file}: {e}")

# Function to handle button click event
def on_button_click():
    try:
        organize_files()
        messagebox.showinfo("Success", "Files organized successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def starting_gui():

    # Create the main window
    root = tk.Tk()
    root.title("File Organizer")

    # Set window size to 800x600
    root.geometry("400x400")

    # Set background color to darkslategray
    root.configure(bg="darkslategray")

    # Create a label widget for "File Organizer"
    label = tk.Label(root, text="File Organizer", font=("Arial", 20), bg="darkslategray", fg="black")
    label.pack(pady=10,anchor = "center")

    # Create a label widget for my name :)
    label2 = tk.Label(root, text="By ZainUlWahab", font=("Arial", 12), bg="darkslategray", fg="black")
    label2.place(relx=0.5,rely=0.14,anchor="center")

    # Create a button widget with custom appearance
    button = tk.Button(root, text="Organize Files", command=on_button_click, bg="grey", fg="black", font=("Arial", 12, "bold"), bd=0, padx=20, pady=10)
    button.place(relx=0.5, rely=0.8, anchor="center")

    # Run the Tkinter event loop
    root.mainloop()
if __name__ == "__main__":
    starting_gui()