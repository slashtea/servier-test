from pandas import read_csv
from collections import defaultdict
from json import dump


def read_pandas_csv(file_path, name, header=True):
    """ Function to read csv with and produce a dataframe as an output """
    df = read_csv(file_path)
    df.name = name
    return df


def pubmed_journal_search(dataframe, search_col, drug, result_dict):
    """ Function to search for the drug within the title of clinical trail and the pubmed"""
    result_dict[drug][dataframe.name] = []
    result_dict[drug]["journal"] = []
    
    for index, row in dataframe.iterrows():
        if drug.lower() in row[search_col].lower():
            # create dict for pubmed and journal.
            dict_pubmed = {"title": row[search_col], "date": row["date"]}
            dict_journal = {"journal": row["journal"], "date": row["date"]}

            # append values.
            result_dict[drug][dataframe.name].append(dict_pubmed)
            result_dict[drug]["journal"].append(dict_journal)
    return result_dict


def clinical_trial_search(dataframe, search_col, drug, result_dict):
    result_dict[drug][dataframe.name] = []
    
    for index, row in dataframe.iterrows():
        if drug.lower() in row[search_col].lower():
            dict_trials = {"title": row[search_col], "date": row["date"]}
            result_dict[drug][dataframe.name].append(dict_trials)
    return result_dict


def clean_results(drugs):
    """ Function to remove empty values """
    items_copy = drugs.items()
    for drug, results in items_copy:
        if len(results["journal"]) == 0 and len(results["pubmed"]) == 0  \
            and len(results["clinical trials"]) == 0: 
            print(drug, results)
            del drugs[drug]
    return drugs


def write_json(file_path, data, mode="w"):
    """ Function to write output graph as json file """
    with open(file_path, mode) as f:
        dump(data, f)


if __name__ == "__main__":
    # Useful vars
    drugs_results = defaultdict(dict)

    # Reading datasets
    drugs = read_pandas_csv("datasources/drugs.csv", "drugs")
    pubmed = read_pandas_csv("datasources/pubmed.csv", "pubmed")
    clinical_trials = read_pandas_csv("datasources/clinical_trials.csv", "clinical trials")

    # Build of graph
    for drug in drugs["drug"]:
        pubmed_journal_search(pubmed, "title", drug, drugs_results)
        clinical_trial_search(clinical_trials, "scientific_title", drug, drugs_results)
    
    drugs_results_cleaned = clean_results(drugs_results)
    # write_json("output.json", drugs_results_cleaned)
