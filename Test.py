import os

file_count = 0
folder_count = 0

def list_files(directory, indent=""):
    global file_count
    global folder_count
    try:
        items = os.listdir(directory)

        for i, item in enumerate(items):
            path = os.path.join(directory, item)
            if os.path.isfile(path):
                if i == len(items) - 1:
                    print(f"{indent}└─ Datei: {item}")
                else:
                    print(f"{indent}├─ Datei: {item}")
                file_count += 1
            elif os.path.isdir(path):
                if i == len(items) - 1:
                    print(f"{indent}└─ Ordner: {item}")
                else:
                    print(f"{indent}├─ Ordner: {item}")
                folder_count += 1
                list_files(path, indent + "│  ")

    except PermissionError as e:
        print(f"{indent}Fehler beim Zugriff auf {directory}: {str(e)}")

input_path = input("Version 1\nBitte gib den Pfad zum Ordner an: ")

try:
    list_files(input_path)
except Exception as e:
    print(f"Fehler beim Durchsuchen des Ordners: {str(e)}")

print(f"\nDurchsuchte Dateien: {file_count}")
print(f"Durchsuchte Ordner: {folder_count}")

input("Drücke Enter, um das Programm zu beenden.")
