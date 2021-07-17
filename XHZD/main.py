#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import json
import re


__NAME__ = "ext.xhzd"
WORD_FREQUENCY = 2

fmt = f"""---
name: {__NAME__}
version: "{datetime.datetime.today().strftime('%Y.%m.%d')}"
sort: by_weight
use_preset_vocabulary: true
...

"""


def handle_idiom():
    bucket = []
    with open("idiom.json", "r", encoding="utf8") as rf:
        txt = json.load(rf)
    for i in txt:
        bucket.append((i["word"], i["pinyin"]))

    with open("idiom.raw.txt", "w", encoding="utf8") as wf:
        json.dump(bucket, wf, ensure_ascii=False)

    return bucket


def handle_words():
    bucket = []
    with open("ci.json", "r", encoding="utf8") as rf:
        txt = json.load(rf)
    for i in txt:
        bucket.append((i["ci"], None))

    with open("words.raw.txt", "w", encoding="utf8") as wf:
        json.dump(bucket, wf, ensure_ascii=False)

    return bucket


def handle_hans():
    bucket = []
    with open("word.json", "r", encoding="utf8") as rf:
        txt = json.load(rf)
    for i in txt:
        bucket.append((i["word"], i["pinyin"]))

    with open("hans.raw.txt", "w", encoding="utf8") as wf:
        json.dump(bucket, wf, ensure_ascii=False)

    return bucket


def dict_without_pinyin():
    filter_words_rule = re.compile(r"[,.\+\-，。a-zA-Z]+")
    idiom = handle_idiom()
    words = handle_words()
    hans = handle_hans()

    bucket = sorted(set([han for han, pinyin in idiom + words + hans]))

    with open(f"{__NAME__}.dict.yml", "w", encoding="utf8") as wf:
        wf.write(fmt + "\n".join([f"{i}\t{WORD_FREQUENCY}" for i in bucket if not re.findall(filter_words_rule, i)]))

    return bucket


if __name__ == '__main__':
    dict_without_pinyin()
