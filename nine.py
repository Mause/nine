import random
from typing import List, Dict, Set
from collections import defaultdict
from english_words import english_words_set

nine_words = {
    word
    for word in english_words_set
    if len(word) == 9
}


def random_nine() -> str:
    return random.choice(list(nine_words))


def shared_letters_for(words: List[str]) -> Dict[str, Set[str]]:
    shared: Dict[str, Set[str]] = defaultdict(set)
    for word in words:
        for letter in word:
            shared[letter].add(letter)
    return shared


def square_for_nine(nine: str) -> List[List[str]]:
    fitting = [
        word
        for word in english_words_set
        if fits(nine, word)
    ]

    shared_letters = shared_letters_for(fitting)

    center, answers = random.choice(
        list(shared_letters.items())
    )

    answers.add(nine)

    letters = list(nine)
    letters.remove(center)
    random.shuffle(letters)

    return [
        letters[:3],
        [letters[4], center, letters[5]],
        letters[5:]
    ]


def fits(containing: str, contained: str) -> bool:
    ...



def main():
    from pprint import pprint

    pprint(square_for_nine(random_nine()))


if __name__ == '__main__':
    main()

