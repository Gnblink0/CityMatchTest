import pandas as pd;

def get_statistic_by(cities, id, df):
    return df[(df["characteristic_id"].isin(id)) & (df["geo_name"].isin(cities))]

PATH = "./cities_CA.csv"

df = pd.read_csv(PATH, encoding="utf-8")

print(df["geo_name"].unique())

#remove some labals
df = df.drop(["census_year", "dguid", "alt_geo_code", "geo_level","tnr_sf", "tnr_lf", 
              "data_quality_flag", "characteristic_note", "c1_count_total_symbol", 
              "c2_count_men_symbol", "c3_count_women_symbol", "c10_rate_total_symbol",
              "c11_rate_men_symbol", "c12_rate_women_symbol"], axis=1)

cities = ["Toronto", "Vancouver", "Calgary", "Ottawa - Gatineau", "Montréal"] 
ids = [1,2]

#get population csv file
df = get_statistic_by(cities, ids, df)

#save
df.to_csv("./population.csv", index=False)