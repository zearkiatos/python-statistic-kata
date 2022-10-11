def loading_data(path: str) -> list:
    data_list = []
    file = open(path)
    file.readline().split(",")
    line = file.readline()
    while len(line) > 0:
        data = line.split(",")
        data_dictionary = {}
        data_dictionary["modelo"] = data[0]
        data_dictionary["usuario"] = data[1]
        data_dictionary["pago"] = float(data[2])
        data_dictionary["estrellas"] = float(data[3])
        data_dictionary["estrellas"] = bool(str.lower(data[4]))
        data_list.append(data_dictionary)

        line = file.readline()
    file.close()
    return data_list
