# Epic Games Tag Mapping

This repository allows to compute an embedding of user tags, based on games on the Epic Games store.

![Map of Epic Games tags](https://github.com/woctezuma/epic-games-tag-mapping/wiki/img/cover.png)

## Definition

A "tag" is a word or expression attached to a game, as can be seen [on the store page of the game "Fortnite"][fortnite].

![Tags for Fortnite](https://github.com/woctezuma/epic-games-tag-mapping/wiki/img/fortnite.png)

## Requirements

-   Install the latest version of [Python 3.X][python].
-   Install the required packages:

```bash
pip install -r requirements.txt
```

## Usage

To create the mapping by analyzing the joint occurences of tags for each game, run the Python script as follows:

```bash
python map_tags.py
```

## Results

Results are shown [on the Wiki][wiki].

## References

- [Steam Tag Mapping][steam-tag-mapping]
- A [tracker for ratings and tags][madjoki-egs-ratings] (called "awards" there) on the Epic Games store

<!-- Definitions -->

[python]: <https://www.python.org/downloads/>
[fortnite]: <https://store.epicgames.com/product/fortnite>
[wiki]: <https://github.com/woctezuma/epic-games-tag-mapping/wiki>
[steam-tag-mapping]: <https://github.com/woctezuma/steam-tag-mapping>
[madjoki-egs-ratings]: <https://github.com/nikop/epic-games-ratings>
