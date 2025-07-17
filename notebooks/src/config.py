from pathlib import Path

PASTA_PROJETO = Path(__file__).resolve().parents[2]

# Dados
PASTA_DADOS = PASTA_PROJETO / 'data'

DADOS_ORIGINAIS = PASTA_DADOS / 'raw' / 'predictive_maintenance.csv'
DADOS_TRATADOS = PASTA_DADOS / 'processed' / 'processed_data.csv'

# Modelos
PASTA_MODELOS = PASTA_PROJETO / 'models'
