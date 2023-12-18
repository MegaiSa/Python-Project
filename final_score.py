import read_file as rf
import tf_idf as ti
import os


def get_matrix(files):
    idf = ti.idf_counter(files)
    tf_idf_matrice = []
    for file in files:
        tf = ti.tf_counter(file)
        doc_matrice = []
        for w in idf.keys():
            if w in tf.keys():
                doc_matrice.append((idf[w] * tf[w]))
            else:
                doc_matrice.append(0)
        tf_idf_matrice.append(doc_matrice)
    return tf_idf_matrice

if __name__ == "__main__":
    files = rf.file_names("speeches")
    rf.convert_files(files)
    os.chdir("cleaned")
    for f in files:
        rf.clean(f)
    matrice = get_matrix(files)
    size = 0
    for i in matrice:
        print(len(i))
