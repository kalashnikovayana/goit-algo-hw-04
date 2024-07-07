def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            total = 0
            count = 0
            for line in file:
                parts = line.strip().split(',')
                salary = int(parts[-1])
                total += salary
                count += 1
            average = total / count if count > 0 else 0
            return total, average
    except FileNotFoundError:
        print(f"Файл {path} не знайдено.")
        return None, None
    except Exception as e:
        print(f"Виникла помилка при читанні файлу: {e}")
        return None, None

total, average = total_salary("salary_file.txt")
if total is not None and average is not None:
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
else:
    print("Не вдалося обчислити заробітну плату.")

