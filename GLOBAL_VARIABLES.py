# edit those fields:
PLAYER_NAME = 'PotNoodle99912'
HAND_HISTORY_FOLDER = '/Users/cukiermichael/Downloads/AmericasCardroom/handHistory/' + PLAYER_NAME + '/'
TOURNEY_SUMMARY_FOLDER = '/Users/cukiermichael/Downloads/AmericasCardroom/TournamentSummary/' + PLAYER_NAME + '/'
TOURNAMENTS_TO_EXTRACT = {
    "$0{FULLSTOP}50 Hold'Em Turbo": 0.55,
    "$1{FULLSTOP}50 Hold'Em Turbo": 1.65,
    "$3 Hold'Em Turbo - On Demand": 3.30,
    "$6 Hold'Em Turbo - On Demand": 6.60}
FOLDER_PLOT_DUMP = "/Users/cukiermichael/Dropbox/backup/projects/2020/pokerHUDv2/plots_dump/"
DATABASE_LOCATION = '/Users/cukiermichael/Dropbox/backup/projects/2020/pokerHUDv2/db.db'

# don't edit those:
TEST_RANDOM_HAND_HISTORIES_FOLDER = '/Users/cukiermichael/Dropbox/backup/projects/2020/pokerHUDv2/tests/utils/fake_tournament_data/random_hhs_and_ts/handHistory/' + PLAYER_NAME + '/'
TEST_RANDOM_FAKE_TOURNAMENT_SUMMARIES_FOLDER = '/Users/cukiermichael/Dropbox/backup/projects/2020/pokerHUDv2/tests/utils/fake_tournament_data/random_hhs_and_ts/TournamentSummary/' + PLAYER_NAME + '/'
TEST_HH_FOR_POS_AND_PLR_NAME_FOLDER = '/Users/cukiermichael/Dropbox/backup/projects/2020/pokerHUDv2/tests/utils/fake_tournament_data/hh_for_position_info/'
TEST_HH_FOR_SIDE_POTS_FOLDER = '/Users/cukiermichael/Dropbox/backup/projects/2020/pokerHUDv2/tests/utils/fake_tournament_data/hh_for_side_pot/'
