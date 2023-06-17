import datetime
import random

# Добавление заметки
def input_note():
    note_elem = ["заголовок", "текст"]
    new_note = list()
    notepad = dict()
    date = datetime.datetime.now().strftime("%Y-%m-%d / %H:%M:%S")
    for i in range(len(note_elem)):
        new_note.insert(i, input(f"Введите {note_elem[i]}: "))
    new_note.insert(2, date)
    notepad[random.randint(1000, 10000)] = new_note 
    export_to_notepad(notepad)
    print("Заметка добавлена...")


def export_to_notepad(notepad):
    with open('note/notepad.csv', 'a+', encoding='utf-8') as data:
        for item in notepad:
            data.writelines('{};{}'.format(item, ';'.join(notepad[item])) +'\n')


def import_to_notepad():
    notepad = dict()        
    with open('note/notepad.csv', 'r', encoding='utf-8') as data:
        notes = data.readlines()
        if len(notes) == 0:
            print("Нет ни одной записи.\nСоздайте заметку.")
        for i in range(len(notes)):
            notepad[i] = notes[i]
    return notepad


def main_import_to_notepad():
    notepad = dict()        
    with open('note/notepad.csv', 'r', encoding='utf-8') as data:
        notes = data.readlines()
        if len(notes) == 0:
            print("Нет ни одной записи.\nСоздайте заметку.")
        for i in range(len(notes)):
            notepad[i] = notes[i]
        for item in notepad:
            print('ID: {} | Заголовок: {}\nТекст: {}\nДата: {}'.format(notepad[item].split(sep=";")[0], notepad[item].split(sep=";")[1], notepad[item].split(sep=";")[2], notepad[item].split(sep=";")[3]))



# Перезапись 
def replace_notepad(messege, new_notepad):
    with open('note/notepad.csv', 'w', encoding='utf-8') as data: 
        print(messege)   
        data.writelines(new_notepad)



# Поиск по дате
def find_date():
    main_import_to_notepad()
    with open('note/notepad.csv', 'r+', encoding='utf-8') as data:
        notes = data.readlines()
        year = input('\nВведите год: ')
        month = input('\nВведите месяц: ')
        day = input('\nВведите день: ')
        date_note = '{}-{}-{}'.format(year, month, day)
        for index in range(len(notes)):
            if date_note == notes[index].split(sep=";")[3][:10]: 
                print('ID: {} | Заголовок: {}\nТекст: {}\nДата: {}'.format(notes[index].split(sep=";")[0], notes[index].split(sep=";")[1], notes[index].split(sep=";")[2], notes[index].split(sep=";")[3]))
            elif index==len(notes)-1 & date_note == notes[index].split(sep=";")[3][:10]:
                print("Такой заметки не существует.")
   



# Изменение заметки
def edit_note():
    note_elem = ["заголовок", "текст"]
    main_import_to_notepad()
    date = datetime.datetime.now().strftime("%Y-%m-%d / %H:%M:%S")
    with open('note/notepad.csv', 'r+', encoding='utf-8') as data:
        notes = data.readlines()
        id_note = int(input('\nВведите ID нужной заметки: '))
        for index in range(len(notes)):
            if id_note == int(notes[index].split(sep=";")[0]): 
                note = notes[index].split(sep=";")
                print('\nЧто Вы хотите изменить?')
                user_choice = int(input('\n1 - Заголовок\n2 - Текст\n'))
                for i in range(len(note_elem)):
                    if i == (user_choice-1):  
                        note[user_choice] = input(f'Введите новый {note_elem[i]}: ')
                note[3] = date
                notes[index] = (';'.join(note)+'\n')
                replace_notepad('Сохранено...', notes)
                break
            elif index==len(notes)-1 & id_note != int(notes[index].split(sep=";")[0]):
                print("Такой заметки не существует.")
                


# Удаление заметки
def delete_note():
    main_import_to_notepad()
    with open('note/notepad.csv', 'r+', encoding='utf-8') as data:
        notes = data.readlines()
        if len(notes)>0:
            id_note = int(input('\nВведите ID нужной заметки: '))
            for index in range(len(notes)):
                if id_note == int(notes[index].split(sep=";")[0]): 
                    del notes[index]
                    replace_notepad('Удалено...', notes)
                    break
                elif index==len(notes)-1 & id_note != int(notes[index].split(sep=";")[0]):
                    print("Такой заметки не существует.")    


