def sort_tags(tag_dictionary, verbose=True):
    tags = sorted(set(tag_dictionary), key=int)
    tag_names = [tag_dictionary[tag]["resultTitle"] for tag in tags]

    if verbose:
        for tag_index, tag_title in zip(tags, tag_names, strict=True):
            print(f'- {tag_index.rjust(2)} -> {tag_title}')

    return tags, tag_names
