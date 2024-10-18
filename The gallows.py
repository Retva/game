import random

def choose_word(difficulty):
    words = {
        "easy": ["кот", "кино", "яблоко", "ноутбук", "кровать"],
        "medium": ["процессор", "радиатор", "клавиатура", "интернет", "игра"],
        "hard": ["аттракцион", "демонстрировать", "конвертировать", "доставка", "аденозинтрифосфорнаякислота"]
    }
    return random.choice(words[difficulty])
def display_hangman(tries):
    stages = [
        """
           -----
           |   |
           |   O
           |  /|\\
           |  / \\
           |
        """,
        """
           -----
           |   |
           |   O
           |  /|\\
           |  / 
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |   /
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |
           |
        """,
        """
           ------
           |    |
           |    O
           |    |
           |
           |
        """,
        """
           ------
           |    |
           |    O
           |
           |
           |
        """,
        """
           ------
           |    |
           |
           |
           |
           |
        """,
        """
           ------
           |    
           |
           |
           |
           |
        """
    ]
    return stages[tries]

def play():
    print("Добро пожаловать в игру 'Виселица'!")
    
    difficulty = input("Выберите уровень сложности (easy, medium, hard): ").lower()
    while difficulty not in ["easy", "medium", "hard"]:
        print("Недопустимый выбор. Пожалуйста, выберите easy, medium или hard.")
        difficulty = input("Выберите уровень сложности (easy, medium, hard): ").lower()

    word = choose_word(difficulty)
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6

    print(display_hangman(tries))
    print(word_completion)
    print("n")

    while not guessed and tries > 0:
        guess = input("Введите букву или слово: ").lower()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("Вы уже угадали эту букву:", guess)
            elif guess not in word:
                print(guess, "нет в слове.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Отлично!", guess, "входит в слово!")
                guessed_letters.append(guess)
                word_completion = "".join([letter if letter in guessed_letters else "_" for letter in word])
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("Вы уже пытались угадать это слово:", guess)
            elif guess != word:
                print(guess, "не это слово.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Недопустимый ввод. Попробуйте еще раз.")

        print(display_hangman(tries))
        print(word_completion)
        print("n")

    if guessed:
        print("Поздравляем! Вы угадали слово:", word)
    else:
        print("Вы проиграли. Загаданное слово было:", word)

if __name__ == "__main__":
    play()
