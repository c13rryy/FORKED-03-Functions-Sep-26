def most_common_word(text):
    text = convert_text(text)
    count_words = {}
    # max_counted_word = ""

    # count_words = [[el, text.count(el)] for el in text]
    # count_words = [tuple(el) for el in count_words]
    # count_words = set(count_words)

    for word in text:
        if word in count_words:
            count_words[word] += 1
        else:
            count_words[word] = 1

    # for key in count_words.keys():
    #     if len(max_counted_word) == 0:
    #         max_counted_word = key

    #     if count_words[max_counted_word] < count_words[key]:
    #         max_counted_word = key

    return max(count_words, key=count_words.get)


def convert_text(text):
    text = text.lower()
    lst = text.split(" ")
    punctuation_marks = "!,?.:;"

    for el in range(len(lst)):
        for mark in punctuation_marks:
            if mark in lst[el]:
                lst[el] = lst[el].strip(mark)

    return lst


assert most_common_word("кот кот собака") == "кот", "Самое частое слово — кот"
assert most_common_word("Кот кот КОТ собака") == "кот", "Регистр должен игнорироваться"
assert most_common_word("молоко, молоко! молоко? хлеб.") == "молоко", "Знаки препинания должны игнорироваться"
assert most_common_word("слово") == "слово", "Ожидалось единственное слово"
res = most_common_word("а б а б")
assert res in ("а", "б"), "Ожидалось одно из слов с максимальной частотой"
