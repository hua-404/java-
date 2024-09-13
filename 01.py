import matplotlib.pyplot as plt
import pandas as pd
import csv
from datetime import datetime
df = pd.read_csv('DXYArea1201.csv')
provinceDf = df[['provinceName','province_confirmedCount','province_suspectedCount','province_curedCount','province_deadCount','updateTime']]
USADf = provinceDf.loc[provinceDf["provinceName"]=='美国']
USADf.loc[:,'updateTime']=pd.to_datetime(USADf.loc[:,"updateTime"])
USA1201Df=USADf[USADf["updateTime"] >= datetime.strptime("2020-12-01","%Y-%m-%d")]
USASe=USA1201Df.iloc[0,:]
index = ["confirmedCount",'suspectedCount','curedCount','deadCount']
value_list = [USASe["province_confirmedCount"],
            USASe["province_suspectedCount"],
            USASe["province_curedCount"],
            USASe["province_deadCount"]]
result = list(zip(index,value_list))
fileName = "result.csv"
with open(fileName,"w",encoding="utf-8") as csv_file:
    writer = csv.writer(csv_file)
    for row in result:
        writer.writerow(row)

plt.rcParams["font.sans-serif"]=['SimHei']
bar_width = 0.6
plt.bar(index,value_list,bar_width)
plt.show()