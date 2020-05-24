from utils.dataset_manipulation import open_filter_reduce_dataset, reduce_on_items
from utils.graph_builder import create_bar_graph
from utils.utils import calculate_ratio

filter_headers = ['Localização', 'Rede']
result_header = 'Total Fundamental'
analysed_key = 'Localização'


# Brasil
tdi_brasil, tdi_brasil_filter_options = open_filter_reduce_dataset(
    'TDI', 
    'brasil', 
    filter_headers, 
    [result_header]
)

brasil_base_data = reduce_on_items(tdi_brasil, {'Rede': 'Total'})
rural_urban_ratio = calculate_ratio(brasil_base_data, analysed_key, result_header, 'Rural', 'Urbana')

create_bar_graph(brasil_base_data, analysed_key, result_header, rural_urban_ratio, 'Brasil', ['Rural', 'Urbana'])


# UF
tdi_uf, tdi_uf_filter_options = open_filter_reduce_dataset(
    'TDI', 
    'uf', 
    filter_headers+['UF'], 
    [result_header]
)

min_ratio = float('inf')
min_data = None
min_UF = None

max_ratio = 0
max_data = None
max_UF = None

for uf_option in tdi_uf_filter_options['UF']:
    filtered_data = reduce_on_items(tdi_uf, {'Rede': 'Total', 'UF': uf_option})
    rural_urban_ratio = calculate_ratio(filtered_data, analysed_key, result_header, 'Rural', 'Urbana')

    if rural_urban_ratio < min_ratio:
        min_ratio = rural_urban_ratio
        min_UF = uf_option
        min_data = filtered_data.copy()

    if rural_urban_ratio > max_ratio:
        max_ratio = rural_urban_ratio
        max_UF = uf_option
        max_data = filtered_data.copy()

create_bar_graph(min_data, analysed_key, result_header, 1/min_ratio, min_UF, ['Urbana', 'Rural'])
create_bar_graph(max_data, analysed_key, result_header, max_ratio, max_UF, ['Rural', 'Urbana'])