from random import choice, shuffle
from typing import List, Dict, Set, Tuple
from collections import defaultdict, Counter
from english_words import english_words_set

nine_words: Set[str] = {
    word
    for word in english_words_set
    if len(word) == 9
}


def random_nine() -> str:
    return choice(list(nine_words))


def shared_letters_for(words: List[str]) -> Dict[str, Set[str]]:
    shared: Dict[str, Set[str]] = defaultdict(set)
    for word in words:
        for letter in word:
            shared[letter].add(word)
    return shared


def square_for_nine(nine: str) -> Tuple[Set[str], List[List[str]]]:
    fitting = [
        word
        for word in english_words_set
        if len(word) >= 4 and fits(nine, word)
    ]

    shared_letters = shared_letters_for(fitting)

    center, answers = choice(
        list(shared_letters.items())
    )

    answers.add(nine)

    letters = list(nine)
    letters.remove(center)
    shuffle(letters)

    lines = [
        letters[:3],
        [letters[4], center, letters[5]],
        letters[5:]
    ]

    return answers, lines


def fits(containing: str, contained: str) -> bool:
    containing_c = Counter(containing)
    contained_c = Counter(contained)

    return all(
        containing_c[letter] >= count
        for letter, count in contained_c.items()
    )


def main():
    __import__('ipdb').set_trace()
    answers, lines = square_for_nine(random_nine())

    print('\n'.join(map(''.join, lines)))


if __name__ == '__main__':
    main()
