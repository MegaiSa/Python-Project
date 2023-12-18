import os 


def file_names(path):

    file_names = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    return file_names

def associate_first_name(name):

    presidents_names ={
        "Giscard d'Estaing": "Valéry Giscard d'Estaing",
        "Mitterrand": "François Mitterand",
        "Chirac": "Jacques Chirac",
        "Sarkozy": "Nicolas Sarkozy",  
        "Macron": "Emmanuel Macron"
    }
    return presidents_names[name]

def convert(file):
    with open("speeches/" + file, "r", encoding= "utf-8") as f:
        text = f.read(-1)
    with open("cleaned/" + file, "w", encoding= "utf-8") as f:
        f.write(text.lower())

def convert_files(file_list):
    for file in file_list:
        convert(file)

def clean(file_name):
    with open(file_name, "r", encoding = "utf-8") as f:
        text = f.read()
    cleaned = ""
    for letter in text:
            if(letter == "'" or letter == "-" or letter == "\n"):
                cleaned += " "
            elif(letter == "." or letter == "," or letter == "!" or letter == "?"):
                cleaned += ""
            else:
                cleaned += letter
    with open(file_name, "w", encoding = "utf-8") as f:
        f.write(cleaned)


