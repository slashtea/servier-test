import pytest
import pandas
from ..data_prep import clinical_trial_search
from collections import defaultdict


@pytest.fixture(scope="module")
def input_df():
    data = {
        "scientific_title": "Use of Diphenhydramine as an Adjunctive Sedative \
            for Colonoscopy in Patients Chronically on Opioids",
        "date": "1 January 2020"
    }
    df = pandas.DataFrame(data, index=[0])
    df.name = "clinical trials"
    return df


def test_clinical_trial_search_type_and_key(input_df):
    drug="Diphenhydramine"
    search_col="scientific_title"                        
    result_dict = defaultdict(dict)
    result = clinical_trial_search(input_df, search_col, drug, result_dict)
    assert type(result) == defaultdict
    assert list(result.keys()) == [drug]


def test_read_csv_file(mocker):
    mocker.patch("pandas.read_csv")
    pandas.read_csv("../datasources/drugs.csv")
    pandas.read_csv.assert_called_once_with("../datasources/drugs.csv")