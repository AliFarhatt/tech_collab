def write_selected_dict_values_to_file(dict_list, filename, keys = ['description', 'category']):
    with open(filename, 'w',  encoding='utf-8') as file:
        try:
            for dictionary in dict_list:
                selected_values = []
                for key in keys:
                    if key in dictionary:
                        value = dictionary[key]
                        if isinstance(value, list):
                            selected_values.extend(map(str, value))
                        else:
                            selected_values.append(str(value)+" ")
                values_line = ', '.join(selected_values)
                file.write(values_line + '\n')
        except Exception as e:
            print(e)
