# Word Counter Analyzer

Counts total words, unique words, and individual word frequencies in a line of text. It matches words without regard to case, treats Unicode punctuation as a separator, and removes straight and curly apostrophes so contractions count as a single word.

## Run

```sh
python3 WordCounter_Analyzer.py
```

Enter text when prompted. For example, `Hello, world! HELLO.` yields three words and two unique words, with `hello` appearing twice. The script uses the Python standard library.
