import os
import re

directory_path = ''


# Funktion, um Lazy Loading hinzuzufügen
def add_lazy_loading_to_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.read()

    # Regex für img- und video-Tags, die noch kein loading="lazy" haben
    img_regex = r'<img\s+((?!loading\s*=\s*["\']lazy["\']).)*?>'
    video_regex = r'<video\s+((?!loading\s*=\s*["\']lazy["\']).)*?>'

    # Füge loading="lazy" zu img-Tags hinzu
    new_data = re.sub(img_regex, lambda match: match.group(0).replace('<img', '<img loading="lazy"'), data)

    # Füge loading="lazy" zu video-Tags hinzu
    new_data = re.sub(video_regex, lambda match: match.group(0).replace('<video', '<video loading="lazy"'), new_data)

    # Speichere die Änderungen in der Datei
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(new_data)

    print(f'Lazy Loading zu {file_path} hinzugefügt.')

# Funktion, um alle HTML-Dateien im Verzeichnis und Unterverzeichnissen zu durchsuchen
def process_files_in_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                add_lazy_loading_to_file(file_path)

# Starte den Prozess
process_files_in_directory(directory_path)
