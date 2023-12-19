import question as q
import os 
import read_file as rf
import final_score as fs


def menu(files, doc_matrix):
    welcome = """
            Welcome
          [1] : Enter ChatBot mode : Ask your own question and get approximative answers !
          [2] : Close 
          
          """
    print(welcome)
    while True:
        choice = int(input())
        if choice == 1:
            question = input("Enter a question: ")
            question = q.clean_question(question)
            print(q.answer(question, files, doc_matrix))
            print()
        elif choice == 2:
            break
        else:
            print("Enter a valid number")