from src.data_utils import SANDBOX_FNAME
from src.download_utils import download_poll_data
from src.json_utils import load_json
from src.parse_utils import parse_poll_dictionary, parse_poll_summary


def main():
    page_mappings = load_json(SANDBOX_FNAME)

    poll_data = download_poll_data(sandbox_ids=page_mappings.values())

    poll_summary = parse_poll_summary(poll_data)
    poll_dictionary = parse_poll_dictionary(poll_data)


if __name__ == "__main__":
    main()
