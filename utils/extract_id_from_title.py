
def extract_id_from_title(title: str):
    return title.split('SITGOID-G')[1].split(' TN')[0].split('T')[0]
