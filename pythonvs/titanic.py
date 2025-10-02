import pandas as pd
import matplotlib.pyplot as mp

vs=pd.read_csv("genderdata.csv")

vs.rename(columns={"PassengerId":"Id"},inplace=True)
vs.rename(columns={"Survived":"Status"},inplace=True)

print(vs.head())
print(vs.info())
print(vs.shape)

top_survivers=vs[vs['Status']==1].head(10)
print(f"Top 10 survived\n{top_survivers}")

non_survivers=vs[vs['Status']==0].head(10)
print(f"Top 10 non survivers\n{non_survivers}")

survivors_count=len(vs[vs["Status"]==1])
nonsurvivors_count=len(vs[vs["Status"]==0])
print(f"total survivers= {survivors_count}\n total non survivors= {nonsurvivors_count}")

count=vs["Status"].value_counts()
print(count)

total=len(vs)
print(total)
survivors_percentage=(survivors_count/total)*100

nonsurvivors_percentage=(nonsurvivors_count/total)*100
print(f"Percentage of survivors = {survivors_percentage:.2f}/n Percentage of Non Survivors = {nonsurvivors_percentage:.2f}")

count.plot(kind='bar',color=["Blue","Black"])
mp.xlabel("Status")
mp.ylabel("count of survivors and non survivors")
mp.title("Titanic Bar chart")
mp.show()