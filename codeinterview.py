import unittest
# Write method that will count number of words in the string: xx

# e.g.

# "Just some words" --> 3
# "Just some   words" --> 3
# "Still some words  " --> 3


# No String manipulation methods, use only char array manipulation allowed
def count_words(sentence):
    word_count = 0
    for word in range(len(sentence)):
        if sentence[word] == " ":
            word_count += 1
        else:
            continue
    return word_count


class Tests(unittest.TestCase):
    data = [
        ("I am a programmer",4),
        ("I love Cooding ", 3)]


def test_count_words(self):
    for tests in self.data:
        sentence, exp_output = tests
        real_output = count_words(sentence)
        print("exp out:{}, real output:{}" .format(exp_output, real_output))
        self.assertEqual(real_output, exp_output)


if __name__ == "__main__":
    unittest.main()
