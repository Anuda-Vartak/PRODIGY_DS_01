import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pycountry


# Read the CSV and skip metadata rows
df = pd.read_csv("API_SP.POP.TOTL_DS2_en_csv_v2_38144.csv", skiprows=4)

df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

# STEP 4: Keep only relevant columns
df_clean = df[["Country Name", "Country Code", "2022"]].copy()
df_clean = df_clean.dropna(subset=["2022"])
df_clean["2022"] = df_clean["2022"].astype(int)
iso_countries = set(country.alpha_3 for country in pycountry.countries)
df_clean = df_clean[df_clean["Country Code"].isin(iso_countries)]

# Sort and get top 10 countries by population
top10 = df_clean.sort_values(by="2022", ascending=False).head(10)
plt.figure(figsize=(12, 6))
sns.barplot(x="2022", y="Country Name", data=top10, palette="coolwarm")
plt.title("Top 10 Most Populated Countries (2022)")
plt.xlabel("Population")
plt.ylabel("Country")
plt.tight_layout()
plt.show()