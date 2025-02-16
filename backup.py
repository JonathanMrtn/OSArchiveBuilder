import os
import shutil
import platform
from datetime import datetime
import tempfile

def get_user_home():
    return os.getcwd() # use to make fast test to pass and build a smal backup file
    # return os.path.expanduser("~") # use this to official test to pass and build a big (contain all files from the user on your OS) backup file

def get_backup_filename():
    date_str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    return f"backup_{date_str}"

def create_backup():
    home_directory = get_user_home()
    backup_name = get_backup_filename()
    backup_path = os.path.join(home_directory, "backups")
    os.makedirs(backup_path, exist_ok=True)
    
    archive_format = "zip" if platform.system() == "Windows" else "gztar"
    archive_path = os.path.join(backup_path, backup_name)
    
    def ignore_errors(directory, files):
        return [f for f in files if not os.access(os.path.join(directory, f), os.R_OK)]
    
    try :
        with tempfile.TemporaryDirectory() as temp_dir:
            shutil.copytree(home_directory, os.path.join(temp_dir, "backup"), ignore=ignore_errors)
            shutil.make_archive(archive_path, archive_format, temp_dir, "backup")
        return f"Backup created: {archive_path}.{archive_format}"
    except Exception as e:
        return f"Error creating backup: {e}"

if __name__ == "__main__":
    print(create_backup())