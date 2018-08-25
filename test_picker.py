#!/usr/bin/env python3

import unittest
import picker

class TestPicker(unittest.TestCase):

    def test_get_html(self):
        content = picker.get_html("shanghai")
        assert content is not None

    def test_process(self):
        with open("test/test.html", "r") as f:
            content = f.read()
            movies = picker.process(content)
            assert len(movies) == 21

    def test_gen_table(self):
        movie_list = []
        movie = picker.MovieItem()
        movie.title = "title1"
        movie.score = 6
        movie.votecount = 4000
        movie_list.append(movie)
        movie2 = picker.MovieItem()
        movie2.title = "title2"
        movie2.score = 7
        movie2.votecount = 3000
        movie_list.append(movie2)

        table = picker.gen_table(movie_list, "score")

        assert "title2" in table[0].get_string()
        assert "7" in table[0].get_string()
        assert "3000" in table[0].get_string()

        table = picker.gen_table(movie_list, "vote")
        assert "title1" in table[0].get_string()
        assert "6" in table[0].get_string()
        assert "4000" in table[0].get_string()


if __name__ == '__main__':
    unittest.main()
