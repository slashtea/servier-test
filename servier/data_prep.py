from pandas import read_csv, DataFrame
from collections import defaultdict
from json import dump
import logging
from dateutil import parser


def read_pandas_csv(file_path: str, name: str, header=True) -> DataFrame:
    """ Function to read csv with and produce a dataframe as an output """
    try:
        df = read_csv(file_path)
        df.name = name
        return df
    except Exception as e:
        logging.error(e)



def pubmed_journal_search(dataframe: DataFrame, search_col: str, drug: str,
                          result_dict: dict) -> dict:
    """ Function gets pubmed with a drug mention in the title
        and gets the associated journal.
    """
    try:
        for index, row in dataframe.iterrows():
            if drug.lower() in row[search_col].lower():
                # create dict for pubmed and journal.
                dict_pubmed = {"title": row[search_col],
                                "date": parser.parse(row["date"]).strftime("%d/%m/%Y")}
                dict_journal = {"journal": row["journal"],
                                "date": parser.parse(row["date"]).strftime("%d/%m/%Y")}

                # append values.
                result_dict[drug][dataframe.name].append(dict_pubmed)
                result_dict[drug]["journal"].append(dict_journal)
        return result_dict
    except Exception as e:
        logging.error(e)


def clinical_trial_search(dataframe: DataFrame, search_col: str, drug: str,
                          result_dict: dict) -> dict:
    """ Function gets clinical trials with a drug mention in the title """
    try:        
        for index, row in dataframe.iterrows():
            if drug.lower() in row[search_col].lower():
                dict_trials = {"title": row[search_col],
                               "date": parser.parse(row["date"]).strftime("%d/%m/%Y")}
                result_dict[drug][dataframe.name].append(dict_trials)
        return result_dict
    except Exception as e:
        logging.error(e)


def write_json(file_path, data, mode="w"):
    """ Function to write output graph as json file """
    with open(file_path, mode) as f:
        dump(data, f)


if __name__ == "__main__":
    # logging
    logging.basicConfig(filename="logs.log", encoding="utf-8", level=logging.DEBUG)

    # Useful vars
    OUTPUT_DIR = "../outputs"
    INPUT_DIR = "../datasources"
    drugs_results = defaultdict(lambda: defaultdict(list))

    # Reading datasets
    drugs = read_pandas_csv(f"{INPUT_DIR}/drugs.csv", "drugs")
    pubmed = read_pandas_csv(f"{INPUT_DIR}/pubmed.csv", "pubmed")
    clinical_trials = read_pandas_csv(f"{INPUT_DIR}/clinical_trials.csv",
                                      "clinical trials")

    # Build of graph
    for drug in drugs["drug"]:
        pubmed_journal_search(pubmed, "title", drug, drugs_results)
        clinical_trial_search(clinical_trials, "scientific_title", drug,
                              drugs_results)
    
    # Writing graph to JSON.
    write_json(f"{OUTPUT_DIR}/output.json", drugs_results)