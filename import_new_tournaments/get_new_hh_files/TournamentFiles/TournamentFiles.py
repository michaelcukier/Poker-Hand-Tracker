
class TournamentFiles:
    """
    A class to represent a single tournament that hasn't been processed yet

    ...

    Attributes
    ----------
    tournament_id : int
        id of the tournament
    hand_history_filenames : list
        the list of hand history filename(s)
    tournament_summary_filename : str
        the tournament summary filename
    re_entries : int
        the number of re-entries

    Methods
    -------
    add_hand_history_filename(filename):
        add a hand history filename to the current list

    set_tournament_summary_filename(filename):
        sets the tournament summary filename

    set_re_entries(re_entries):
        sets the number of re-entries
    """

    def __init__(self, tournament_id: int):
        self.tournament_id = tournament_id
        self.hand_history_filenames = []
        self.tournament_summary_filename = None
        self.re_entries = 0

    def add_hand_history_filename(self, filename):
        self.hand_history_filenames.append(filename)

    def set_tournament_summary_filename(self, filename):
        self.tournament_summary_filename = filename

    def set_re_entries(self, re_entries: int):
        self.re_entries = re_entries