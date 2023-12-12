import os 


def file_names(path):

    file_names = [f for f in os.listdir(path) if os.isfile(os.join(path, f))]
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
        with open(name) as f:
            text = f.read(-1)
        text.lower()
        cleaned_file = open("cleaned/" + name, "w")
        cleaned_file.write(text)
        cleaned_file.close()

def clean(file_name):
    with open(file_name, "w") as f:
        text = f.read(-1)
        for l in text:
                if(letter == "'" or letter == "-" or letter == "\n"):
                    letter = " "
                if(letter == "." or letter == "," or letter == "!" or letter == "?"):
                    letter = ""
        text.write(text)


