import os
import read_file as rf
import tf_idf as ti
import final_score as fs
import menu

def main():
    files = rf.file_names("speeches")
    rf.convert_files(files)
    os.chdir("cleaned")
    for f in files:
        rf.clean(f)
    matrix = fs.get_matrix(files)
    menu.menu(files, matrix)

if __name__ == "__main__":
    main()