

import pandas
df = pandas.read_csv('nato_phonetic_alphabet.csv')


alphabet_dictionary = {row.letter:row.code for (index, row) in df.iterrows()}
print(alphabet_dictionary)

def generate_phonetic():
  word = input("Enter a word: ").upper()
  try:
      output = [alphabet_dictionary[letter] for letter in word]
      
  except KeyError:
      print("Sorry Only letters in the alphabets only")
      generate_phonetic()
  
  else:
    print(output)


generate_phonetic()

  


