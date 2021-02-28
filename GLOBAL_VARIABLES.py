# edit those fields:
PLAYER_NAME = ''
HAND_HISTORY_FOLDER = '<>/AmericasCardroom/handHistory/' + PLAYER_NAME + '/'
TOURNEY_SUMMARY_FOLDER = '<>/AmericasCardroom/TournamentSummary/' + PLAYER_NAME + '/'
TOURNAMENTS_TO_EXTRACT = {'<>'}
FOLDER_PLOT_DUMP = "<>/plots_dump/"
DATABASE_LOCATION = '<>/db.db'

# optional:
TEST_RANDOM_HAND_HISTORIES_FOLDER = '<>/tests/utils/fake_tournament_data/random_hhs_and_ts/handHistory/' + PLAYER_NAME + '/'
TEST_RANDOM_FAKE_TOURNAMENT_SUMMARIES_FOLDER = '<>/tests/utils/fake_tournament_data/random_hhs_and_ts/TournamentSummary/' + PLAYER_NAME + '/'
TEST_HH_FOR_POS_AND_PLR_NAME_FOLDER = '<>/tests/utils/fake_tournament_data/hh_for_position_info/'
TEST_HH_FOR_SIDE_POTS_FOLDER = '<>/tests/utils/fake_tournament_data/hh_for_side_pot/'