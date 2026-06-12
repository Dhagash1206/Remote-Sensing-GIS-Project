# GeoSpatial Analysis Project
## Summer Training Programme - Remote Sensing & GIS

---

## Project Structure

```
GeoSpatial_Project/
├── data/
│   ├── 2011_Dist.shp       # India district boundaries shapefile
│   ├── 2011_Dist.dbf       # Attribute data for shapefile
│   ├── 2011_Dist.shx       # Shape index file
│   ├── 2011_Dist.prj       # Projection info
│   └── 2011_Dist.sbx       # Spatial index
│
├── scripts/
│   ├── day_07_data_visualization.py       # Day 7 - Visualization & Analysis
│   └── day_08_advanced_spatial_analysis.py # Day 8 - Advanced GIS Operations
│
├── outputs/                # Auto-generated maps, charts, CSV exports
│
└── README.md
```

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.x | Core language |
| GeoPandas | Vector geospatial data handling |
| Matplotlib | Plotting and map visualization |
| Pandas | Tabular data and time-series analysis |

---

## How to Run

### 1. Install dependencies
```bash
pip install geopandas matplotlib pandas
```

### 2. Run Day 7 script
```bash
python scripts/data_visualization.py
```

### 3. Run Day 8 script
```bash
python scripts/advanced_spatial_analysis.py
```

All outputs (PNG maps, CSV) are saved to the `/outputs` folder automatically.

---

## Day 7 - Data Visualization
- Load and plot India district shapefile
- Choropleth map using mean raster values
- Time-series line chart (2022-2025)
- Bar chart, scatter plot, correlation analysis
- Export statistical summary CSV

## Day 8 - Advanced Spatial Analysis
- CRS inspection (EPSG:4326) and reprojection (EPSG:3857)
- 10km buffer zone analysis around districts
- Intersection and Union overlay operations
- State-level filtering (Rajasthan)
- Spatial query: Find all districts touching Rajasthan

---

## Notes
- `unary_union` is deprecated — replaced with `union_all()` in Day 8 script
- Choropleth map requires `mean_value` column (from zonal statistics shapefile)
- All paths are relative — no hardcoded user paths
