

def finished_time(content: str) -> str:
    all_times = []
    for line in content.split('\n'):
        if ')- 2' in line:
            all_times.append('2' + line.split(')- 2')[1].replace(' UTC', ''))
    return all_times[-1]
