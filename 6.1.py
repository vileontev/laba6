def slovar():
    # Создаем словарь с перечнем стран и их столиц
    countries_capitals = {
        'Россия': 'Москва',
        'США': 'Вашингтон',
        'Китай': 'Пекин',
        'Франция': 'Париж',
        'Германия': 'Берлин',
        'Италия': 'Рим',
        'Япония': 'Токио',
        'Великобритания': 'Лондон',
        'Испания': 'Мадрид',
        'Канада': 'Оттава'
    }

    # a) Выводим все пары ключ-значение
    print("Пары ключ-значение (Страна : Столица):")
    for country, capital in countries_capitals.items():
        print(f"{country} : {capital}")

    # b) Выводим столицу для определенной страны
    country_to_lookup = 'Франция'
    if country_to_lookup in countries_capitals:
        print(f"Столица страны {country_to_lookup}: {countries_capitals[country_to_lookup]}")
    else:
        print(f"Страна {country_to_lookup} не найдена в словаре.")

    # c) Сортируем и выводим содержимое словаря по алфавиту названий стран
    sorted_countries = sorted(countries_capitals.keys())
    print("\nСодержимое словаря, отсортированное по алфавиту стран:")
    for country in sorted_countries:
        print(f"{country} : {countries_capitals[country]}")

slovar()
