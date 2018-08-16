#!/usr/bin/env python3

import argparse
import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable
import sys

playing_url = "https://movie.douban.com/cinema/nowplaying/"


class MovieItem:
    title = ""
    score = 0.0
    votecount = 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="pick movie to watch")

    parser.add_argument("-c", "--city", help="the city to scrapy")
    parser.add_argument("-s", "--sort", default="score", choices=["score", "vote"], help="sort method")

    args = parser.parse_args()
    
    url = playing_url
    if args.city:
        url += args.city
    resp = requests.get(url)
    if resp.status_code != 200:
        print("get playing list fail")
        sys.exit(-1)
    movieplaying = []
    soup = BeautifulSoup(resp.content, "lxml")
    for item in soup.find_all("li", {"data-category": "nowplaying"}):
        movie = MovieItem()
        movie.title = item["data-title"]
        movie.score = float(item["data-score"])
        movie.votecount = int(item["data-votecount"])
        movieplaying.append(movie)
    sorted_movie = None
    if args.sort == "score":
        sorted_movie = sorted(movieplaying,  key = lambda m:m.score, reverse = True)
    elif args.sort == "vote":
        sorted_movie = sorted(movieplaying,  key = lambda m:m.votecount, reverse = True)
    table = PrettyTable(["title", "score", "vote"])
    for m in sorted_movie:
        table.add_row([m.title, m.score, m.votecount])
    print(table)
