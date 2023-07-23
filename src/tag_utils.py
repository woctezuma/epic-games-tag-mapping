from src.data_utils import TAG_LIST_FNAME
from src.json_utils import load_json, save_json


def sort_tags(tag_dictionary, verbose=True):
    tags = sorted(set(tag_dictionary), key=int)
    tag_names = [tag_dictionary[tag]["resultTitle"] for tag in tags]

    if verbose:
        for tag_index, tag_title in zip(tags, tag_names, strict=True):
            print(f'- {tag_index.rjust(2)} -> {tag_title}')

    save_json(tag_names, TAG_LIST_FNAME, prettify=True)

    return tags, tag_names


def load_tag_names(fname=TAG_LIST_FNAME):
    return load_json(fname)
