import json
import os

template = {
    "basic": {"name": "", "country": "", "continent": ""},
    "social": {
        "population": None,
        "area": None,
        "populationDensity": None,
        "medianAge": None,
    },
    "economic": {
        "gdpPerCapita": None,
        "unemploymentRate": None,
        "medianAnnualWage": None,
        "minimumHourlyWage": None,
        "costOfLivingIndex": None,  # Numbeo index
        "housePriceToIncomeRatio": None,
        "averageWorkingHours": None,
        "paidVacationDays": None,
    },
    "environmental": {
        "climate": {
            "type": None,
            "averageAnnualTemperature": None,
            "highTemperatureDays": None,
            "annualPrecipitation": None,
            "averageRelativeHumidity": None,
            "annualSunshineHours": None,
        },
        "distanceToCoast": None,
        "averagePM25": None,
        "greenSpaceCoverage": None,
        "parksPerCapita": None,
    },
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
    city = json.loads(json.dumps(template))  # Deep copy of template
    city["basic"]["name"] = f"City{next_city_number}"
    city["basic"]["country"] = f"Country{next_city_number}"
    city["basic"]["continent"] = "Continent"
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

print(f"Added {new_city['basic']['name']} to {file_path}.")
