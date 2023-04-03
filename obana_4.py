import random
import string

def get_valid_word(words):
    words = random.choice(words)
    while '_' in word or ' ' in word:
        word = random.choiсe(words)
    return word

def func():
    word = get_valid_word(words)
    word_letters = random = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    while len(word_letters) > 0:
        print("Мы применяем эти буквы: ", " ".join(used_letters))
        word_list = (letter if letter in used_letters else "-" for letter in word)
        print("Текущее слово : ", " ".join(word_list))
        user_letter = input("Напишите письмо : ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

        elif user_letter in used_letters:
            print("Этот персонаж уде используется.Попробуйте еще раз")

        else:
            print("Некорректнй персонаж.Попробуйте еще раз")
