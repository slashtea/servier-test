import json


def read_file(file_path):
    """ Reads a json file """
    with open(file_path, mode="r") as f:
        return json.load(f)


def find_popular_journal(data):
    """ Iterate over all journal values and increment if value exists
    Returns first most popular element sorted by number of publications 
    """
    occurences = {}
    for k, v in data.items():
        for j in v["journal"]:
            if j["journal"] in occurences.keys():
                occurences[j["journal"]] += 1
            else:
                occurences[j["journal"]] = 1
    return sorted(occurences, lambda journal: journal[1], reverse=True)[0]


if __name__ == "__main__":
    json_graph = read_file("output.json")
    most_popular_journal = find_popular_journal(json_graph)
    print(most_popular_journal)