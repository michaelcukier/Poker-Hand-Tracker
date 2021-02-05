
# tournament class

from extract.hands.hands import process_hands, get_hands_in_list


class Tournament:
    def __init__(self, hand_history_filenames: list, tournament_summary_filename: list, re_entries: int, parent_folder: str):
        self.hand_history_filenames = hand_history_filenames
        self.tournament_summary_filename = tournament_summary_filename
        self.re_entries = re_entries
        self.parent_folder = parent_folder

        self.hands = None
        self.price = None
        self.finish_time = None
        self.elapsed_time = None
        self.prize = None
        self.position = None

    def build_tournament(self):
        self._get_hands()
        self._process_hands()




    def _get_hands(self):
        self.hands = get_hands_in_list(self.parent_folder, self.hand_history_filenames)

    def _process_hands(self):
        self.hands = process_hands(self.hands)

    def get_id(self):
        pass

    def get_price(self):
        pass

    def get_finish_time(self):
        pass

    def get_elapsed_time(self):
        pass

    def get_prize(self):
        pass

    def get_position(self):
        pass

