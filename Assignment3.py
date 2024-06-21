#removing Duplicate character form a sentence
input_sentence = input("Enter the sentence: ")
words = input_sentence.split()
final_result = []
for i in words:
    if i not in final_result:
        final_result.append(i)
final_sentence = ' '.join(final_result)
print(final_sentence)