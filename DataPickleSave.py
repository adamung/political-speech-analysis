import os
import pickle
import re
import string
from Anforande import Anforande  

stop_words = []
alla_anforanden = []
#fel = 0

with open("Common_words.txt", "r", encoding='utf-8') as stop_word_file:
     for word in stop_word_file:
          stop_words.append(word.strip())


def clean_text(text):

        pattern = r'<.*?>'
        text = re.sub(pattern, '', text)

        translation_table = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
        text = text.translate(translation_table)

        text = text.lower()


        filtered_words = [word for word in text.split() if word.lower() not in stop_words]

        cleaned_text = ' '.join(filtered_words)

        return cleaned_text

def extract_info_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        
        first_line = file.readline().strip()
        
        parts = first_line.split('(')

        if len(parts) >= 2:
            name = ''.join(parts[0].split(' ', 2)[2]).strip()

            party = parts[1].split(')')[0]

            names = name.split()
            if ("rådet" in names[0] or "minister" in names[0]):
                names.pop(0)
            name = ' '.join(names).upper()

            speech = file.read()

            cleaned_speech = clean_text(speech)
            year = file_path.split(".text")[0][-4:]
            year = year[:2] + "/" + year[2:]
        else:
            print(parts)
            raise ValueError("Felaktig data i filen, filen är förmodligen inget anförande från ett parti.")
        
        return name, party, cleaned_speech, year


# folder_path = "anforande-202223.text"

base_folder = "Anforanden"

for year_folder in os.listdir(base_folder):
     year_folder_path = os.path.join(base_folder, year_folder)

     if os.path.isdir(year_folder_path):
          for filename in os.listdir(year_folder_path):
               if filename.endswith(".txt"):
                    file_path = os.path.join(year_folder_path, filename)
                    try:
                        name, party, speech, year = extract_info_from_file(file_path)
                        if party != "-":
                            party = party.upper()
                            if party == "FP":
                                 party = "L"
                            anforande = Anforande(file_path, party, name, speech, year)
                            alla_anforanden.append(anforande)
                    except ValueError as e:
                         #fel += 1
                         #print(fel)
                         print("Ett fel uppstod:", e)
                    # print("Namn:", name)
                    # print("Parti:", party)
                    # print("Anförande:", speech)
                    # print("----------")

"""
# Loopa igenom alla filer i mappen
for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):

        file_path = os.path.join(folder_path, filename)

        name, party, speech = extract_info_from_file(file_path)

        if name != "Felaktig data":
            anförande = Anforande(file_path, party, name, speech)
            alla_anföranden.append(anförande)
        # print("Namn:", ' '.join(name))
        # print("Parti:", party)
        # print("Anförande:", speech)
        # print("----------")
"""


""" -------------------------------------------- """
""" Kod för att läsa in en enstaka txt-fil"""
# file_path = "Anforanden/anforande-201112.text/GZ094-3.txt"

# name, party, speech = extract_info_from_file(file_path)

# print("Namn:", name)
# print("Parti:", party)
# print("Anförande:", speech)
""" -------------------------------------------- """





pickle_sökväg = "anforanden.pickle"
with open(pickle_sökväg, "wb") as fil:
    pickle.dump(alla_anforanden, fil)