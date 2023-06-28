import json

"""function to calculate the sum of the scores of each element and the number of attributes it has.
returns total score"""
def calc_score(json_data:dict)-> int:
    score = 0
    if isinstance(json_data, dict):
        score = len(json_data.keys())
        for key in json_data:
            score += calc_score(json_data[key])
        return score
    elif isinstance(json_data, list):
        for item in json_data:
            score += calc_score(item)
        return score
    else:
        return 0

if __name__ == "__main__":
    with open("data.json") as data:
        data_dict = json.load(data)
        score = calc_score(data_dict)
        print(f"Score: {score}")
