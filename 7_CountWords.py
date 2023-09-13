def count_words(sentence):
    words = sentence.split()
    word_count = {}
    for word in words:
        word = word.lower()
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

print(count_words("This is a test. This is only a test."))
