import read_file as rf
import math 
import os

def tf_counter(file):
    tf_counter = {}
    with open(file, "r", encoding= "utf-8") as f:
        text = f.read().split(" ")
    for word in text:
        if word in tf_counter.keys():
            tf_counter[word] += 1
        else:
            tf_counter[word] = 1
    return tf_counter


def idf_counter(directory):

    nb_appearance = {}
    idf_counter = {}
    files = rf.file_names(directory)
    rf.convert_files(files)
    os.chdir("cleaned")
    for f in files:
        rf.clean(f)
        tf = tf_counter(f)
        for w in tf.keys():
            if w in nb_appearance.keys():
                nb_appearance[w] += 1
            else: 
                nb_appearance[w] = 1
            if w in idf_counter.keys():
                idf_counter[w] += tf[w]
            else:
                idf_counter[w] = tf[w]
    for m in idf_counter.keys():
        idf_counter[w] = math.log10(len(files)/nb_appearance[w])
    return idf_counter



if __name__ == "__main__":
    print(idf_counter("speeches"))



    
