@author: Laura
"""

import requests
URL = "https://www.ccss.sa.cr/arc/datos-abiertos/t_db_licitaciones.xlsx"
response = requests.get(URL)
open("C:\\dashboard\\datasource.xlsx", "wb").write(response.content)