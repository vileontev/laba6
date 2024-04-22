def calculate_word_score(word):
    # Словарь с буквами и их значениями в очках
    letter_scores = {
        'А': 1, 'В': 1, 'Е': 1, 'И': 1, 'Н': 1, 'О': 1, 'Р': 1, 'С': 1, 'Т': 1,
        'Д': 2, 'К': 2, 'Л': 2, 'М': 2, 'П': 2, 'У': 2,
        'Б': 3, 'Г': 3, 'Ё': 3, 'Ь': 3, 'Я': 3,
        'Й': 4, 'Ы': 4,
        'Ж': 5, 'З': 5, 'Х': 5, 'Ц': 5, 'Ч': 5,
        'Ш': 8, 'Э': 8, 'Ю': 8,
        'Ф': 10, 'Щ': 10, 'Ъ': 10
    }

    # Преобразуем слово к верхнему регистру для унификации
    word = word.upper()

    total_score = 0
    for letter in word:
        if letter in letter_scores:
            total_score += letter_scores[letter]
        else:
            print(f"Буква '{letter}' не имеет значения в игре Эрудит и будет пропущена.")

    return total_score

def erudit():
    # Запрашиваем у пользователя ввод слова
    word = input("Введите слово для подсчета очков: ")

    # Вычисляем и выводим стоимость слова (очки)
    word_score = calculate_word_score(word)
    print(f"Стоимость слова '{word}' в игре Эрудит: {word_score} очков.")

erudit()
