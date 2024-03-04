import pytest
import random
import string
from main import word_count, symbol_count, line_count, text_without_newlines, text_without, text_without_punctuation


def random_word_from_file(path):
    with open(path, 'r') as file:
        text = file.read()
        words = text.split()
        return random.choice(words)

def test_word_count():
    for path in ['text_1.txt', 'text_2.txt', 'text_3.txt']:
        word = random_word_from_file(path)
        assert word_count(path, word) >= 0

def test_word_count_precise():
    for path in ['text_1.txt', 'text_2.txt', 'text_3.txt']:
        word = random_word_from_file(path)
        with open(path, 'r') as file:
            text = file.read()
            assert word_count(path, word) == text.count(word)

def test_symbol_count():
    for path in ['text_1.txt', 'text_2.txt', 'text_3.txt']:
        assert symbol_count(path) >= 0

def test_line_count():
    for path in ['text_1.txt', 'text_2.txt', 'text_3.txt']:
        assert line_count(path) >= 0

def test_text_without_newlines():
    for path in ['text_1.txt', 'text_2.txt', 'text_3.txt']:
        assert '\n' not in text_without_newlines(path)

def test_text_without():
    for path in ['text_1.txt', 'text_2.txt', 'text_3.txt']:
        to_remove = random.choice(string.punctuation)
        assert to_remove not in text_without(path, to_remove)

def test_text_without_punctuation():
    for path in ['text_1.txt', 'text_2.txt', 'text_3.txt']:
        text = text_without_punctuation(path)
        assert not any(c in string.punctuation for c in text)