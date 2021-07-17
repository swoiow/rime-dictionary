import json
import os
import pprint
import re
import time

import httpx


UA_STRING = "Mozilla/5.0 (compatible;PetalBot;+https://webmaster.petalsearch.com/site/petalbot)"

IX_RULE = re.compile(r"(?P<number>[\d]+)个词库")
SEARCH_RULE = re.compile(r"(?P<number>[\d]+)个搜索结果")
TITLE_RULE = re.compile(r"&name=(?P<title>[\S \d\-\+]*)\"\>")
DATE_RULE = re.compile(r"[\d]{4}-[\d]{2}-[\d]{2}")
DOWNLOAD_LINK_RULE = re.compile(r"(?P<link>//pinyin.sogou.com/d/dict/download_cell.php\?id=[\d]+&name=[\S \d\-\+]*)\">")

CATE = "https://pinyin.sogou.com/dict/cate/index/{idx}"
GFTJ_CATE = "https://pinyin.sogou.com/dict/search/search_list/%A1%BE%B9%D9%B7%BD%CD%C6%BC%F6%A1%BF/normal/{idx}"

DOWNLOAD_API = "https://pinyin.sogou.com/d/dict/download_cell.php?id={id}&name={name}&f=detail"

if not os.path.exists("./官方推荐"):
    os.mkdir("官方推荐")


def fetch_all_gftj():
    for ix in range(1, 46):
        r = httpx.options(GFTJ_CATE.format(idx=ix), headers={
            "User-Agent": UA_STRING
        })

        html = r.content.decode("utf8", 'ignore')
        wrodbook = re.findall(SEARCH_RULE, html)

        if wrodbook and int(wrodbook[0]) > 0:
            with open(f"官方推荐/cate-{ix}", "w", encoding="utf8") as wf:
                wf.write(html)

        time.sleep(0.5)
        print(ix, int(wrodbook[0]))


def sogou_wordbook():
    wordbooks = []
    existed = os.listdir("./官方推荐")
    for f in existed:
        with open(f"官方推荐/{f}") as rf:
            html = rf.read()

            titles = re.findall(TITLE_RULE, html)
            links = re.findall(DOWNLOAD_LINK_RULE, html)
            dates = re.findall(DATE_RULE, html)
            try:
                assert len(titles) == len(links) == len(dates)
            except AssertionError:
                raise Exception(f)

            wordbooks.extend(zip(titles, links, dates))

    dicts = json.dumps(
        sorted([{"title": t, "link": l, "date": d} for t, l, d in wordbooks], key=lambda x: x["date"], reverse=True),
        indent=2,
        ensure_ascii=False
    )
    pprint.pprint(dicts)
    return dicts


if __name__ == '__main__':
    fetch_all_gftj()
    sogou_wordbook()
