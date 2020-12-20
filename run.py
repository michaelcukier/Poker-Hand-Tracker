
from hh_import.raw_hh_to_dict.run import run as raw_hh_to_dict
raw_hh_to_dict_ = raw_hh_to_dict()


from hh_import.dict_to_clean_data.run import run as dict_to_clean_data
dict_to_clean_data_ = dict_to_clean_data(raw_hh_to_dict_)

print(dict_to_clean_data_)