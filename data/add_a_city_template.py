import json
import os

# 定义一个城市数据模板，所有字符串字段改为多语言字典
template = {
    "name": {"en": "", "zh": ""},  # 英文名  # 中文名
    "country": {"en": "", "zh": ""},
    "continent": {"en": "", "zh": ""},
    "population": None,  # 未知人口设为 None
    "area": None,  # 未知面积设为 None
    "characteristics": {"cityFeatures": {"en": [], "zh": []}},
    "socialFactors": {
        "safetyIndex": None,
        "sustainabilityIndex": None,
        "governanceEfficiencyIndex": None,
        "populationSizeIndex": None,
        "populationDensityIndex": None,
        "populationAgeIndex": None,
    },
    "economicFactors": {
        "economicDevelopmentLevel": None,
        "employmentOpportunityIndex": None,
        "minimumWageIndex": None,
        "costOfLivingIndex": None,
        "housingAffordabilityIndex": None,
        "tippingCultureIndex": None,
        "workLifeBalanceIndex": None,
        "techInnovationIndex": None,
    },
    "environmentalFactors": {
        "climate": {
            "climateLabels": {"en": [], "zh": []},
            "climateType": {"en": "", "zh": ""},
            "livabilityIndex": None,
            "temperatureIndex": None,
            "highTemperatureDaysIndex": None,
            "precipitationIndex": None,
            "humidityIndex": None,
            "sunshineIndex": None,
        },
        "environment": {
            "coastalIndex": None,
            "waterBodyIndex": None,
            "airQualityIndex": None,
            "naturalDisasterRiskIndex": None,
        },
        "greenSpaceIndex": None,
    },
    "culturalFactors": {
        "language": {
            "mainLanguages": {"en": [], "zh": []},
            "englishProficiencyIndex": None,
        },
        "socialAttitudeIndex": None,
        "socialInclusivityIndex": None,
        "internationalizationIndex": None,
        "culturalDiversityIndex": None,
        "historicalCulturalRichnessIndex": None,
        "lifePaceIndex": None,
        "mentalHealthSupportIndex": None,
        "socialMobilityIndex": None,
    },
    "infrastructureFactors": {
        "transportation": {
            "walkabilityIndex": None,
            "bikeFriendlinessIndex": None,
            "publicTransportConvenienceIndex": None,
            "averageCommuteTimeIndex": None,
        },
        "urbanDesignAestheticsIndex": None,
        "healthcareFacilityQualityIndex": None,
        "educationResourceAbundanceIndex": None,
        "digitalizationIndex": None,
        "seniorFriendlinessIndex": None,
        "childFriendlinessIndex": None,
        "petFriendlinessIndex": None,
    },
    "leisureAndEntertainmentFactors": {
        "culturalActivityIndex": None,
        "entertainmentFacilityIndex": None,
        "sportsFacilityIndex": None,
        "naturalLandscapeIndex": None,
        "culinaryIndex": None,
        "nightlifeIndex": None,
    },
}


# 生成下一个城市的名字，按顺序增加
def generate_next_city(existing_cities):
    next_city_number = len(existing_cities) + 1
    city = template.copy()  # 复制模板
    # 设置城市名称的多语言版本
    city["name"]["en"] = f"City{next_city_number}"
    city["name"]["zh"] = f"城市{next_city_number}"

    # 设置国家和大陆的多语言版本
    city["country"]["en"] = f"Country{next_city_number}"
    city["country"]["zh"] = f"国家{next_city_number}"

    city["continent"]["en"] = "Continent"
    city["continent"]["zh"] = "大洲"

    # 人口和面积保持 None, 作为未知值
    return city


# 文件路径
file_path = "/Users/gnblink/2 项目 · Project/2024_Code/CityMatchTest/data/cities.json"

# 检查文件是否存在并读取现有城市
if os.path.exists(file_path):
    with open(file_path, "r") as file:
        try:
            cities = json.load(file)
        except json.JSONDecodeError:
            cities = []  # 文件为空时初始化为空列表
else:
    cities = []

# 生成下一个城市并添加到列表
new_city = generate_next_city(cities)
cities.append(new_city)

# 写回到 cities.json 文件
with open(file_path, "w") as file:
    json.dump(cities, file, indent=4, ensure_ascii=False)

print(
    f"已添加 {new_city['name']['en']} ({new_city['name']['zh']}) 到 {file_path} 文件中。"
)
