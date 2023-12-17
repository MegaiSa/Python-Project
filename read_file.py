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


def convert(file_list):
    for name in file_list:
        with open(name, encoding = "utf-8") as f:
            text = f.read()
            for i,l in enumerate(text):
                if ord('A') <= ord(l) <= ord('Z'):
                    text[i].lower()
        cleaned_file = open(name, "r+", encoding = "utf-8")
        cleaned_file.write(text)
        cleaned_file.close()

def clean(file_name):
    with open(file_name, "a+", encoding = "utf-8") as f:
        text = f.read()
        for l in text:
                if(letter == "'" or letter == "-" or letter == "\n"):
                    letter = " "
                if(letter == "." or letter == "," or letter == "!" or letter == "?"):
                    letter = ""
        f.write(text)


