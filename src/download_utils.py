from src.data_utils import POLL_DATA_FNAME
from src.json_utils import load_json_failsafe, save_json
from src.parse_utils import are_dummy_poll_results
from src.query_game_polls import to_game_polls


def download_poll_data(
    sandbox_ids,
    locale="en",
    include_localizations=True,
    num_steps_between_saves=100,
    verbose=True,
):
    poll_data = load_json_failsafe(POLL_DATA_FNAME)

    num_sandboxes = len(sandbox_ids)

    for counter, sandbox_id in enumerate(sandbox_ids, start=1):
        if sandbox_id in poll_data:
            continue

        poll_results = to_game_polls(
            sandbox_id,
            locale=locale,
            include_localizations=include_localizations,
            verbose=verbose,
        )

        if verbose and not are_dummy_poll_results(poll_results):
            print(f"[{counter}/{num_sandboxes}] {sandbox_id} -> {poll_results}")

        poll_data[sandbox_id] = poll_results

        if counter % num_steps_between_saves == 0:
            save_json(poll_data, POLL_DATA_FNAME, prettify=True)

    save_json(poll_data, POLL_DATA_FNAME, prettify=True)

    return poll_data
