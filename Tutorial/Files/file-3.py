with open('student_data.txt', 'r', encoding='utf-8') as f:
    data = f.read()
    data_list = data.split(',')
    #print(data_list)
    my_info = {
        'name': data_list[0],
        'age': data_list[1],
        'location': data_list[2],
        'mobile': data_list[3]
    }

    print(my_info)


with open('student_data.txt', 'a', encoding='utf-8') as f:
    f.write("\n End of the file.")