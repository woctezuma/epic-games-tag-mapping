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

## Data source

The file `data/page_mappings.json`:
- contains the mapping between page slugs and sandbox IDs,
- was copied from [`woctezuma/epic-games-tracker`][egs-tracker].

## Usage

To download tags to `data/poll_summary.json` and `data/poll_dictionary.json`, run:

```bash
python download_tags.py
```

To create the mapping by analyzing the joint occurences of tags for each game, run the Python script as follows:

```bash
python map_tags.py
```

## Results

Results are shown [on the Wiki][wiki].

## References

- [Steam Tag Mapping][steam-tag-mapping]
- A [tracker for ratings and tags][madjoki-egs-ratings] (called "awards" there) on the Epic Games store
- A [tracker for ratings and achievements][egs-tracker]

<!-- Definitions -->

[python]: <https://www.python.org/downloads/>
[fortnite]: <https://store.epicgames.com/product/fortnite>
[wiki]: <https://github.com/woctezuma/epic-games-tag-mapping/wiki>
[steam-tag-mapping]: <https://github.com/woctezuma/steam-tag-mapping>
[madjoki-egs-ratings]: <https://github.com/nikop/epic-games-ratings>
[egs-tracker]: <https://github.com/woctezuma/epic-games-tracker>
