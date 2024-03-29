import os
import shutil

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

files = [f for f in os.listdir() if not f.startswith('.')]  # Exclude hidden files

# Loop which runs till every file is not in its designated folder
for file in files:
    if os.path.isfile(file):
        _,ext = os.path.splitext(file)
        folder_name = make_folder_name(ext[1:].lower())
        if not os.path.exists(folder_name):
            os.mkdir(folder_name)
        shutil.move(file,folder_name)


