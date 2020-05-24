from numpy import NaN
from pandas import read_excel


def get_dataset(dataset_name, abrangencia):
    return read_excel(f'../datasets/{dataset_name}/{abrangencia}.xls')


def generate_options(data, headers):
    options = {}
    for fil in headers:
        options[fil] = list(data[fil].unique())

    return options


def open_filter_reduce_dataset(dataset_name, abrangencia, filter_headers, result_headers):
    data = get_dataset(dataset_name, abrangencia)
    data = data[filter_headers+result_headers]
    filter_options = generate_options(data, filter_headers)
    return data, filter_options


def merge_on_headers(data1, data2, headers):
    return data1.merge(
        data2,
        right_on=headers,
        left_on=headers
    )


def reduce_on_items(data, filters):
    reduced_data = data.copy()
    for key, value in filters.items():
        reduced_data = reduced_data[reduced_data[key] == value]
        reduced_data.drop([key], axis=1, inplace=True)
    
    return reduced_data


def join_filter_dataset(
    dataset1,
    dataset2, 
    filter_headers, 
    result_headers
):
    data = merge_on_headers(dataset1, dataset2, filter_headers)
    return data[filter_headers + result_headers].replace('--', NaN).dropna() 
