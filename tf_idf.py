import read_file as rf
import math 
import os

def tf_counter(file):
    tf_counter = {}
    with open(file, "r", encoding= "utf-8") as f:
        text = f.read().replace("\n", " ").split(" ")
    for word in text:
        if word in tf_counter.keys():
            tf_counter[word] += 1
        else:
            tf_counter[word] = 1
    return tf_counter


def idf_counter(files):
    nb_appearance = {}
    idf_counter = {}
    for f in files:
        tf = tf_counter(f)
        for w in tf.keys():
            if w in nb_appearance.keys():
                nb_appearance[w] += 1
            else: 
                nb_appearance[w] = 1
    for m in nb_appearance.keys():
        idf_counter[m] = math.log10(len(files)/nb_appearance[m])
    return idf_counter



if __name__ == "__main__":
    files = rf.file_names("speeches")
    rf.convert_files(files)
    os.chdir("cleaned")
    for f in files:
        rf.clean(f)
    print(idf_counter(files))



    
