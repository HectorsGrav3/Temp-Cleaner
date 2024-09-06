import os
import shutil
import glob

def delete_files(directory):
    # Get all files and folders in the directory
    files = glob.glob(os.path.join(directory, "*"))
    
    for file in files:
        try:
            if os.path.isfile(file) or os.path.islink(file):
                os.remove(file)
            elif os.path.isdir(file):
                shutil.rmtree(file)
        except Exception as e:
            print(f"{file} Cannot be deleted because its used by another process")

# Delete files in the Recent folder
recent_path = os.path.join(os.environ['USERPROFILE'], 'Recent')
delete_files(recent_path)

# Delete files in the Prefetch folder
prefetch_path = r'C:\Windows\Prefetch'
delete_files(prefetch_path)

# Delete files in the Temp folder
temp_windows_path = r'C:\Windows\Temp'
delete_files(temp_windows_path)

# Delete files in the user's local Temp folder
user_temp_path = os.path.join(os.environ['USERPROFILE'], 'AppData', 'Local', 'Temp')
delete_files(user_temp_path)

input("Press Enter to continue...")
