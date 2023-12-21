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


def tf_idf_question(question, files):
    tf_doc = {}
    for file in files:
        with open(file, encoding= "utf-8") as f:
            tf_file = ti.tf_counter(file)
            for w in tf_file.keys():
                if w in tf_doc.keys():
                    tf_doc[w] += tf_file[w]
                else:
                    tf_doc[w] = tf_file[w]
    tf = tf_question(question, tf_doc)
    idf = ti.idf_counter(files)
    tf_idf = []
    for w in tf:
            tf_idf.append(tf[w] * idf[w])
    return tf_idf

def scalar_product(v1, v2):
    scalar = 0
    for i in range(len(v1)):
        scalar += (v1[i] * v2[i])
    return scalar

def get_norm(v):
    norm = 0
    for i in range(len(v)):
        norm = v[i] ** 2
    return math.sqrt(norm)

def similarity(v1, v2):
    if get_norm(v1) == 0 or get_norm(v2) == 0:
        return 0
    return scalar_product(v1,v2)/(get_norm(v1) * get_norm(v2))

def most_relevant(matrix, vector, files):
    most_relevant = 0
    for i,v in enumerate(matrix):
        if similarity(v, vector) > similarity(vector, matrix[most_relevant]): 
            most_relevant = i
    return files[most_relevant]

def answer(question, files, doc_matrix):
    maxi = 0
    idf_corpus = list(ti.idf_counter(files))
    tf_idf = tf_idf_question(question, files)
    for value in tf_idf:
        if value > maxi:
            maxi = value
    answer = ""
    first_occ = 0
    start_sent = 0
    end_sent = 0
    final_answer = ""
    with open(most_relevant(doc_matrix, tf_idf, files), "r", encoding="utf-8") as f1:
        texte = f1.read().split()
        while texte[first_occ] != idf_corpus[tf_idf.index(maxi)]:
            first_occ += 1
        ponctuation = [".", "!", "?"]
        for i in range(first_occ, 0, -1):
            if texte[i-1][-1] in ponctuation and start_sent == 0 :
                start_sent = i
        for i in range(first_occ, len(texte), 1):
            if texte[i].split("\n")[0][-1] in ponctuation and end_sent == 0:
                end_sent = i
        for i in range(start_sent, end_sent, 1):
            answer += texte[i] + " "
        answer += texte[end_sent].split("\n")[0]
        answer = chr(ord(answer[0])+32)+answer[1:]

    starters = {
        "Comment": "Après analyse, ",
        "Pourquoi": "Car, ",
        "Peux-tu": "Oui, bien sûr! "
    }

    for i in starters:
        if question[0] == i:
            final_answer = starters[i]+answer
            break
    if final_answer != "":
        return(final_answer)
    else:
        return(answer)
"""    
def highest_score(words, files):
    highest = words[0]
    highest_score = tf_idf_question(words[0])
    for word in words:
        w_tf_idf = tf_idf(word)
        if w_tf_idf > highest_score:
        highest = word

def generate_answer(question, files, doc_matrix):
    highest = highest_score(question, files)
    question_matrix = tf_idf_question(question, files)
    most_relevant = most_relevant(doc_matrix, question_matrix, files)
    first_occ = 0
    tf_question = 
    with open(most_relevant, "r", encoding="utf-8") as f:
        text = f.read.split(" ")
        for w in text:
            tf_
"""
