
import os
import functions as fn


# Меню
def notepad_menu():
    user_choice = input('\n1 - показать все заметки\n2 - создать новую заметку\n3 - удалить заметку\n4 - изменить заметку\n5 - выборка заметок по дате\nДругой символ - закрыть программу\n')
    if user_choice == '1':
        if os.path.exists("note/notepad.csv"):
            fn.main_import_to_notepad()
            notepad_menu()
        else:
            print("Нет ни одной заметки.\nСоздайте первую заметку")
            notepad_menu()
        
    elif user_choice == '2':
        fn.input_note()
        notepad_menu()
    elif user_choice == '3':
        if os.path.exists("note/notepad.csv"):
            fn.delete_note()
            notepad_menu()
        else:
            print("Нет ни одной заметки.\nСоздайте первую заметку")
            notepad_menu()
    elif user_choice == '4':
        if os.path.exists("note/notepad.csv"):
            fn.edit_note()
            notepad_menu()
        else:
            print("Нет ни одной заметки.\nСоздайте первую заметку")
            notepad_menu()
    elif user_choice == '5':
        if os.path.exists("note/notepad.csv"):
            fn.find_date()
            notepad_menu()
        else:
            print("Нет ни одной заметки.\nСоздайте первую заметку")
            notepad_menu()
    else:
        exit


