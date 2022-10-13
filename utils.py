def loading_data(path: str) -> list:
    data_list = []
    file = open(path)
    head = file.readline().split(",")
    line = file.readline()
    while len(line) > 0:
        data = line.split(",")
        data_dictionary = {}
        data_dictionary[head[0]] = data[0]
        data_dictionary[head[1]] = data[1]
        data_dictionary[head[2]] = float(data[2])
        data_dictionary[head[3]] = float(data[3])
        data_dictionary[str.replace(head[4],"\n","")] = bool(str.lower(data[4]))
        data_list.append(data_dictionary)

        line = file.readline()
    file.close()
    return data_list
