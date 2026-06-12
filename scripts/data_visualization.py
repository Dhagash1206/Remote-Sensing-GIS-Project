
"""
Day 7 - Data Visualization and Analysis in Python
Summer Training Programme - Remote Sensing & GIS

- Loading and plotting geospatial vector data
- Choropleth maps using column values
- Time-series line and bar charts
- Scatter plots and correlation analysis
- Exporting statistical summaries and plots
"""

import os
import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd

SHAPEFILE_PATH = os.path.join(
    os.path.dirname(__file__), "..", "data", "2011_Dist.shp"
)

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "outputs")
os.makedirs(OUTPUT_DIR, exist_ok=True)


def load_shapefile(path: str) -> gpd.GeoDataFrame:

    gdf = gpd.read_file(path)
    print(f"[INFO] Loaded shapefile with {len(gdf)} records")
    print(gdf.head())
    return gdf


def plot_district_boundaries(gdf: gpd.GeoDataFrame) -> None:

    gdf.plot(figsize=(10, 10), edgecolor="black")
    plt.title("India District Boundaries")
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "01_district_boundaries.png"), dpi=150)
    plt.show()
    print("[INFO] Saved: 01_district_boundaries.png")


def plot_choropleth(gdf: gpd.GeoDataFrame) -> None:

    if "mean_value" not in gdf.columns:
        print("[WARN] 'mean_value' column not found. Skipping choropleth.")
        return

    gdf.plot(
        column="mean_value",
        cmap="YlOrRd",
        legend=True,
        figsize=(10, 10),
        edgecolor="black",
        linewidth=0.3
    )
    plt.title("District-wise Mean Raster Values")
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "02_choropleth_mean_value.png"), dpi=150)
    plt.show()
    print("[INFO] Saved: 02_choropleth_mean_value.png")


def create_time_series() -> pd.DataFrame:

    ts = pd.DataFrame({
        "Year": [2022, 2023, 2024, 2025],
        "Mean_Value": [10.5, 11.2, 12.4, 13.1],
        "Another_Value": [9.8, 10.6, 11.5, 12.0]
    })
    print("\n[INFO] Time-series data:")
    print(ts)
    return ts


def plot_line_chart(ts: pd.DataFrame) -> None:

    plt.figure(figsize=(8, 5))
    plt.plot(
        ts["Year"].astype(str),
        ts["Mean_Value"],
        marker="o",
        linewidth=2,
        color="steelblue"
    )
    plt.title("Time-Series Change in Mean Raster Value")
    plt.xlabel("Year")
    plt.ylabel("Mean Raster Value")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "03_time_series_line.png"), dpi=150)
    plt.show()
    print("[INFO] Saved: 03_time_series_line.png")


def plot_bar_chart(ts: pd.DataFrame) -> None:

    plt.figure(figsize=(8, 5))
    plt.bar(ts["Year"].astype(str), ts["Mean_Value"], color="coral")
    plt.title("Year-wise Mean Raster Values")
    plt.xlabel("Year")
    plt.ylabel("Mean Raster Value")
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "04_bar_chart.png"), dpi=150)
    plt.show()
    print("[INFO] Saved: 04_bar_chart.png")


def plot_scatter(ts: pd.DataFrame) -> None:
    plt.figure(figsize=(7, 5))
    plt.scatter(ts["Mean_Value"], ts["Another_Value"], color="purple", s=80)
    plt.title("Relationship Between Two Variables")
    plt.xlabel("Mean Value")
    plt.ylabel("Another Variable")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "05_scatter_plot.png"), dpi=150)
    plt.show()
    print("[INFO] Saved: 05_scatter_plot.png")


def compute_correlation(ts: pd.DataFrame) -> None:
    correlation = ts["Mean_Value"].corr(ts["Another_Value"])
    print(f"\n[INFO] Pearson Correlation: {correlation:.4f}")


def export_summary(ts: pd.DataFrame) -> None:
    summary = ts.describe()
    print("\n[INFO] Statistical Summary:")
    print(summary)

    csv_path = os.path.join(OUTPUT_DIR, "Statistical_Summary.csv")
    summary.to_csv(csv_path)
    print(f"[INFO] Saved: Statistical_Summary.csv -> {csv_path}")


if __name__ == "__main__":
    gdf = load_shapefile(SHAPEFILE_PATH)

    plot_district_boundaries(gdf)
    plot_choropleth(gdf)

    ts = create_time_series()
    plot_line_chart(ts)
    plot_bar_chart(ts)
    plot_scatter(ts)
    compute_correlation(ts)
    export_summary(ts)

    print("\n[DONE] Day 7 analysis complete. Check /outputs folder.")
