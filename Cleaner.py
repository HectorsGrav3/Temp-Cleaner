import os
import sys
import platform
import ctypes

def is_admin():
    if platform.system() == "Windows":
        try:
            return ctypes.windll.shell32.IsUserAnAdmin() != 0
        except AttributeError:
            return False
    elif platform.system() == "Linux" or platform.system() == "Darwin":
        return os.geteuid() == 0
    else:
        return False

def delete_file(file_path):
    try:
        os.remove(file_path)
        print(f"Deleted: {file_path}")
    except PermissionError:
        print(f"Access denied: {file_path}")
    except OSError as e:
        print(f"Error occurred while deleting {file_path}: {e}")

if is_admin():
    # Clearing Recent folder
    recent_folder = os.path.join(os.environ['userprofile'], 'Recent')
    for root, dirs, files in os.walk(recent_folder):
        for file in files:
            file_path = os.path.join(root, file)
            delete_file(file_path)

    # Clearing Prefetch folder
    prefetch_folder = 'C:\\Windows\\Prefetch'
    for file in os.listdir(prefetch_folder):
        file_path = os.path.join(prefetch_folder, file)
        delete_file(file_path)

    # Clearing Windows Temp folder
    windows_temp_folder = 'C:\\Windows\\Temp'
    for file in os.listdir(windows_temp_folder):
        file_path = os.path.join(windows_temp_folder, file)
        delete_file(file_path)

    # Clearing User Temp folder
    user_temp_folder = os.path.join(os.environ['USERPROFILE'], 'appdata', 'local', 'temp')
    for file in os.listdir(user_temp_folder):
        file_path = os.path.join(user_temp_folder, file)
        delete_file(file_path)

    input("Cleaning completed. Press Enter to exit...")
else:
    print("Please run the script as an administrator to perform the cleaning operation.")
    input("Press Enter to exit...")

