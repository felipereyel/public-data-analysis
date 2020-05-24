def calculate_ratio(data, key, result_key, value1, value2):
    result1 = float(data[data[key] == value1][result_key])
    result2 = float(data[data[key] == value2][result_key])
    return result1/result2
