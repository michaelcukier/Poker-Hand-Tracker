
from process.tournament.extract.hands import hands
from process.tournament.extract.id import id
from process.tournament.extract.price import price
from process.tournament.extract.finish_time import finish_time
from process.tournament.extract.elapsed_time import elapsed_time
from process.tournament.extract.prize import prize
from process.tournament.extract.position import position
from process.tournament.extract.opponents import opponents
from process.tournament.extract.nb_of_participants import nb_of_participants

from utils.get_hands_in_list import get_hands_in_list


class Tournament:
    def __init__(self,
                 hand_history_filenames: list,
                 tournament_summary_filename: str,
                 re_entries: int,
                 parent_folder_hand_history: str,
                 parent_folder_tournament_summary: str):

        self.hand_history_filenames = hand_history_filenames
        self.tournament_summary_filename = tournament_summary_filename
        self.re_entries = re_entries
        self.parent_folder_hand_history = parent_folder_hand_history
        self.parent_folder_tournament_summary = parent_folder_tournament_summary

        self.hands = None
        self.id = None
        self.price = None
        self.finish_time = None
        self.elapsed_time = None
        self.prize = None
        self.position = None
        self.opponents = None
        self.nb_of_participants = None

    def build_tournament(self):
        self._get_hands()
        self._get_id()
        self._get_price()
        self._get_finish_time()
        self._get_elapsed_time()
        self._get_prize()
        self._get_position()
        self._get_opponents()
        self._get_nb_of_participants()


    def _get_hands(self):
        self.hands = get_hands_in_list(self.parent_folder_hand_history, self.hand_history_filenames)
        self.hands = hands(self.hands)

    def _get_id(self):
        self.id = id(self.hand_history_filenames[0])

    def _get_price(self):
        self.price = price(self.hand_history_filenames[0])

    def _get_finish_time(self):
        last_hand = self.hands[-1]
        self.finish_time = finish_time(last_hand)

    def _get_elapsed_time(self):
        first_hand = self.hands[0]
        last_hand = self.hands[-1]
        self.elapsed_time = elapsed_time(first_hand, last_hand)

    def _get_prize(self):
        self.prize = prize(self.parent_folder_tournament_summary, self.tournament_summary_filename)

    def _get_position(self):
        self.position = position(self.parent_folder_tournament_summary, self.tournament_summary_filename)

    def _get_opponents(self):
        self.opponents = opponents(self.parent_folder_tournament_summary, self.tournament_summary_filename)

    def _get_nb_of_participants(self):
        self.nb_of_participants = nb_of_participants(self.parent_folder_tournament_summary, self.tournament_summary_filename)
