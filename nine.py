from uuid import uuid4
from random import Random
from typing import List, Dict, Set, Tuple
from collections import defaultdict, Counter

from english_words import english_words_set
from flask import Flask, request, render_template, url_for, redirect

app = Flask('__name__')

nine_words: Set[str] = {
    word
    for word in english_words_set
    if len(word) == 9
}


def random_nine(random: Random) -> str:
    return random.choice(list(nine_words))


def shared_letters_for(words: List[str]) -> Dict[str, Set[str]]:
    shared: Dict[str, Set[str]] = defaultdict(set)
    for word in words:
        for letter in word:
            shared[letter].add(word)
    return shared


def square_for_nine(random: Random,
                    nine: str) -> Tuple[List[str], List[List[str]]]:
    fitting = [
        word
        for word in english_words_set
        if len(word) >= 4 and fits(nine, word)
    ]

    shared_letters = shared_letters_for(fitting)

    center, answers = random.choice(
        list(shared_letters.items())
    )

    answers.add(nine)

    letters = list(nine)
    letters.remove(center)
    random.shuffle(letters)

    lines = [
        letters[:3],
        [letters[3], center, letters[4]],
        letters[5:]
    ]

    return sorted(answers, key=len, reverse=True), lines


def fits(containing: str, contained: str) -> bool:
    containing_c = Counter(containing)
    contained_c = Counter(contained)

    return all(
        containing_c[letter] >= count
        for letter, count in contained_c.items()
    )


@app.route('/random_new')
def random_new():
    return redirect(url_for('index', seed=uuid4()))


@app.route('/')
def index():
    seed = request.args.get('seed')

    if not seed:
        return redirect(url_for('index', seed=uuid4()))

    random = Random(seed)

    answers, lines = square_for_nine(random, random_nine(random))

    return render_template(
        'index.html',
        answers=answers,
        lines=lines,
        seed=seed
    )


if __name__ == '__main__':
    app.run(debug=True)
