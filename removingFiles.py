import time
import os
import shutil

def main():
    deletedFoldersCount=0
    deletedFilesCount=0
    path="path to delete"
    days=30
    seconds=time.time()-(days*24*60*60)
    if os.path.exists(path):
        for route_folder, folders, files in os.walk(path):
            if seconds>=get_file_folder_age(route_folder):
                remove_folder(route_folder)
                deletedFoldersCount+=1
                break
            else:
                for folder in folders:
                    folder_path=os.path.join(route_folder, folder)
                    if seconds>=get_file_folder_age(folder_path):
                        remove_folder(folder_path)
                        deletedFoldersCount+=1
                for file in files:
                    file_path=os.path.join(route_folder, file)
                    if seconds>=get_file_folder_age(file_path):
                        remove_file(file_path)
                        deletedFilesCount+=1
            else:
                if seconds>=get_file_folder_age(path):
                    remove_file(path)
                    deletedFilesCount+=1
    else:
        print(f'"{path}"is not found')
        deletedFilesCount+=1
    print(f"totalFoldersDeleted:{deletedFoldersCount}")
    print(f"totalFilesDeleted:{deletedFilesCount}")

def remove_folder(path):
    if not shutil.rmtree(path):
        print(f"{path}is removed successfully")
    else:
        print(f"unable to delete"+path)

def remove_file(path):
    if not os.remove(path):
        print(f"{path}is removed successfully")
    else:
        print(f"unable to delete"+path)

def get_file_folder_age(path):
    ctime=os.stat(path).st_ctime
    return ctime

if __name__=='__main__':
    main()

