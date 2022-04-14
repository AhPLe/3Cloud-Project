#format data

import pandas as pd
# file = 'HVAC.csv'

# pcsv = pd.read_csv(file, header = 0)
# print(pcsv.iloc[:10])
# pcsv = pcsv.sort_values(by='System')
# print(pcsv.iloc[:10])
out_file = 'HVAC_sorted_sys.csv'
# pcsv.to_csv(out_file)

s = ''
with open(out_file) as f:
    for line in f:
        s = s + '"' + line.replace('\n', '\\n"\n')
        
fout = 'HVAC_formatted.csv'
with open(fout, 'w+') as f:
    f.write(s)