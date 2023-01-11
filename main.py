import pandas as pd
import geopandas as gpd
from shapely.geometry import shape

def footprints_download(location):
  """
  location = nome do país em inglês (string)
  """
  dataset_links = pd.read_csv("https://minedbuildings.blob.core.windows.net/global-buildings/dataset-links.csv")
  loc_links = dataset_links[dataset_links.Location == location]
  for _, row in loc_links.iterrows():
      df = pd.read_json(row.Url, lines=True)
      df['geometry'] = df['geometry'].apply(shape)
      gdf = gpd.GeoDataFrame(df, crs=4326)
      gdf.to_file(f"{row.QuadKey}.shp")
      
# Executar função footprints_download
footprints_download('Brazil')
