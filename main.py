__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files" 
import os
import shutil
import zipfile
import os.path

path = os.getcwd()
CACHE = "cache"
filePath = os.path.join(os.getcwd(), CACHE)
isExist = os.path.exists(path)
def clean_cache():
    if not os.path.exists(filePath):
        os.makedirs(filePath)
    elif os.path.exists(filePath):
          shutil.rmtree(filePath)
          os.mkdir(filePath)

def cache_zip(zip_file_path, cache_dir_path):
    with zipfile.ZipFile(zip_file_path, 'r') as zfile:
        zfile.extractall(cache_dir_path)
        return zfile

def cached_files():
     file_list = [] 
     os.path.abspath('.\cache')
     obj = os.scandir(os.path.abspath('.\cache'))
     for entry in obj:
         file_list.append(entry.path)
     return file_list

def find_password(file_list):
    for file_name in file_list:
        with open(file_name, 'r') as f:
             contents = f.readlines()
             for line in contents:
                 if 'password' in line:
                     return line.strip()[10:]
print(find_password(cached_files()))