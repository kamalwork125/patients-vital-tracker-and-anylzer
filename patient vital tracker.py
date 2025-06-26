import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
#read file
df=pd.read_csv('vitals.csv')
print(df)
print("data fetched succesfully")
plt.plot(df['Temperature'],df['Status'],marker='o',color='yellow')
plt.title("Temperature vsStatus")
plt.ylabel("Temperature")
plt.xlabel("Status")
plt.grid(True)
plt.show()
#bar chart
plt.figure(figsize=(8,5))
sns.barplot(x='BP_Sys',y='BP_Dia',data=df)
plt.title("blood pressure comparison")
plt.ylabel("BP_Dia")
plt.xlabel("BP_Sys")
plt.show()
#boxplot
sns.boxplot(y=df['HeartRate'],color='red')
plt.title("HeartRate variarance")
plt.show()
#piechart
health=df["Status"].value_counts()
plt.pie(health,labels=health.index)
plt.title("health status")
plt.show()
#heatmap
sns.heatmap(df[['BP_Sys', 'BP_Dia', 'HeartRate']].corr(), annot=True, cmap='coolwarm')
plt.title("correlation hitmap")
plt.show()