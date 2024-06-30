import random
from urllib.request import urlopen

# Simplified URL and word list
WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

# Reintegrated full phrases dictionary
PHRASES = {
    "class %%%(%%%):":
        "「%%%という名前のクラスを作り、このクラスは%%%クラスを継承する」",
    "class %%%(object):\n\tdef __init__(self, ***)":
        "「%%%クラスは、 __init__ 関数を持つ。この関数のパラメータはselfと***だ。」",
    "class %%%(object):\n\tdef ***(self, @@@)":
        "「%%%クラスは、***という名前の関数を持つ。この関数のパラメータはselfと@@@だ。」",
    "*** = %%%()":
        "「***変数に%%%クラスのインスタンスを設定する。」",
    "***.***(@@@)":
        "「***の関数である***をselfと @@@を引数にして呼び出す。」",
    "***.*** = '***'":
        "「***の属性である***に***を設定する。」"
}

# Load words from the website
words_content = urlopen(WORD_URL).read().decode('utf-8')
WORDS = words_content.strip().splitlines()

def convert(snippet):
    class_names = [random.choice(WORDS).capitalize() for _ in range(snippet.count("%%%"))]
    other_names = [random.choice(WORDS) for _ in range(snippet.count("***"))]
    params = [','.join(random.sample(WORDS, random.randint(1, 3))) for _ in range(snippet.count("@@@"))]

    phrase = PHRASES[snippet]

    # Replace placeholders
    for word in class_names:
        snippet = snippet.replace("%%%", word, 1)
        phrase = phrase.replace("%%%", word, 1)
    for word in other_names:
        snippet = snippet.replace("***", word, 1)
        phrase = phrase.replace("***", word, 1)
    for param in params:
        snippet = snippet.replace("@@@", param, 1)
        phrase = phrase.replace("@@@", param, 1)

    return snippet, phrase

# Interactive quiz
try:
    while True:
        snippet = random.choice(list(PHRASES.keys()))
        question, answer = convert(snippet)
        print("質問:", question)
        input("> ")
        print(f"答え: {answer}\n\n")
except EOFError:
    print("\nさようなら")
