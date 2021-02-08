
def id(title: str) -> int:
    return int(title.split('SITGOID-G')[1].split(' TN')[0].split('T')[0])