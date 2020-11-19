def found_vowels(word: str) -> set:
    """Выводит все гласные на экран """
    vowels = set('aeiou')
    return vowels.intersection(set(word))


def search_for_letters(phrase: str, letters: str = 'aeiou') -> set:
    """Осуществляет поиск заданных букв во введенном слове"""
    return set(letters).intersection(set(phrase))
