
from process.tournament.Tournament.Tournament import Tournament


def process_filenames(tournamentFilenamesList: list, parent_folder_hand_history: str, parent_folder_tournament_summary: str) -> list:
    processed = []

    for t in tournamentFilenamesList:
        processed_t = Tournament(
            hand_history_filenames=t.hand_history_filenames,
            tournament_summary_filename=t.tournament_summary_filename,
            re_entries=t.re_entries,
            parent_folder_hand_history=parent_folder_hand_history,
            parent_folder_tournament_summary=parent_folder_tournament_summary
        )
        processed_t.build_tournament()
        processed.append(processed_t)

    return processed
