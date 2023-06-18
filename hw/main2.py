import re
from collections import Counter

def count_most_common_words(text, n):
    # Приведение текста к нижнему регистру и удаление знаков препинания
    cleaned_text = re.sub(r'[^\w\s]', '', text.lower())

    # Разделение текста на слова
    words = cleaned_text.split()

    # Подсчет количества встречаемых слов
    word_counts = Counter(words)

    # Возвращение n самых часто встречающихся слов
    most_common_words = word_counts.most_common(n)

    return most_common_words

# Пример текстовой строки (статья из документации Python)
text = """
Computer programming is the process of performing particular computations (or more generally, accomplishing specific computing results), usually by designing and building executable computer programs. Programming involves tasks such as analysis, generating algorithms, profiling algorithms' accuracy and resource consumption, and the implementation of algorithms (usually in a particular programming language, commonly referred to as coding).[1][2] The source code of a program is written in one or more languages that are intelligible to programmers, rather than machine code, which is directly executed by the central processing unit. The purpose of programming is to find a sequence of instructions that will automate the performance of a task (which can be as complex as an operating system) on a computer, often for solving a given problem. Proficient programming thus usually requires expertise in several different subjects, including knowledge of the application domain, specialized algorithms, and formal logic.
"""

# Подсчет 10 самых часто встречающихся слов
most_common_words = count_most_common_words(text, 10)

print("Исходный текст:")
print(text)
print("\n10 самых часто встречающихся слов:")
for word, count in most_common_words:
    print(f"{word}: {count} раз(a)")
