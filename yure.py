import sys
from pathlib import Path
from typing import Dict, List

import pyperclip
from sudachipy import Tokenizer, Dictionary

SUDACHI_TOKENIZER = Dictionary().create()
TOKENIZE_MODE = Tokenizer.SplitMode.C


def get_reading(s: str) -> str:
    return "".join(
        [morph.reading_form() for morph in SUDACHI_TOKENIZER.tokenize(s, TOKENIZE_MODE)]
    )


def group_variation(s: str) -> Dict[str, List[str]]:
    d: Dict[str, List[str]] = {}
    morphs = SUDACHI_TOKENIZER.tokenize(s, TOKENIZE_MODE)
    for morph in morphs:
        n_form = morph.normalized_form()
        d_form = morph.dictionary_form()
        if n_form in d:
            d[n_form].append(d_form)
        else:
            d[n_form] = [d_form]
    return d


def format_variation(d: Dict[str, List[str]]) -> str:
    ss = []
    for k, v in d.items():
        vs = list(set(v))
        if 1 < len(vs):
            ss.append([get_reading(k), "／".join(vs)])
    ss.sort(key=lambda x: x[0])
    return "\n".join(["{}\t{}".format(*s) for s in ss])


def read_file(path: str) -> str:
    if len(path) < 1:
        c = pyperclip.paste()
        if len(c) < 1:
            print("Clipboard is empty.")
            return ""
        return c

    p = Path(path)
    if not p.exists():
        print("Invalid path.")
        return ""

    t = p.read_text(encoding="utf-8")
    if len(t) < 1:
        print("Empty file.")
        return ""
    return t


def main(path: str):
    t = read_file(path)
    if 0 < len(t):
        s = format_variation(group_variation(t))
        Path("out/out.txt").write_text(s, encoding="utf-8")


if __name__ == "__main__":
    args = sys.argv
    path = args[1] if 1 < len(args) else ""
    main(path)
