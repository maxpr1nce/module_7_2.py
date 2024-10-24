def custom_write(file_name, strings):
    strings_positions = {}

    with open(file_name, 'w', encoding='utf-8') as file:
        for i, string in enumerate(strings, start=1):
            byte_position = file.tell()  # Получаем текущую позицию байта
            file.write(string + '\n')  # Записываем строку в файл
            strings_positions[(i, byte_position)] = string  # Добавляем в словарь

    return strings_positions

file_name = 'output.txt'
strings = ['Text for tell.', 'Используйте кодировку utf-8.']
result = custom_write(file_name, strings)
print(result)