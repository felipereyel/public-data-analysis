from utils.dataset_manipulation import get_dataset, generate_options, join_filter_dataset
from utils.graph_builder import create_disper_graph

filter_headers = ['Região', 'UF', 'Código do Município', 'Localização', 'Rede']
result_headers = ['TOTAL FUNDAMENTAL 8 E 9 ANOS', 'Total Aprovação Fundamental']

hora_aula = get_dataset('hora_aula', 'municipio')
aprovacao = get_dataset('aprovacao', 'municipio')
filter_options = generate_options(hora_aula, filter_headers)
hora_aprovacao_dataset = join_filter_dataset(hora_aula, aprovacao, filter_headers, result_headers)

create_disper_graph(hora_aprovacao_dataset, result_headers, 'Brasil')

for regiao in filter_options['Região']:
    regiao_dataset = hora_aprovacao_dataset[hora_aprovacao_dataset['Região'] == regiao]
    create_disper_graph(regiao_dataset, result_headers, regiao)
