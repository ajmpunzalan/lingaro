# Write a method which repeat words in string 'index' times. Do it 'pythonic way'.
def repeat_string(text):
    """
    Repeat words in string 'index' times :param text: string with words to repeat 
    :return: modified text
    Example:
    repeat_string('Welcome to Warsaw !') 
    ' to WarsawWarsaw !!!'
    """
    list_text = text.split()
    new_text = []
    for n, text in enumerate(list_text):
        new_text.append(text * n)

    return " ".join(new_text)


print(repeat_string('Welcome to Warsaw !'))
