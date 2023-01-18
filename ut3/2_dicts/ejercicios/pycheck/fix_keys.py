# ********************
# LA CLAVE ES LA CLAVE
# ********************


def run(items: dict) -> dict:
    fitems = {}
    for item, value in items.items():
        replace_times = item.count(" ")
        replaced_item = item.replace(" " * replace_times, "")
        fitems[replaced_item] = value 
    return fitems


if __name__ == '__main__':
    run({'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']})
