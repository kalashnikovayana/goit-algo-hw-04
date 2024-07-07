def get_cats_info(path):
    cats_info = []

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                id, name, age = line.strip().split(',')
                cat_info = {
                    "id": id,
                    "name": name,
                    "age": age
                }
                cats_info.append(cat_info)
        return cats_info
    except FileNotFoundError:
        return f"Файл {path} не знайдено."
    except Exception as e:
        return f"Виникла помилка при читанні файлу: {e}"

cats_info = get_cats_info("cats_file.txt")
for cat in cats_info:
    print(cat)
