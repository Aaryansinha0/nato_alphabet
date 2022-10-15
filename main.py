
import pandas

phonetic_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dic = {row.letter: row.code for (index, row) in phonetic_alphabet.iterrows()}

def new_word():
      word_input = input("Enter a word: ").upper()
      final_list = [phonetic_dic[letter] for letter in word_input]
      print(final_list)

new_word()
again = True
while again:
  if input("Do you want to run again? y for yes or n for no \n").lower() == "y":
    new_word()
  else:
    again = False
    print("Have a good day!")
    
