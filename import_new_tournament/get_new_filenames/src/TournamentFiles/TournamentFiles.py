
class TournamentFiles:
    def __init__(self, tournament_id):
        self.tournament_id = tournament_id
        self.hand_history_filenames = []
        self.tournament_summary_filename = []
        self.re_entries = 0

    def add_hand_history_filename(self, filename):
        self.hand_history_filenames.append(filename)

    def add_tournament_summary_filename(self, filename):
        self.tournament_summary_filename.append(filename)

    def set_re_entries(self, re_entries: int):
        self.re_entries = re_entries