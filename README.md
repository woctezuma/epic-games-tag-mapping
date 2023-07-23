# Epic Games Tag Mapping

This repository allows to compute an embedding of user tags, based on games on the Epic Games store.

![Tags for Fortnite](https://github.com/woctezuma/epic-games-tag-mapping/wiki/img/fortnite.png)

## Definition

A "tag" is a word or expression attached to a game, as can be seen [on the store page of the game "Fortnite"][fortnite].

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

To analyze the joint occurences of tags for each game, run:

```bash
python map_tags.py
```

To create a mapping of tags, run [`epic_games_tag_mapping.ipynb`][colab-notebook]
[![Open In Colab][colab-badge]][colab-notebook]

## Results

A 2D embedding is obtained by [**U**niform **M**anifold **A**pproximation and **P**rojection][umap-github] (UMAP) with the cosine metric.

### With the incidence matrix

This is the map of tags obtained with the [incidence matrix][wiki-incidence-matrix] as input.

![Map of Epic Games tags with the incidence matrix](https://github.com/woctezuma/epic-games-tag-mapping/wiki/img/incidence_matrix.png)

### With the adjacency matrix

This is the map of tags obtained with the [adjacency matrix][wiki-adjacency-matrix] as input.

![Map of Epic Games tags with the adjacency matrix](https://github.com/woctezuma/epic-games-tag-mapping/wiki/img/adjacency_matrix.png)

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
[umap-github]: <https://github.com/lmcinnes/umap>
[wiki-incidence-matrix]: <https://en.wikipedia.org/wiki/Incidence_matrix>
[wiki-adjacency-matrix]: <https://en.wikipedia.org/wiki/Adjacency_matrix>
[colab-notebook]: <https://colab.research.google.com/github/woctezuma/epic-games-tag-mapping/blob/colab/epic_games_tag_mapping.ipynb>
[colab-badge]: <https://colab.research.google.com/assets/colab-badge.svg>
