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
from import_new_tournaments.process_hh_files.process.hands.extract.positions_info import position_info


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

    position_info = dict
        dict containing each position (regardless of
        how many players seated) as key and the name of
        the player, his stack size and his cards (if showdown).
        this dict fills the position values
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

        self.BTN_player_name = None
        self.SB_player_name = None
        self.BB_player_name = None
        self.UTG_player_name = None
        self.UTGp1_player_name = None
        self.MP_player_name = None
        self.MPp1_player_name = None
        self.MPp2_player_name = None
        self.CO_player_name = None

        self.BTN_stack = None
        self.SB_stack = None
        self.BB_stack = None
        self.UTG_stack = None
        self.UTGp1_stack = None
        self.MP_stack = None
        self.MPp1_stack = None
        self.MPp2_stack = None
        self.CO_stack = None

        self.BTN_cards = None
        self.SB_cards = None
        self.BB_cards = None
        self.UTG_cards = None
        self.UTGp1_cards = None
        self.MP_cards = None
        self.MPp1_cards = None
        self.MPp2_cards = None
        self.CO_cards = None

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
        self._get_position_info()

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

    def _get_position_info(self):
        _position_info = position_info(self.hand_txt)
        self.BTN_player_name = _position_info['BTN']['Name']
        self.SB_player_name = _position_info['SB']['Name']
        self.BB_player_name = _position_info['BB']['Name']
        self.UTG_player_name = _position_info['UTG']['Name']
        self.UTGp1_player_name = _position_info['UTG+1']['Name']
        self.MP_player_name = _position_info['MP']['Name']
        self.MPp1_player_name = _position_info['MP+1']['Name']
        self.MPp2_player_name = _position_info['MP+2']['Name']
        self.CO_player_name = _position_info['CO']['Name']

        self.BTN_stack = _position_info['BTN']['Stack']
        self.SB_stack = _position_info['SB']['Stack']
        self.BB_stack = _position_info['BB']['Stack']
        self.UTG_stack = _position_info['UTG']['Stack']
        self.UTGp1_stack = _position_info['UTG+1']['Stack']
        self.MP_stack = _position_info['MP']['Stack']
        self.MPp1_stack = _position_info['MP+1']['Stack']
        self.MPp2_stack = _position_info['MP+2']['Stack']
        self.CO_stack = _position_info['CO']['Stack']

        self.BTN_cards = _position_info['BTN']['Cards']
        self.SB_cards = _position_info['SB']['Cards']
        self.BB_cards = _position_info['BB']['Cards']
        self.UTG_cards = _position_info['UTG']['Cards']
        self.UTGp1_cards = _position_info['UTG+1']['Cards']
        self.MP_cards = _position_info['MP']['Cards']
        self.MPp1_cards = _position_info['MP+1']['Cards']
        self.MPp2_cards = _position_info['MP+2']['Cards']
        self.CO_cards = _position_info['CO']['Cards']
