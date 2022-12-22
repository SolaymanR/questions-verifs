from js import document 

num_exam = 23

document.getElementById('titre').innerHTML = f"Examen numéro {num_exam}"

import pandas as pd
from pathlib import Path

excel_data = pd.read_excel(Path("tableau-question.xlsx"))
excel_data = excel_data.drop(range(3,len(excel_data),4))
a = excel_data.set_index(["N°", "Type"])
new_index = []
for (my_num, my_type) in a.index:
    if pd.notna(my_num):
        last_real_num = my_num
    if isinstance(last_real_num, str):
        last_real_num = last_real_num.replace("\net", "")
    else:
        last_real_num = str(last_real_num)
    new_index.append((last_real_num, my_type))
df = excel_data.set_index(new_multi_index).drop(["N°", "Type"], axis=1)