# nytimesarchive
Python wrapper for the New York Times [Archive API](https://developer.nytimes.com/archive_api.json). 

## Note

As of 11/17/2016, the NYT Developers [page](https://developer.nytimes.com/) lists the Archive API as being in alpha status. 

## Usage

The Archive API provides JSON format NYT articles by month. 

```python
from nytimesarchive import ArchiveAPI
api = ArchiveAPI('your api key goes here')
print(api.query(2016, 11))
```

## Instllation

```
sudo pip3 install -e ./nytimesarchive
# (PyPi integration coming soon)
```

## Article API

For the [Article API](https://developer.nytimes.com/article_search_v2.json), see Evan Scherlock's [nytimesarticle](https://github.com/evansherlock/nytimesarticle).
