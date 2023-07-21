from src.check_utils import POLL_DEFINITION_FIELD, check_fields
from src.data_utils import POLL_DICTIONARY_FNAME, POLL_SUMMARY_FNAME
from src.json_utils import save_json


def are_dummy_poll_results(poll_results):
    return poll_results is None or len(poll_results) == 0


def parse_poll_summary(poll_data):
    poll_summary = {}
    for sandbox_id, poll_results in poll_data.items():
        if not are_dummy_poll_results(poll_results):
            poll_summary[sandbox_id] = {e["id"]: e["total"] for e in poll_results}

    if len(poll_summary) > 0:
        save_json(poll_summary, POLL_SUMMARY_FNAME, prettify=True)

    return poll_summary


def parse_poll_dictionary(poll_data):
    poll_dictionary = {}
    for sandbox_id, poll_results in poll_data.items():
        if not are_dummy_poll_results(poll_results):
            for element in poll_results:
                poll_id = element["id"]
                poll_definition_id = element[POLL_DEFINITION_FIELD]
                poll_localizations = element["localizations"]

                poll_description = poll_dictionary.get(poll_id)

                if poll_description is None:
                    poll_dictionary[poll_id] = {
                        POLL_DEFINITION_FIELD: poll_definition_id,
                    } | poll_localizations
                else:
                    check_fields(
                        sandbox_id,
                        poll_description,
                        poll_definition_id,
                        poll_localizations,
                    )

    if len(poll_dictionary) > 0:
        save_json(poll_dictionary, POLL_DICTIONARY_FNAME, prettify=True)

    return poll_dictionary
