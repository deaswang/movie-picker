# Movie Picker

从豆瓣挑选当前上映的高分影片。

# Usage

```python
$python picker.py -h
usage: picker.py [-h] [-c CITY] [-s {score,vote}]

pick movie to watch

optional arguments:
  -h, --help            show this help message and exit
  -c CITY, --city CITY  the city to scrapy
  -s {score,vote}, --sort {score,vote}
                        sort method
```

可以设置城市
```python
python picker.py -c shanghai
```

按分数排序和按投票数排序,默认按分数排序
```python
python picker.py -c shanghai -s vote
```
