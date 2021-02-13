from os import listdir
import copy


def get_tournament_summaries_and_re_entries(
        tournament_files: list,
        TOURNAMENT_SUMMARY_FOLDER: str) -> list:
    """
    Returns a list of TournamentFiles with the values of tournament_summary and re_entries set.

            Parameters:
                    tournament_files (List[TournamentFiles]): a list of TournamentFiles
                    TOURNAMENT_SUMMARY_FOLDER (str): the tournament summary parent folder

            Returns:
                    tournament_files (list): a list of TournamentFiles classes
    """

    def find_best_summary_when_multiple_filenames(summary_file_name: list):
        """

        :param summary_file_name:
        :return:
        """
        all = {}
        for file in summary_file_name:
            with open(TOURNAMENT_SUMMARY_FOLDER + file, 'r') as f:
                data = f.read()
                hhsum = eval(copy.deepcopy(data))
                all[file] = hhsum['player_count']
        return max(all, key=all.get)

    def get_tournament_summary_filename(tournament_summaries: list) -> list or None:
        """

        :param tournament_summaries:
        :return:
        """
        if len(tournament_summaries) == 0:
            return None
        else:
            if len(tournament_summaries) == 1:
                return tournament_summaries[0]
            if len(tournament_summaries) > 1:
                return find_best_summary_when_multiple_filenames(tournament_summaries)

    def get_re_entries(tournament_summaries: list) -> int:
        """

        :param tournament_summaries:
        :return:
        """
        nb_of_re_entries = len(tournament_summaries)
        if nb_of_re_entries == 0:
            # if there's no process summary, there is 1 re-entry by default
            return 1
        return nb_of_re_entries

    for t_file in tournament_files:
        summary_file_names = [f for f in listdir(TOURNAMENT_SUMMARY_FOLDER) if str(t_file.tournament_id) in f]
        re_entries = get_re_entries(summary_file_names)
        tournament_summary = get_tournament_summary_filename(summary_file_names)
        t_file.set_re_entries(re_entries)
        t_file.set_tournament_summary_filename(tournament_summary)

    return tournament_files
