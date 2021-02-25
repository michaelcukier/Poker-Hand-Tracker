from import_new_tournaments.process_hh_files.process.hands.extract.time import time
from import_new_tournaments.process_hh_files.process.hands.extract.level import level
from import_new_tournaments.process_hh_files.process.hands.extract.my_cards import my_cards
from import_new_tournaments.process_hh_files.process.hands.extract.board_cards import board_cards
from import_new_tournaments.process_hh_files.process.hands.extract.tournament_id import tournament_id
from import_new_tournaments.process_hh_files.process.hands.extract.id import get_id
from import_new_tournaments.process_hh_files.process.hands.extract.starting_stack_size_bb import starting_stack_size_bb
from import_new_tournaments.process_hh_files.process.hands.extract.side_pot_n_winner import side_pot_n_winner
from import_new_tournaments.process_hh_files.process.hands.extract.main_pot_winner import main_pot_winner
from import_new_tournaments.process_hh_files.process.hands.extract.side_pot_n_size_bb import side_pot_n_size_bb
from import_new_tournaments.process_hh_files.process.hands.extract.main_pot_size_bb import main_pot_size_bb
from import_new_tournaments.process_hh_files.process.hands.extract.nb_occupied_seats import nb_occupied_seats
from import_new_tournaments.process_hh_files.process.hands.extract.table_type import table_type
from import_new_tournaments.process_hh_files.process.hands.extract.positions_info import position_player_name


class Hand:
    """
    A class that represents a single hand and the methods used to build it

    ...

    Attributes
    ----------
    hand_txt : str
        a hand history raw text

    time : str
        the time when the hand started

    level : str
        the blind level

    my_cards : str
        the player's 2 hole cards

    board_cards : str
        the community cards

    tournament_id : int
        the tournament ID of the hand

    id : str
        the unique ID of the hand

    starting_stack_size_bb : float
        the stack size at the beginning of the hand in big blinds

    main_pot_winner : str
        the name of the main pot winner

    side_pot_1_winner: str or None
        the name of side pot #1 winner

    side_pot_2_winner: str or None
        the name of side pot #2 winner

    side_pot_3_winner: str or None
        the name of side pot #3 winner

    main_pot_size_bb : float
        the size of the main pot in big blinds

    side_pot_1_size_bb = float or None
        the size of the side pot #1 in big blinds

    side_pot_2_size_bb = float or None
        the size of the side pot #2 in big blinds

    side_pot_3_size_bb = float or None
        the size of the side pot #3 in big blinds

    nb_of_occupied_seats = int
        the number of seated players at the table

    table_type = str
        the table type (eg: 9-max)

    position_and_player = dict
        dict containing each position (regardless of
        how many players seated) as key and the name of
        the player as value. If no player is seated at
        position X, then position X is set to None.
    """

    def __init__(self, hand_txt):
        self.hand_txt = hand_txt.replace("'", '"')  # to avoid sql problems when inserting
        self.time = None
        self.level = None
        self.my_cards = None
        self.board_cards = None
        self.tournament_id = None
        self.id = None
        self.starting_stack_size_bb = None
        self.main_pot_winner = None
        self.side_pot_1_winner = None
        self.side_pot_2_winner = None
        self.side_pot_3_winner = None
        self.main_pot_size_bb = None
        self.side_pot_1_size_bb = None
        self.side_pot_2_size_bb = None
        self.side_pot_3_size_bb = None
        self.nb_occupied_seats = None
        self.table_type = None
        self.position_and_player = None

    def build_hand(self):
        self._get_time()
        self._get_level()
        self._get_my_cards()
        self._get_board_cards()
        self._get_tournament_id()
        self._get_id()
        self._get_starting_stack_size_bb()
        self._get_main_pot_winner()
        self._get_side_pot_1_winner()
        self._get_side_pot_2_winner()
        self._get_side_pot_3_winner()
        self._get_main_pot_size_bb()
        self._get_side_pot_1_size_bb()
        self._get_side_pot_2_size_bb()
        self._get_side_pot_3_size_bb()
        self._get_nb_occupied_seats()
        self._get_table_type()
        self._get_position_player_name()

    def _get_time(self):
        self.time = time(self.hand_txt)

    def _get_level(self):
        self.level = level(self.hand_txt)

    def _get_my_cards(self):
        self.my_cards = my_cards(self.hand_txt)

    def _get_board_cards(self):
        self.board_cards = board_cards(self.hand_txt)

    def _get_tournament_id(self):
        self.tournament_id = tournament_id(self.hand_txt)

    def _get_id(self):
        self.id = get_id(self.hand_txt)

    def _get_starting_stack_size_bb(self):
        self.starting_stack_size_bb = starting_stack_size_bb(self.hand_txt)

    def _get_main_pot_winner(self):
        self.main_pot_winner = main_pot_winner(self.hand_txt)

    def _get_side_pot_1_winner(self):
        self.side_pot_1_winner = side_pot_n_winner(self.hand_txt, n=1)

    def _get_side_pot_2_winner(self):
        self.side_pot_2_winner = side_pot_n_winner(self.hand_txt, n=2)

    def _get_side_pot_3_winner(self):
        self.side_pot_3_winner = side_pot_n_winner(self.hand_txt, n=3)

    def _get_main_pot_size_bb(self):
        self.main_pot_size_bb = main_pot_size_bb(self.hand_txt)

    def _get_side_pot_1_size_bb(self):
        self.side_pot_1_size_bb = side_pot_n_size_bb(self.hand_txt, n=1)

    def _get_side_pot_2_size_bb(self):
        self.side_pot_2_size_bb = side_pot_n_size_bb(self.hand_txt, n=2)

    def _get_side_pot_3_size_bb(self):
        self.side_pot_3_size_bb = side_pot_n_size_bb(self.hand_txt, n=3)

    def _get_nb_occupied_seats(self):
        self.nb_occupied_seats = nb_occupied_seats(self.hand_txt)

    def _get_table_type(self):
        self.table_type = table_type(self.hand_txt)

    def _get_position_player_name(self):
        self.position_and_player = position_player_name(self.hand_txt)
