from src.api import send_post_request_to_api
from src.query_utils import get_query_str_for_polls


def get_params_to_query_game_polls(sandbox_id, locale="en", include_localizations=True):
    query_str = "{"
    query_str += get_query_str_for_polls(sandbox_id, locale, include_localizations)
    query_str += "}"

    params = {"query": query_str}

    return params


def to_game_polls(sandbox_id, locale="en", include_localizations=True, verbose=True):
    params = get_params_to_query_game_polls(sandbox_id, locale, include_localizations)
    data = send_post_request_to_api(params, verbose=verbose)
    try:
        game_polls = data["data"]["RatingsPolls"]["getProductResult"]["pollResult"]
    except (TypeError, KeyError) as e:
        game_polls = None
    return game_polls
