import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def Check_Dataframe():
   print("##########COMPLETE INFO#######################")
   print("Head\n", df.head())
   print("\nInfo\n")
   df.info()
   print("\nDescribe\n", df.describe(include='all'))
   print("\nIsNull\n", df[df.isnull().any(axis = 1)])
   print("\nDataframe Column Names\n",df.columns)
   print("#################################")

df = pd.read_csv("all_data.csv")
Check_Dataframe()


#Rename the column name with unnecessary space 

df = df.rename(columns = {'Life expectancy at birth (years)':'Life_expectancy'})
print(df.columns)

#Line plot between year and life expectancy for different countries.
sns.lmplot(data=df, x="Year", y="Life_expectancy", hue="Country", palette="tab20", markers='o')
plt.xlabel("Year")
plt.ylabel("Life Expectancy (in years)")
plt.title("Life Expectancy over the years")
plt.show()

#Line plot between year and GDP for different countries.
sns.lmplot(data=df, x="Year", y="GDP", hue="Country", palette="tab20", markers='_')
plt.xlabel("Year")
plt.ylabel("GDP")
plt.title("GDP over the years")
plt.show()

#Scatter plot between GDP and Life Expectancy
sns.scatterplot(data = df, x = "GDP", y = "Life_expectancy", hue="Country")
plt.title("Relation between GDP and Life expectancy")
plt.show()
plt.clf()

for country in df.Country.unique():
   new_df = df[df["Country"] == country]
   print(f"Avg Life Expectancy in {country} is", 
         round(new_df["Life_expectancy"].mean(), 2), "years old")
   print(f"The avg GDP of the {country} is ", round(new_df["GDP"].mean(), 2))


df_corr = df[["GDP", "Life_expectancy"]]
matrix = df_corr.corr()
print(matrix)
val = matrix.loc['GDP', 'Life_expectancy']
if val >=0 and val < 0.3:
   print("Weak correlation between GDP and Life Expectancy")
elif val >= 0.3 and val < 0.6:
   print("Moderate correlation between GDP and Life Expectancy")
elif val >= 0.6 and val < 0.8:
   print("Strong correlation between GDP and Life Expectancy")
else:
   print("Very Strong correlation between GDP and Life Expectancy")



for country in df.Country.unique():
   new_df = df[df["Country"] == country]
   sns.lmplot(data=new_df, x="Year", y="GDP", hue="Country", palette="tab20", markers='o')
   plt.xlabel("Year")
   plt.ylabel("GDP")
   plt.title("GDP over the years")
   plt.show()