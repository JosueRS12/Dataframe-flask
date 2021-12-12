import pandas as pd
from sodapy import Socrata

client = Socrata("www.datos.gov.co", None)

results = client.get("sdvb-4x4j", limit=1000000)
# qasc-uuup
# sdvb-4x4j
