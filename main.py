from colorama import Fore, init
import json


def employees_rewrite(sort_type):
    valid_keys = ['firstName', 'lastName', 'department', 'salary']

    try:
        if sort_type not in valid_keys:
            raise ValueError('Bad key for sorting')
        with open('employees.json', 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)

        employees = data['employees']

        if sort_type == 'salary':
            sorted_employees = sorted(employees, key=lambda x: x[sort_type], reverse=True)
        else:
            sorted_employees = sorted(employees, key=lambda x: x[sort_type])

        sorted_data = {'employees': sorted_employees}

        output_file = f"employees_{sort_type.lower()}_sorted.json"
        with open(output_file, 'w', encoding='utf-8') as file:
            json.dump(sorted_data, file, ensure_ascii=False, indent=4)

        print(Fore.GREEN + f"Данные успешно отсортированы и сохранены в {output_file}")
    except ValueError as err:
        print(Fore.RED + f"{err}: Значение {sort_type} отсутствует в нашем файле!")


if __name__ == '__main__':
    employees_rewrite('lastName')
    employees_rewrite('firstName')
    employees_rewrite('salary')
    employees_rewrite('department')
    employees_rewrite('location')
