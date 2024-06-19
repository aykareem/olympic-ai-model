import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

teams = pd.read_csv("teams.csv")
pd.set_option('display.max_columns', 100)
teams = teams[["team", "country", "year", "athletes", "age", "prev_medals", "medals"]]

corr = teams.corr(numeric_only=True)["medals"]
print(corr)

sns.lmplot(x="athletes", y="medals", data=teams, fit_reg=True, ci=True)
plt.show()