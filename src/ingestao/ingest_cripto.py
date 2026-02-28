# Importando bibliotecas 

import requests                         # requisição de API
import json                             # trabalhar com Json
from pathlib import Path                # manipular caminhos de arquivos e pastas 
from datetime import datetime as dt     # pegar data atual

# Criando campos chave 

apiKey = 'J8M9P0B2JCPHH1PM'

# sourceCurrency
srcCur = 'BTC'               # Moeda/Cripto origem que vou extrair os dados 

# convertedCurrency 
convCur = 'USD'              # Moeda/Cripto para qual a origem será convertida

repository = 'data_lake/raw'



# Fazendo requisição da API 

url = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={srcCur}&to_currency={convCur}&apikey={apiKey}'
response = requests.get(url)

#print(response)

data = response.json()


# Salvando a response da API num arquivo json, na minha pasta local 

# currentDate
curDate = dt.today().strftime('%Y-%m-%d')

output_dir = Path(repository) / srcCur 
output_dir.mkdir(parents=True, exist_ok=True)

file = output_dir / f"{srcCur}_{curDate}.json" 

with file.open("w") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

#print(file.resolve())
#print(data)

# teste para commit