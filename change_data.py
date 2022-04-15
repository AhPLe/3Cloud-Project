#format data

import pandas as pd
file = 'HVAC.csv'

pcsv = pd.read_csv(file, header = 0)
print(pcsv.iloc[:40])
pcsv = pcsv.sort_values(by='System')
print(pcsv.iloc[:40])

#reorder columns
cols = pcsv.columns.tolist()
#['Date', 'Time', 'TargetTemp', 'ActualTemp', 'System', 'SystemAge', 'BuildingID']

print(cols)
#cols = cols[-3:] + cols[:-3]
num = 6
cols = cols[num:num + 1] + cols[:num] + cols[num+1:]
print(cols)
pcsv = pcsv[cols]

out_file = 'HVAC_sorted_building.csv'
pcsv.to_csv(out_file, index = False)

# s = ''
# with open(out_file) as f:
    # for line in f:
        # s = s + '"' + line.replace('\n', '\\n"\n')
        
# fout = 'HVAC_formatted.csv'
# with open(fout, 'w+') as f:
    # f.write(s)