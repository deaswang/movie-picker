#!/usr/bin/env python3

"""
Pick the playing movie from douban.
"""

import argparse
import sys
import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable


BASE_URL = "https://movie.douban.com/cinema/nowplaying/"


class MovieItem:
    """
    set the single movie information
    """

    def __init__(self):
        self.title = ""
        self.score = 0.0
        self.votecount = 0

# get html
def get_html(city):
    """
    get html content
    :param city:
    :return:
    """
    try:
        url = BASE_URL
        if city:
            url += city
        resp = requests.get(url)
        if resp.status_code != 200:
            print("get playing list fail")
            sys.exit(-1)
        return resp.content
    except Exception as e:
        print(e.with_traceback())
        sys.exit(-1)


def process(content):
    """
    process html content
    :param content:
    :return:
    """
    movieplaying = []
    soup = BeautifulSoup(content, "lxml")
    for item in soup.find_all("li", {"data-category": "nowplaying"}):
        movie = MovieItem()
        movie.title = item["data-title"]
        movie.score = float(item["data-score"])
        movie.votecount = int(item["data-votecount"])
        movieplaying.append(movie)
    return movieplaying


def show_table(movies):
    """
    print the movies table
    :param movies:
    :return:
    """
    sorted_movie = None
    if args.sort == "score":
        sorted_movie = sorted(movies, key=lambda m: m.score, reverse=True)
    elif args.sort == "vote":
        sorted_movie = sorted(movies, key=lambda m: m.votecount, reverse=True)
    table = PrettyTable(["title", "score", "vote"])
    for m in sorted_movie:
        table.add_row([m.title, m.score, m.votecount])
    print(table)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="pick movie to watch")

    parser.add_argument("-c", "--city", help="the city to scrapy")
    parser.add_argument("-s", "--sort", default="score", choices=["score", "vote"],
                        help="sort method")

    args = parser.parse_args()

    content = get_html(args.city)
    movies = process(content)
    show_table(movies)
