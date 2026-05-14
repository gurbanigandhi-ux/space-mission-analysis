import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("mission_launches.csv")
data["Date"] = pd.to_datetime(
    data["Date"],
    format="mixed",
    utc=True
)

data["Month"] = data["Date"].dt.month_name()
print(data[["Date", "Month"]])
# getseason function groups the months to their respective seasons
def getseason (month):
    if month in("March","April","May"):
        return "Spring"
    elif month in("June","July","August"):
        return "Summer"
    elif month in("September","October","November"):
        return "Autumn"
    else:
        return "Winter"
    
data["Season"]=data["Month"].apply(getseason)
season_counts=data["Season"].value_counts()
plt.figure(figsize=(8,5))
plt.bar(season_counts.index,season_counts.values,color="steelblue")
plt.title("Space Mission Launches by Seasons")
plt.xlabel("Seasons")
plt.ylabel("Number of luanches")
plt.tight_layout()
plt.savefig("Seasons_chart.png")
plt.show()