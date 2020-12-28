from hh_import.raw_hh_to_dict.run import run as raw_hh_to_dict
from hh_import.dict_to_clean_data.run import run as dict_to_clean_data
from hh_import.store_hh_sqlite.run import run as store_hh_sqlite


def wrapper_import_new():
    raw_hh_to_dict_ = raw_hh_to_dict()
    dict_to_clean_data_ = dict_to_clean_data(raw_hh_to_dict_, log_progress=True, early_stop_for_test=True)
    print('Found', len(dict_to_clean_data_), 'new tournament(s) to add')
    store_hh_sqlite(dict_to_clean_data_)
