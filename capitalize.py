# Question 4: Capitalize Words
def capitalize_words(sentence):
    return ' '.join(word.capitalize() for word in sentence.split())

input_string = input("Enter a sentence: ")
capitalized_result = capitalize_words(input_string)
print(f"For input '{input_string}', the program returns '{capitalized_result}'.")
