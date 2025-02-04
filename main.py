alphabet = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
    'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y', 'Z'
]

morse_alphabet = [
    '.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---',
    '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-',
    '..-', '...-', '.--', '-..-', '-.--', '--..'
]


converted_word = []

user_input = input(f"Enter word here: ")


for letter in user_input.upper():
    if letter in alphabet:
        alphabet_index = alphabet.index(letter)
        morse_index = morse_alphabet[alphabet_index]

        converted_word.append(morse_index)

    elif letter == " ":
        converted_word.append(" / ")

    else:
        converted_word.append(" ERR ")

print(f"{user_input} = {' '.join(converted_word)}")
