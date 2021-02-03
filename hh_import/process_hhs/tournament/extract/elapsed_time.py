from datetime import datetime


def extract_elapsed_time_from_content(content: str) -> int:






    def get_first_hand():
        pass

    def get_last_hand():
        pass








    all_times = []

    for line in content.split('\n'):
        if ')- 2' in line:
            all_times.append('2' + line.split(')- 2')[1].replace(' UTC', ''))

    last_hand_time = datetime.strptime(all_times[-1].replace('/', '-'), '%Y-%m-%d %H:%M:%S')
    first_hand_time = datetime.strptime(all_times[0].replace('/', '-'), '%Y-%m-%d %H:%M:%S')

    duration = last_hand_time - first_hand_time
    duration_in_mn = duration.total_seconds()/60

    return round(duration_in_mn)
