
from .process.tournament.Tournament.Tournament import Tournament


def process_filenames(tournamentFilenamesList: list, parent_folder_hand_history: str, parent_folder_tournament_summary: str) -> list:
    """
    Wrapper function that returns the processed tournaments

            Parameters:
                    tournamentFilenamesList (list): list of tournaments filenames to process
                    parent_folder_hand_history (str): parent folder of the tournament hand history files
                    parent_folder_tournament_summary (str): parent folder of the tournament summary files

            Returns:
                    processed (list[Tournament]): a list of Tournament classes
    """

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
