sentence = input()

word_char_count = {word:len(word) for word in sentence.split(' ')}
print(word_char_count)