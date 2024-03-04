# Text Processing Functions

In this assignment, you are tasked with implementing several text processing functions. The functions are defined in the `main.py` file. You should write your implementations in this file, replacing the `pass` statement with your code.

Here are the functions you need to implement:

1. `word_count(path, word)`: This function should take a file path and a word as input, and return the number of times the word appears in the file.

2. `symbol_count(path)`: This function should take a file path as input, and return the total number of non-whitespace characters in the file.

3. `line_count(path)`: This function should take a file path as input, and return the number of lines in the file.

4. `text_without_newlines(path)`: This function should take a file path as input, and return the text of the file as a single string, with all newline characters removed.

5. `text_without(path, to_remove)`: This function should take a file path and a string to remove as input, and return the text of the file as a single string, with all instances of the string to remove deleted.

6. `text_without_punctuation(path)`: This function should take a file path as input, and return the text of the file as a single string, with all punctuation characters removed.

Unit tests for these functions are provided in the `test_main.py` file. You should run these tests to check your work. 
### Please do not modify the tests; they are designed to check if your functions are working correctly, also don't touch the text files themselves.
#### to run the tests you should first install pytest module, using *```pip install pytest```* and the just run *```pytest```* from he terminal.

Good luck!