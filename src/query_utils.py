def format_params_for_query_str(sandbox_id, locale="en"):
    params_str = f'(sandboxId: "{sandbox_id}", locale: "{locale}") '
    return params_str


def get_query_str_for_polls(sandbox_id, locale="en", include_localizations=True):
    query_str = "RatingsPolls {getProductResult"
    query_str += format_params_for_query_str(sandbox_id, locale)
    query_str += "{"

    query_str += "pollResult {id pollDefinitionId total "
    if include_localizations:
        query_str += "localizations {text emoji resultEmoji resultTitle resultText}"
    query_str += "}"

    query_str += "}} "

    return query_str
