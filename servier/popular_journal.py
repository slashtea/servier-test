import json


def read_file(file_path: str) -> json:
    """ Reads a json file """
    try:
        with open(file_path, mode="r") as f:
            return json.load(f)
    except Exception as e:
        print(f"Exception {e}")


def find_popular_journal(data: dict) -> list:
    """ Iterate over all journal values and increment if value exists
    Returns one or many most popular journal having the maximum number
    of citations. 
    """
    occurences = {}
    for k, v in data.items():
        for j in v["journal"]:
            if j["journal"] in occurences.keys():
                occurences[j["journal"]] += 1
            else:
                occurences[j["journal"]] = 1
    
    max_value = max(occurences.values())
    return [k for k, v in occurences.items() if v == max_value]


if __name__ == "__main__":
    INPUT_DIR = "../outputs"
    json_graph = read_file(f"{INPUT_DIR}/output.json")
    most_popular_journal = find_popular_journal(json_graph)
    print(most_popular_journal)