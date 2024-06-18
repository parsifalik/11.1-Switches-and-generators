# Напишите генераторное выражение, которое возвращает буквы строки "hello", но только если они являются гласными.
vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

vowels_ = list(x for x in "hello" if x in vowels)
print(vowels_)