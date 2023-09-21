eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюяабвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

todo = input('What are we gonna do?: ').lower()
while todo != 'cipher' and todo != 'decipher':
    todo = input(('Input "cipher" or "decipher" \n'))
language = input('Choose language -  russian/english: ').lower()
while language != 'english' and language != 'russian':
    language = input(('Write "russian" or "english" \n'))
step = input('Choose the amount of symbols - digit: ')
while not step.isdigit():
    step = input('Write number \n')
if todo == 'cipher':
    user_text = input('Write a text to cipher: ')
elif todo == 'decipher':
    user_text = input("Write a text to decipher: ")
while user_text.isdigit() or user_text.isspace() or user_text == '':
    user_text = input(('You should write a text \n'))


def caesar(action, lang, cystep, text):
    place = 0
    for i in range(len(text)):
        if lang == 'russian':
            alphas = 32
            low_alpha = rus_lower_alphabet
            upper_alpha = rus_upper_alphabet
        elif lang == 'english':
            alphas = 26
            low_alpha = eng_lower_alphabet
            upper_alpha = eng_upper_alphabet
        if text[i].isalpha():
            if text[i] == text[i].lower():
                place = low_alpha.find(text[i])
            if text[i] == text[i].upper():
                place = upper_alpha.find(text[i])
            if action == 'decipher':
                index = (place - int(cystep)) % alphas
            elif action == 'cipher':
                index = (place + int(cystep)) % alphas

            if text[i] == text[i].lower():
                print(low_alpha[index], end='')
            elif text[i] == text[i].upper():
                print(upper_alpha[index], end='')
        else:
            print(text[i], end='')


caesar(todo, language, step, user_text)
