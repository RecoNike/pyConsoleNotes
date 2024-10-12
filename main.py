from bgColorsClass import bcolors
import os

def main():
    os.system('cls')
    print_main_menu()

def print_main_menu():
    print(f"{bcolors.OKCYAN}\n\n{'█' * 17}\n█ Console Notes █\n{'█' * 17}\n{bcolors.ENDC}")
    print(f"{bcolors.OKBLUE}Main Menu\n{bcolors.ENDC}")
    print(f"{bcolors.UNDERLINE}1. See notes\n{bcolors.ENDC}")
    print(f"{bcolors.UNDERLINE}2. Exit\n{bcolors.ENDC}")
    answer = input()
    match(answer):
        case "1":
            print_notes()
        case "2":
            exit_app()

def print_notes_menu():

    print(f"{bcolors.OKCYAN}\n\n{'█' * 16}\n█ Manage notes █\n{'█' * 16}\n{bcolors.ENDC}")

    print(f"{bcolors.UNDERLINE}1. Create new note\n{bcolors.ENDC}")
    print(f"{bcolors.UNDERLINE}2. Update note\n{bcolors.ENDC}")
    print(f"{bcolors.UNDERLINE}3. Delete note\n{bcolors.ENDC}")
    print(f"{bcolors.UNDERLINE}4. Back\n{bcolors.ENDC}")
    print(f"{bcolors.UNDERLINE}5. Exit\n{bcolors.ENDC}")

def notes_menu_router():
    answer = input()
    match(answer):
        case "1":
            create_new_note()
        case "2":
            number_of_updating_note()
        case "3":
            delete_note()
        case "4":
            main()
        case "5":
            exit_app()



def update_note(nr_of_updating_note):
    try:
        # Читаем содержимое файла
        with open('notes.txt', 'r') as file:
            lines = file.readlines()

        # Проверяем, что указанная строка существует
        if 0 < int(nr_of_updating_note) <= len(lines):
            # Получаем текущую строку, которую пользователь хочет изменить
            current_line = lines[int(nr_of_updating_note) - 1].strip()
            
            # Предоставляем пользователю возможность редактировать текущую строку
            new_content = input(f"Edit note {nr_of_updating_note} (current: '{current_line}'): ") or current_line

            # Обновляем нужную строку
            lines[int(nr_of_updating_note) - 1] = new_content + "\n"
            
            # Перезаписываем файл с обновлёнными данными
            with open('notes.txt', 'w') as file:
                file.writelines(lines)
            
            print(f"Note {nr_of_updating_note} updated successfully.")
            print_notes()
            return
        else:
            print("Error: Note number does not exist.")
    
    except IOError as e:
        print(f"Error opening or updating the file: {e}")

def delete_note():
    try:
        # Читаем содержимое файла
        with open('notes.txt', 'r') as file:
            lines = file.readlines()

        # Получаем номер записи, которую нужно удалить
        note_number = get_int_input("Enter the number of the note to delete: ")

        # Проверяем, что введённый номер находится в пределах списка строк
        if 0 < note_number <= len(lines):
            # Подтверждаем удаление
            confirmation = input(f"Are you sure you want to delete note {note_number}? (y/n): ").lower()
            if confirmation == 'y':
                # Удаляем строку
                deleted_note = lines.pop(note_number - 1)
                
                # Перезаписываем файл с обновлённым содержимым
                with open('notes.txt', 'w') as file:
                    file.writelines(lines)
                
                print(f"Note {note_number} deleted successfully: {deleted_note.strip()}")
            else:
                print("Deletion cancelled.")
        else:
            print("Error: Note number does not exist.")
    
    except IOError as e:
        print(f"Error opening or updating the file: {e}")
    print_notes()

def number_of_updating_note():
    print("Write down number of the note, which you want to update:")
    note_number = get_int_input("Enter the number of the note to update: ")
    update_note(note_number)

def get_int_input(prompt):
    while True:
        try:
            # Пробуем получить целое число
            user_input = int(input(prompt))
            return user_input  # Если ввод успешен, возвращаем число
        except ValueError:
            # Если произошло исключение, выводим сообщение об ошибке
            print("Invalid input. Please enter a valid integer.")
            print_notes()

def print_notes():
    os.system('cls')
    print_notes_menu()
    print(f"{bcolors.WARNING}Notes\n{bcolors.ENDC}")
    try:
        with open('notes.txt', 'a+') as file:
            file.seek(0)  # Перемещаем указатель в начало файла, чтобы можно было его читать
            for i, line in enumerate(file, 1):  # Нумеруем строки, начиная с 1
                print(f"{i}: {line.strip()}")
    except IOError as e:
            print(f"Error opening or creating the file: {e}")
    notes_menu_router()


def create_new_note():
    os.system('cls')
    print("Type text of note, use 'Enter' to save")
    try:
        with open('notes.txt', 'a+') as file:
            user_input = input()
            file.write(user_input+'\n')
    except IOError as e:
            print(f"Error opening or creating the file: {e}")
    print_notes_menu()
    print_notes()



def exit_app():
    exit

main()