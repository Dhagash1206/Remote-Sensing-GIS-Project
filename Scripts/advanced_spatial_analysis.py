"""
Advanced Spatial Analysis using GIS and Python
Summer Training Programme - Remote Sensing & GIS

- Loading India district shapefile
- CRS inspection and reprojection (EPSG:4326 -> EPSG:3857)
- Buffer analysis (10km around districts)
- Overlay operations: Intersection and Union
- Attribute filtering (Rajasthan state)
- Spatial query: Districts touching Rajasthan boundary
"""

import os
import warnings
import geopandas as gpd
import matplotlib.pyplot as plt

warnings.filterwarnings("ignore", category=DeprecationWarning)

SHAPEFILE_PATH = os.path.join(
    os.path.dirname(__file__), "..", "data", "2011_Dist.shp"
)

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "outputs")
os.makedirs(OUTPUT_DIR, exist_ok=True)


def load_shapefile(path: str) -> gpd.GeoDataFrame:

    gdf = gpd.read_file(path)
    print(f"[INFO] Loaded {len(gdf)} districts")
    print(gdf.head())
    return gdf


def plot_boundaries(gdf: gpd.GeoDataFrame) -> None:

    gdf.plot(figsize=(10, 10), edgecolor="black")
    plt.title("India District Boundaries")
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "d8_01_district_boundaries.png"), dpi=150)
    plt.show()
    print("[INFO] Saved: d8_01_district_boundaries.png")


def reproject(gdf: gpd.GeoDataFrame) -> gpd.GeoDataFrame:

    print(f"\n[INFO] Original CRS: {gdf.crs}")
    gdf_projected = gdf.to_crs(epsg=3857)
    print(f"[INFO] Projected CRS: {gdf_projected.crs}")
    return gdf_projected


def buffer_analysis(gdf_projected: gpd.GeoDataFrame) -> gpd.GeoSeries:

    buffered = gdf_projected.buffer(10000)  # 10,000 metres = 10 km
    print(f"\n[INFO] Buffer created for {len(buffered)} districts")
    print(buffered.head())
    return buffered


def plot_buffer(gdf_projected: gpd.GeoDataFrame, buffered: gpd.GeoSeries) -> None:
    fig, ax = plt.subplots(figsize=(10, 10))

    gdf_projected.plot(ax=ax, color="lightblue", edgecolor="black")

    buffered.plot(ax=ax, color="red", alpha=0.3)

    plt.title("District Buffer Analysis (10km)")
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "d8_02_buffer_analysis.png"), dpi=150)
    plt.show()
    print("[INFO] Saved: d8_02_buffer_analysis.png")


def overlay_intersection(gdf_projected: gpd.GeoDataFrame) -> gpd.GeoDataFrame:

    intersection = gpd.overlay(
        gdf_projected,
        gdf_projected,
        how="intersection",
        keep_geom_type=False 
    )
    print(f"\n[INFO] Intersection result: {len(intersection)} records")
    print(intersection.head())
    return intersection


def overlay_union(gdf_projected: gpd.GeoDataFrame) -> gpd.GeoDataFrame:

    union_result = gpd.overlay(
        gdf_projected,
        gdf_projected,
        how="union",
        keep_geom_type=False
    )
    print(f"\n[INFO] Union result: {len(union_result)} records")
    print(union_result.head())
    return union_result


def plot_union(union_result: gpd.GeoDataFrame) -> None:
    union_result.plot(figsize=(10, 10), color="lightgreen", edgecolor="black")
    plt.title("Union Overlay Result")
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "d8_03_union_overlay.png"), dpi=150)
    plt.show()
    print("[INFO] Saved: d8_03_union_overlay.png")


def filter_state(gdf: gpd.GeoDataFrame, state_name: str) -> gpd.GeoDataFrame:
    state_gdf = gdf[gdf["ST_NM"] == state_name]
    print(f"\n[INFO] {state_name} has {len(state_gdf)} districts")
    print(state_gdf.head())
    return state_gdf


def plot_state(state_gdf: gpd.GeoDataFrame, state_name: str) -> None:
    state_gdf.plot(figsize=(8, 8), color="orange", edgecolor="black")
    plt.title(f"{state_name} Districts")
    plt.tight_layout()
    filename = f"d8_04_{state_name.lower()}_districts.png"
    plt.savefig(os.path.join(OUTPUT_DIR, filename), dpi=150)
    plt.show()
    print(f"[INFO] Saved: {filename}")


def find_touching(gdf: gpd.GeoDataFrame, state_gdf: gpd.GeoDataFrame) -> gpd.GeoDataFrame:

    state_union = state_gdf.union_all()  # combine all state polygons into one
    touching = gdf[gdf.touches(state_union)]
    print(f"\n[INFO] Districts touching Rajasthan: {len(touching)}")
    print(touching.head())
    return touching


def plot_touching(
    state_gdf: gpd.GeoDataFrame,
    touching: gpd.GeoDataFrame,
    state_name: str
) -> None:

    fig, ax = plt.subplots(figsize=(10, 10))

    state_gdf.plot(ax=ax, color="orange", edgecolor="black")
    touching.plot(ax=ax, color="red", edgecolor="black")

    plt.title(f"Districts Touching {state_name}")
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "d8_05_touching_districts.png"), dpi=150)
    plt.show()
    print("[INFO] Saved: d8_05_touching_districts.png")


if __name__ == "__main__":
    gdf = load_shapefile(SHAPEFILE_PATH)

    plot_boundaries(gdf)

    gdf_projected = reproject(gdf)

    buffered = buffer_analysis(gdf_projected)
    plot_buffer(gdf_projected, buffered)

    intersection = overlay_intersection(gdf_projected)
    union_result = overlay_union(gdf_projected)
    plot_union(union_result)

    rajasthan = filter_state(gdf, "Rajasthan")
    plot_state(rajasthan, "Rajasthan")

    touching = find_touching(gdf, rajasthan)
    plot_touching(rajasthan, touching, "Rajasthan")

    print("\n[DONE] Day 8 analysis complete. Check /outputs folder.")
