import json
import os
import random

# 定义一个简化的城市数据模板，只使用英文
template = {
    "name": "",
    "country": "",
    "continent": "",
    "population": None,
    "area": None,
    "climate": {"type": None},  # 这里将使用枚举值
    "indices": {
        "safetyIndex": None,
        "costOfLivingIndex": None,
        "sunshineIndex": None,
        "coastalIndex": None,
        "waterBodyIndex": None,
        "airQualityIndex": None,
        "englishProficiencyIndex": None,
        "publicTransportConvenienceIndex": None,
        "culturalActivityIndex": None,
        "entertainmentFacilityIndex": None,
        "sportsFacilityIndex": None,
        "culinaryIndex": None,
    },
    "language": {"mainLanguages": []},
}

# 气候类型枚举
climate_types = [
    "TROPICAL_RAINFOREST",
    "TROPICAL_MONSOON",
    "TROPICAL_SAVANNA",
    "OCEANIC",
    "TEMPERATE_CONTINENTAL",
    "MEDITERRANEAN",
    "TEMPERATE_MONSOON",
    "SUBTROPICAL_MONSOON",
    "ARID_SEMI_ARID",
    "HIGHLAND_MOUNTAIN",
    "HUMID_SUBTROPICAL",
]


def generate_next_city(existing_cities):
    next_city_number = len(existing_cities) + 1
    city = template.copy()
    city["name"] = f"City{next_city_number}"
    city["country"] = f"Country{next_city_number}"
    city["continent"] = "Continent"
    return city


# 文件路径
file_path = "data/cities_statis_data.json"

# 检查文件是否存在并读取现有城市
if os.path.exists(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        try:
            data = json.load(file)
            cities = data.get("cities", [])
        except json.JSONDecodeError:
            cities = []
else:
    cities = []

# 生成下一个城市并添加到列表
new_city = generate_next_city(cities)
cities.append(new_city)

# 准备完整的数据结构
data = {
    "cities": cities,
    "climateTypes": {
        climate_type: climate_type.replace("_", " ").title()
        for climate_type in climate_types
    },
}

# 写回到文件
os.makedirs(os.path.dirname(file_path), exist_ok=True)
with open(file_path, "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)

print(f"Added {new_city['name']} to {file_path}.")
