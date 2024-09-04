import json
import subprocess
import os


def run_script(script_name):
    result = subprocess.run(["python", script_name], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error running {script_name}:")
        print(result.stderr)
    else:
        print(result.stdout)


# 读取cities_name.json
with open("data/cities_name.json", "r", encoding="utf-8") as file:
    cities_data = json.load(file)

# 确保目标文件夹存在
os.makedirs("data", exist_ok=True)

# 对每个城市运行脚本
for city in cities_data["cities"]:
    print(f"Processing city: {city['name']}")

    # 运行add_a_city_statis_data_template.py
    run_script("data/add_a_city_statis_data_template.py")

    # 运行add_a_city_template.py
    run_script("data/add_a_city_template.py")

print("All cities have been processed.")

# 读取并更新cities_statis_data.json
with open("data/cities_statis_data.json", "r", encoding="utf-8") as file:
    statis_data = json.load(file)

for i, city in enumerate(cities_data["cities"]):
    if i < len(statis_data["cities"]):
        statis_data["cities"][i]["basic"]["name"] = city["name"]
        statis_data["cities"][i]["basic"]["country"] = city["country"]

# 写回更新后的cities_statis_data.json
with open("data/cities_statis_data.json", "w", encoding="utf-8") as file:
    json.dump(statis_data, file, indent=4, ensure_ascii=False)

# 读取并更新cities.json
with open("data/cities.json", "r", encoding="utf-8") as file:
    cities_json = json.load(file)

for i, city in enumerate(cities_data["cities"]):
    if i < len(cities_json):
        cities_json[i]["name"]["en"] = city["name"]
        cities_json[i]["country"]["en"] = city["country"]

# 写回更新后的cities.json
with open("data/cities.json", "w", encoding="utf-8") as file:
    json.dump(cities_json, file, indent=4, ensure_ascii=False)

print("City names and countries have been updated in both files.")
