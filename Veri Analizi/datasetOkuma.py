import pandas as pd
dataset = pd.read_csv("USvideos.csv")
print(dataset)
newData = dataset.drop(["video_id","trending_date"],axis=1)
print(newData)
newData.to_csv("UsVideosNew.csv")
newData.to_csv("UsVideosNew2.csv",index=False)
"""excelSet = pd.read_excel("excelfile.xlsx")
print(excelSet)
excelSet["Column5"] = ["Emirhan","Aydın","41","94"]
print(excelSet)
excelSet.to_excel("wxcel.filenew.xlsx")
"""
new = pd.read_html("https://www.contextures.com/xlsampledata01.html",header=0)
print(new)
print(len(new))