from src.data_utils import POLL_DICTIONARY_FNAME, POLL_SUMMARY_FNAME
from src.json_utils import load_json
from src.matrix_utils import get_adjacency_matrix, get_tag_joint_game_matrix
from src.tag_utils import sort_tags


def main():
    games = load_json(POLL_SUMMARY_FNAME)
    tag_dictionary = load_json(POLL_DICTIONARY_FNAME)

    tags, tag_names = sort_tags(tag_dictionary)

    tag_joint_game_matrix = get_tag_joint_game_matrix(games, tags)
    tags_adjacency_matrix = get_adjacency_matrix(tag_joint_game_matrix)


if __name__ == "__main__":
    main()
