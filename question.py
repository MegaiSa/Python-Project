import tf_idf as ti
import math 

def clean_question(question):
    cleaned = ""
    question = question.lower()
    for letter in question:
            if(letter == "'" or letter == "-" or letter == "\n"):
                cleaned += " "
            elif(letter == "." or letter == "," or letter == "!" or letter == "?"):
                cleaned += ""
            else:
                cleaned += letter
    return cleaned.split(" ")

def is_in_corpus(word_list, directory = "cleaned"): 
    corpus_words = ti.idf_counter(directory)
    words = []
    for w in word_list:
        if w in corpus_words.keys():
             words.append(w)
    return words

def tf_question(question, doc_tf):
    tf_counter = {}
    for w in doc_tf.keys():
        if (w in question) and (w in tf_counter.keys()):
            tf_counter[w] += 1
        elif (w in question) and not(w in tf_counter.keys()):
            tf_counter[w] = 1
        else:
            tf_counter[w] = 0
    return tf_counter

def idf_question(question, doc_idf):
    idf_counter = {}
    for w in question:
        if not(w in idf_counter.keys()):
            idf_counter[w] = doc_idf[w]
    return idf_counter

def tf_idf_question(question, doc_tf, doc_idf):
    cleaned = clean_question(question)
    tf_idf = []
    tf = tf_question(cleaned, doc_tf)
    idf = idf_question(cleaned, doc_idf)
    for w in tf:
        if ( tf[w] * idf[w]) : tf_idf.append(tf[w] * idf[w])
    return tf_idf

def scalar_product(v1, v2):
    scalar = 0
    for i in range(len(v1)):
        scalar += (v1[i] * v2[i])
    return scalar

def get_norm(v):
    norm = 0
    for i in range(len(v)):
        norm = v[i] ^ 2
    return math.sqrt(norm)

def similarity(v1, v2):
    return scalar_product(v1,v2)/(get_norm(v1) * get_norm(v2))

def most_relevant(matrix, vector, files):
    most_relevant = 0
    for i,v in enumerate(matrix):
        if similarity(v, vector) > similarity(vector, matrix[most_relevant]): most_relevant = i
    return files[most_relevant]

