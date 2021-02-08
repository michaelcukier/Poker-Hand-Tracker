# from utils.run_sql_command import run_sql_command


import unittest


# from GLOBAL_VARIABLES import FAKE_HAND_HISTORY_FOLDER
# from import_new_tournament.get_new_filenames.tasks.query_local_filesystem import query_local_filesystem


from utils_and_test_data.create_fake_database.create_fake_database import CreateFakeDatabase

class test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.database = CreateFakeDatabase(
            db_name='myDB',
            table_name='tournaments',
            columns_labels=['buyin', 'prize', 'lol'],
            data=[
                ['12', 'row1 col2', 'row1 col3'],
                ['row2 col1', 'row2 col2', 'row2 col3'],
                ['row3 col1', 'row3 col2', 'row3 col3'],
            ])

    def test_query_local_database(self):
        pass
        # files = query_local_filesystem(FAKE_HAND_HISTORY_FOLDER)
        #
        # self.assertEqual(
        #     len(files),
        #     12)

#
#
#
# def query_local_database(filenames: list) -> list:
#     '''
#     remove filenames already in the db
#     '''
#
#     def extract_id_from_title(title: str):
#         return title.split('SITGOID-G')[1].split(' TN')[0].split('T')[0]
#
#     hh_in_db = run_sql_command('''
#         SELECT
#         ID
#         FROM
#         tournaments
#     ''', unique_items=True)
#
#     filtered = []
#     for file_name in filenames:
#         tournament_id = extract_id_from_title(file_name)
#         if tournament_id not in hh_in_db:
#             filtered.append(file_name)
#     return filtered
