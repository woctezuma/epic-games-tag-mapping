POLL_DEFINITION_FIELD = "pollDefinitionId"
LOCALIZATION_FIELDS = ["text", "emoji", "resultEmoji", "resultTitle", "resultText"]


def check_fields(sandbox_id, poll_description, poll_definition_id, poll_localizations):
    if poll_description[POLL_DEFINITION_FIELD] != poll_definition_id:
        print(
            f'[WARNING] {sandbox_id} {POLL_DEFINITION_FIELD} -> {poll_description[POLL_DEFINITION_FIELD]} != {poll_definition_id}',
        )

    for field in LOCALIZATION_FIELDS:
        if poll_description[field] != poll_localizations[field]:
            print(
                f'[WARNING] {sandbox_id} {field} -> {poll_description[field]} != {poll_localizations[field]}',
            )
