import os
import shutil
import subprocess
#KXRIM
#GITHUB REPO: https://github.com/KerYagciHTL/Commit-Spammer
file_name = input("Gib den Dateinamen ein: ").strip()
if not os.path.exists(file_name):
    print(f"Datei '{file_name}' existiert nicht. Beende das Programm.")#KXRIM
    exit()
#KXRIM
try:#KXRIM
    num_commits = int(input("Wie viele Commits sollen erstellt werden: ").strip())
    commits_per_file = round(num_commits // 2)
except ValueError:#KXRIM
    print("Ungültige Eingabe. Bitte eine Zahl eingeben.")
    exit()#KXRIM
#KXRIM
message = input("Commit Nachricht: ")
backup_dir = "backup"
os.makedirs(backup_dir, exist_ok=True)
#KXRIM
for _ in range(commits_per_file):
    backup_path = os.path.join(backup_dir, os.path.basename(file_name))
    shutil.copy(file_name, backup_path)
    subprocess.run(["git", "rm", file_name], check=True)
    subprocess.run(["git", "commit", "-m", message], check=True)
    shutil.copy(backup_path, file_name)
    subprocess.run(["git", "add", file_name], check=True)
    subprocess.run(["git", "commit", "-m", message], check=True)
#KXRIM
subprocess.run(["git", "push", "--force"], check=True)
shutil.rmtree(backup_dir)#KXRIM
#KXRIM
print("Commit process completed.")
input("Press...")#KXRIM

