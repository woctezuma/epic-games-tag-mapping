import numpy as np

from src.data_utils import JOINT_MATRIX_FNAME


def get_tag_joint_game_matrix(games, tags, verbose=True):
    tag_joint_game_matrix = np.zeros([len(tags), len(games)], dtype=int)

    for game_index, game_tags in enumerate(games.values()):
        for tag_index, tag in enumerate(tags):
            if tag in game_tags:
                tag_joint_game_matrix[tag_index][game_index] += 1

    if verbose:
        print(tag_joint_game_matrix.shape)

    np.savetxt(JOINT_MATRIX_FNAME, tag_joint_game_matrix, fmt='%d')

    return tag_joint_game_matrix


def get_adjacency_matrix(tag_joint_game_matrix=None, verbose=True):
    if tag_joint_game_matrix is None:
        tag_joint_game_matrix = np.loadtxt(JOINT_MATRIX_FNAME)

    tags_adjacency_matrix = np.matmul(
        tag_joint_game_matrix,
        tag_joint_game_matrix.transpose(),
    )

    # Make sure the diagonal of the matrix contains only zeros. See http://lvdmaaten.github.io/tsne/
    for tag_index in range(tags_adjacency_matrix.shape[0]):
        tags_adjacency_matrix[tag_index][tag_index] = 0

    # Normalize the matrix to sum up to one. See http://lvdmaaten.github.io/tsne/
    tags_adjacency_matrix = tags_adjacency_matrix.astype(float)
    tags_adjacency_matrix /= tags_adjacency_matrix.sum()

    if verbose:
        print(tags_adjacency_matrix.shape)

    return tags_adjacency_matrix
