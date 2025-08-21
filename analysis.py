import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

os.makedirs("plots", exist_ok=True)


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data", "co2_data.csv")

df = pd.read_csv(DATA_PATH)

df = df.dropna(subset=["co2", "year", "country"])  

# --- Plot 1: Global CO2 emissions trend (sum of all countries) ---
global_trend = df.groupby("year")["co2"].sum().reset_index()
plt.figure(figsize=(10, 6))
sns.lineplot(data=global_trend, x="year", y="co2", marker="o")
plt.title("Global CO₂ Emissions Trend", fontsize=14)
plt.xlabel("Year")
plt.ylabel("Total CO₂ Emissions (Million Tonnes)")
plt.savefig("plots/global_trend.png")
plt.show()

# --- Plot 2: Top 10 emitters (latest year) ---
latest_year = df["year"].max()
top_emitters = (
    df[df["year"] == latest_year]
    .groupby("country")["co2"]
    .sum()
    .nlargest(10)
    .reset_index()
)
plt.figure(figsize=(10, 6))
sns.barplot(data=top_emitters, x="co2", y="country", hue="country", palette="Reds_r", legend=False, dodge=False)
plt.title(f"Top 10 CO₂ Emitters in {latest_year}", fontsize=14)
plt.xlabel("CO₂ Emissions (Million Tonnes)")
plt.ylabel("Country")
plt.savefig("plots/top_emitters.png")
plt.show()

# --- Plot 3: Per capita emissions ---
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x="year", y="co2_per_capita", hue="continent", alpha=0.6)
plt.title("CO₂ Emissions Per Capita", fontsize=14)
plt.xlabel("Year")
plt.ylabel("CO₂ Per Capita")
plt.legend(title="Continent")
plt.savefig("plots/per_capita.png")
plt.show()

# --- Plot 4: Continent-wise emissions trend ---
continent_trend = df.groupby(["year", "continent"])["co2"].sum().reset_index()
plt.figure(figsize=(10, 6))
sns.lineplot(data=continent_trend, x="year", y="co2", hue="continent", marker="o")
plt.title("Continent-wise CO₂ Emissions Trend", fontsize=14)
plt.xlabel("Year")
plt.ylabel("Total CO₂ Emissions (Million Tonnes)")
plt.savefig("plots/continent_trend.png")
plt.show()

# --- Plot 5: Top 10 CO₂ Emitters Over Time ---
top_countries = (
    df.groupby("country")["co2"].sum().nlargest(10).index
)
top_over_time = df[df["country"].isin(top_countries)]
plt.figure(figsize=(12,6))
sns.lineplot(data=top_over_time, x="year", y="co2", hue="country")
plt.title("Top 10 CO₂ Emitters Over Time")
plt.xlabel("Year")
plt.ylabel("CO₂ Emissions (Million Tonnes)")
plt.savefig("plots/top_emitters_over_time.png")
plt.show()

# --- Plot 6: CO₂ vs CO₂ Per Capita (Scatter) ---
plt.figure(figsize=(10,6))
sns.scatterplot(data=df, x="co2", y="co2_per_capita", hue="continent", alpha=0.6)
plt.title("CO₂ vs CO₂ Per Capita")
plt.xlabel("Total CO₂ (Million Tonnes)")
plt.ylabel("CO₂ Per Capita")
plt.savefig("plots/co2_vs_per_capita.png")
plt.show()

# --- Plot 7: Distribution of CO₂ Per Capita (Histogram) ---
plt.figure(figsize=(10,6))
sns.histplot(df["co2_per_capita"], bins=50, kde=True)
plt.title("Distribution of CO₂ Per Capita Across Countries")
plt.xlabel("CO₂ Per Capita")
plt.ylabel("Frequency")
plt.savefig("plots/per_capita_distribution.png")
plt.show()
