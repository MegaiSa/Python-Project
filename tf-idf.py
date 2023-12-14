import read_file as rf
import math as m
import os

def tf_idf(directory):

    files = rf.file_names(directory)
    old_dir = os.getcwd()
    os.chdir(directory)
    rf.convert(files)
    os.chdir(old_dir)
    os.chdir("cleaned")
    for f in files:
        rf.clean(f)
    idf_counter = {}
    for file in files:
        with open(file, "r") as f:
            text = f.read()
        text.split(" ")
        for word in text:
            if word in idf_counter.keys():
                idf_counter[word] += 1
            else:
                idf_counter[word] = 1
    for w in idf_counter.keys():
        idf_counter[w] = 1/m.log(idf_counter[w])
    return idf_counter

if __name__ == "__main__":
    print(tf_idf("speeches"))

    
