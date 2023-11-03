import pandas as pd
import numpy as np
import seaborn as sns
import requests

#collecting the data using API from the website
Brown_TestRelease_phenotypic_url = "https://query.data.world/s/qn77fxegyhqwzn37cpmxpl3wpw6q6p?dws=00000"
with open("../../data/00-raw-data/Brown_TestRelease_phenotypic.csv", 'wb') as outfile:
  csv_content =requests.get(Brown_TestRelease_phenotypic_url, stream=True).content
  outfile.write(csv_content)

  KKI_phenotypic_url = "https://query.data.world/s/vzxx6bdmyc7a5oxp6sf4izblvaw5on?dws=00000"
with open("../../data/00-raw-data/KKI_phenotypic.csv", 'wb') as outfile:
  csv_content = requests.get(KKI_phenotypic_url, stream=True).content
  outfile.write(csv_content)

  NYU_phenotypic_url = "https://query.data.world/s/uoz4qwmiat3uui5col6tgz6t5u5cef?dws=00000"
with open("../../data/00-raw-data/NYU_phenotypic.csv", 'wb') as outfile:
  csv_content = requests.get(NYU_phenotypic_url, stream=True).content
  outfile.write(csv_content)


OHSU_phenotypic_url = "https://query.data.world/s/363ozhtlywzpoofvbjxkzblloj4blv?dws=00000"
with open("../../data/00-raw-data/OHSU_phenotypic.csv", 'wb') as outfile:
  csv_content = requests.get(OHSU_phenotypic_url, stream=True).content
  outfile.write(csv_content)


  OHSU_TestRelease_phenotypic_url = "https://query.data.world/s/wyq7rn7y76ptzo4jjue7qopttf7uk2?dws=00000"
with open("../../data/00-raw-data/OHSU_TestRelease_phenotypic.csv", 'wb') as outfile:
  csv_content = requests.get(OHSU_TestRelease_phenotypic_url, stream=True).content
  outfile.write(csv_content)


  Peking_1_phenotypic_url = "https://query.data.world/s/fdst5h6dklmpgejnevstfd7uczwewz?dws=00000"
with open("../../data/00-raw-data/Peking_1_phenotypic.csv", 'wb') as outfile:
  csv_content = requests.get(Peking_1_phenotypic_url, stream=True).content
  outfile.write(csv_content)


  Peking_1_TestRelease_phenotypic_url = "https://query.data.world/s/bq4ikki7ul2tetz2gu5jodznza5a2y?dws=00000"
with open("../../data/00-raw-data/Peking_1_TestRelease_phenotypic.csv", 'wb') as outfile:
  csv_content = requests.get(Peking_1_TestRelease_phenotypic_url, stream=True).content
  outfile.write(csv_content)

verbal_by_performance_url = "https://query.data.world/s/5thcsizuyun2ytaijudsbniiog4wpa?dws=00000"
with open("../../data/00-raw-data/verbal_by_performance.csv", 'wb') as outfile:
  csv_content = requests.get(verbal_by_performance_url, stream=True).content
  outfile.write(csv_content)
  

  Pittsburgh_phenotypic_url = "https://query.data.world/s/ypezjly5jewyaka4wopwteyrvubi6c?dws=00000"
with open("Pittsburgh_phenotypic.csv", 'wb') as outfile:
  csv_content = requests.get(Pittsburgh_phenotypic_url, stream=True).content
  outfile.write(csv_content)
