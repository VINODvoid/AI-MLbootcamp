import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Set style
plt.style.use("seaborn-v0_8-darkgrid")
sns.set_palette("husl")

print("🏠 Loading Airbnb Data...")

# ==========================================
# 1. LOAD & EXPLORE DATA
# ==========================================

# Load data
df = pd.read_csv("listings.csv")

print(f"\n📊 Dataset Shape: {df.shape}")
print(f"Total Listings: {len(df):,}")

# Check first few rows
print("\n👀 First 5 Listings:")
print(df.head())

# Check columns
print(f"\n📋 Total Columns: {len(df.columns)}")
print("Key columns:", df.columns.tolist()[:10])

# ==========================================
# 2. DATA CLEANING
# ==========================================

print("\n🧹 Cleaning Data...")

# Select important columns (adjust based on what's in your CSV)
columns_to_keep = [
    "id",
    "name",
    "host_name",
    "neighbourhood",
    "latitude",
    "longitude",
    "room_type",
    "price",
    "minimum_nights",
    "number_of_reviews",
    "reviews_per_month",
    "availability_365",
]

# Keep only columns that exist
columns_to_keep = [col for col in columns_to_keep if col in df.columns]
df = df[columns_to_keep]

# Clean price column (remove $ and commas, convert to float)
if "price" in df.columns:
    df["price"] = df["price"].replace("[\$,]", "", regex=True).astype(float)

# Remove listings with price = 0 or too high (outliers)
df = df[(df["price"] > 0) & (df["price"] < 1000)]

# Fill missing values
df["reviews_per_month"].fillna(0, inplace=True)

print(f"✅ Clean dataset: {len(df):,} listings")

# ==========================================
# 3. BASIC STATISTICS
# ==========================================

print("\n" + "=" * 50)
print("📈 BASIC STATISTICS")
print("=" * 50)

print(f"\nAverage Price: ${df['price'].mean():.2f}")
print(f"Median Price: ${df['price'].median():.2f}")
print(f"Min Price: ${df['price'].min():.2f}")
print(f"Max Price: ${df['price'].max():.2f}")
print(f"Std Deviation: ${df['price'].std():.2f}")

print(f"\nTotal Neighborhoods: {df['neighbourhood'].nunique()}")
print(f"Total Hosts: {df['host_name'].nunique()}")

# ==========================================
# 4. KEY INSIGHTS
# ==========================================

print("\n" + "=" * 50)
print("🔍 KEY INSIGHTS")
print("=" * 50)

# Insight 1: Room type distribution
print("\n1️⃣ Listings by Room Type:")
room_counts = df["room_type"].value_counts()
print(room_counts)

# Insight 2: Average price by room type
print("\n2️⃣ Average Price by Room Type:")
price_by_room = df.groupby("room_type")["price"].mean().sort_values(ascending=False)
print(price_by_room.round(2))

# Insight 3: Top 5 most expensive neighborhoods
print("\n3️⃣ Top 5 Most Expensive Neighborhoods:")
top_neighborhoods = (
    df.groupby("neighbourhood")["price"].mean().sort_values(ascending=False).head()
)
print(top_neighborhoods.round(2))

# Insight 4: Most reviewed listings
print("\n4️⃣ Top 5 Most Reviewed Listings:")
most_reviewed = df.nlargest(5, "number_of_reviews")[
    ["name", "neighbourhood", "price", "number_of_reviews"]
]
print(most_reviewed)

# ==========================================
# 5. VISUALIZATIONS
# ==========================================

print("\n📊 Creating Visualizations...")

# Create figure with subplots
fig = plt.figure(figsize=(16, 12))

# Visualization 1: Price Distribution
ax1 = plt.subplot(3, 3, 1)
plt.hist(df["price"], bins=50, edgecolor="black", alpha=0.7)
plt.xlabel("Price ($)")
plt.ylabel("Frequency")
plt.title("Price Distribution")
plt.axvline(
    df["price"].mean(),
    color="red",
    linestyle="--",
    label=f'Mean: ${df["price"].mean():.2f}',
)
plt.axvline(
    df["price"].median(),
    color="green",
    linestyle="--",
    label=f'Median: ${df["price"].median():.2f}',
)
plt.legend()

# Visualization 2: Room Type Counts
ax2 = plt.subplot(3, 3, 2)
room_counts.plot(kind="bar", color=["#FF6B6B", "#4ECDC4", "#45B7D1"])
plt.xlabel("Room Type")
plt.ylabel("Number of Listings")
plt.title("Listings by Room Type")
plt.xticks(rotation=45)

# Visualization 3: Price by Room Type (Box Plot)
ax3 = plt.subplot(3, 3, 3)
df.boxplot(column="price", by="room_type", ax=ax3)
plt.xlabel("Room Type")
plt.ylabel("Price ($)")
plt.title("Price Distribution by Room Type")
plt.suptitle("")

# Visualization 4: Top 10 Neighborhoods by Average Price
ax4 = plt.subplot(3, 3, 4)
top_10_neighborhoods = (
    df.groupby("neighbourhood")["price"].mean().sort_values(ascending=False).head(10)
)
top_10_neighborhoods.plot(kind="barh", color="coral")
plt.xlabel("Average Price ($)")
plt.ylabel("Neighborhood")
plt.title("Top 10 Most Expensive Neighborhoods")

# Visualization 5: Price vs Number of Reviews (Scatter)
ax5 = plt.subplot(3, 3, 5)
plt.scatter(df["number_of_reviews"], df["price"], alpha=0.3, s=10)
plt.xlabel("Number of Reviews")
plt.ylabel("Price ($)")
plt.title("Price vs Reviews")

# Visualization 6: Availability Distribution
ax6 = plt.subplot(3, 3, 6)
plt.hist(df["availability_365"], bins=50, edgecolor="black", alpha=0.7, color="green")
plt.xlabel("Days Available per Year")
plt.ylabel("Frequency")
plt.title("Availability Distribution")

# Visualization 7: Minimum Nights Distribution
ax7 = plt.subplot(3, 3, 7)
min_nights_filtered = df[df["minimum_nights"] <= 30]  # Filter outliers
plt.hist(
    min_nights_filtered["minimum_nights"],
    bins=30,
    edgecolor="black",
    alpha=0.7,
    color="purple",
)
plt.xlabel("Minimum Nights")
plt.ylabel("Frequency")
plt.title("Minimum Stay Requirements")

# Visualization 8: Reviews per Month Distribution
ax8 = plt.subplot(3, 3, 8)
reviews_filtered = df[df["reviews_per_month"] > 0]  # Only active listings
plt.hist(
    reviews_filtered["reviews_per_month"],
    bins=50,
    edgecolor="black",
    alpha=0.7,
    color="orange",
)
plt.xlabel("Reviews per Month")
plt.ylabel("Frequency")
plt.title("Review Activity Distribution")

# Visualization 9: Correlation Heatmap
ax9 = plt.subplot(3, 3, 9)
# Select numeric columns for correlation
numeric_cols = [
    "price",
    "minimum_nights",
    "number_of_reviews",
    "reviews_per_month",
    "availability_365",
]
correlation = df[numeric_cols].corr()
sns.heatmap(correlation, annot=True, fmt=".2f", cmap="coolwarm", center=0)
plt.title("Feature Correlations")

plt.tight_layout()
plt.savefig("airbnb_analysis_dashboard.png", dpi=300, bbox_inches="tight")
print("✅ Saved: airbnb_analysis_dashboard.png")

# ==========================================
# 6. ADVANCED ANALYSIS
# ==========================================

# Create a separate figure for geographic visualization
fig2 = plt.figure(figsize=(12, 8))

plt.scatter(
    df["longitude"], df["latitude"], c=df["price"], cmap="YlOrRd", alpha=0.5, s=5
)
plt.colorbar(label="Price ($)")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Geographic Distribution of Listings (Color = Price)")
plt.savefig("airbnb_map.png", dpi=300, bbox_inches="tight")
print("✅ Saved: airbnb_map.png")

# ==========================================
# 7. EXPORT INSIGHTS TO CSV
# ==========================================

print("\n💾 Exporting Insights...")

# Summary statistics by neighborhood
neighborhood_summary = (
    df.groupby("neighbourhood")
    .agg(
        {"price": ["mean", "median", "min", "max", "count"], "number_of_reviews": "sum"}
    )
    .round(2)
)

neighborhood_summary.columns = ["_".join(col) for col in neighborhood_summary.columns]
neighborhood_summary = neighborhood_summary.sort_values("price_mean", ascending=False)
neighborhood_summary.to_csv("neighborhood_insights.csv")
print("✅ Saved: neighborhood_insights.csv")

# Top deals (high reviews, low price)
df["value_score"] = df["number_of_reviews"] / (
    df["price"] + 1
)  # +1 to avoid division by zero
top_deals = df.nlargest(20, "value_score")[
    ["name", "neighbourhood", "price", "number_of_reviews", "room_type"]
]
top_deals.to_csv("top_value_listings.csv", index=False)
print("✅ Saved: top_value_listings.csv")

# ==========================================
# 8. FINAL SUMMARY
# ==========================================

print("\n" + "=" * 50)
print("🎉 ANALYSIS COMPLETE!")
print("=" * 50)

print("\n📁 Files Created:")
print("  1. airbnb_analysis_dashboard.png (9 visualizations)")
print("  2. airbnb_map.png (geographic distribution)")
print("  3. neighborhood_insights.csv (data by neighborhood)")
print("  4. top_value_listings.csv (best deals)")

print("\n💡 Key Findings:")
print(f"  • Analyzed {len(df):,} listings")
print(f"  • Average price: ${df['price'].mean():.2f}")
print(f"  • Most common room type: {room_counts.index[0]}")
print(
    f"  • Most expensive neighborhood: {top_neighborhoods.index[0]} (${top_neighborhoods.iloc[0]:.2f})"
)
print(f"  • Price range: ${df['price'].min():.2f} - ${df['price'].max():.2f}")


print("\n" + "=" * 50)
