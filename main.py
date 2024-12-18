import os
import shutil
import subprocess

file_list = []
while True:
    file_name = input("Gib den Dateinamen ein (oder 'q' zum Starten): ").strip()
    if file_name.lower() == 'q':
        break
    if os.path.exists(file_name):
        file_list.append(file_name)
    else:
        print(f"Datei '{file_name}' existiert nicht. Überspringe.")

if not file_list:
    print("Keine Dateien vorhanden. Beende das Programm.")
    exit()

try:
    num_commits = int(input("Wie viele Commits sollen erstellt werden? ").strip())
except ValueError:
    print("Ungültige Eingabe. Bitte eine Zahl eingeben.")
    exit()

backup_dir = "backup"
os.makedirs(backup_dir, exist_ok=True)

for i in range(num_commits):
    print(f"Starte Commit-Runde {i + 1} von {num_commits}...")
    for file_name in file_list:
        backup_path = os.path.join(backup_dir, os.path.basename(file_name))
        shutil.copy(file_name, backup_path)
        print(f"{file_name} wurde gesichert.")

        subprocess.run(["git", "rm", file_name], check=True)
        print(f"{file_name} wurde aus dem Repository entfernt.")

        subprocess.run(["git", "commit", "-m", f"Entferne {file_name} - Commit {i + 1}"], check=True)
        print(f"Entfernen von {file_name} committed.")

        shutil.copy(backup_path, file_name)
        subprocess.run(["git", "add", file_name], check=True)
        subprocess.run(["git", "commit", "-m", f"Füge {file_name} hinzu - Commit {i + 1}"], check=True)
        print(f"{file_name} wurde wieder hinzugefügt und committed.")

subprocess.run(["git", "push"], check=True)

shutil.rmtree(backup_dir)
print("Commit-Spam abgeschlossen.")
