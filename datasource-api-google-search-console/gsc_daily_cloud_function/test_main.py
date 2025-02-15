
from main import run
import datetime


def test_main():
    '''Test main locally'''

    # construct input variables
    site = "bikelanes.com"
    site = "errorsolutions.tech"
    BQ_DATASET_NAME = 'data_winners_dataset'
    BQ_TABLE_NAME = 'gsc_daily_table'

    # if testing locally
    from unittest.mock import Mock
    data = {
        'site': site, 
        'BQ_DATASET_NAME':BQ_DATASET_NAME, 
        'BQ_TABLE_NAME':BQ_TABLE_NAME,
        'start_date': '2022-06-06',
        'n_days_back':60
    }
    request = Mock(get_json=Mock(return_value=data), args=data)
    res = run(request)

    True