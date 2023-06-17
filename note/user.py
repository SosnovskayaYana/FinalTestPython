import menu as m

# Пользовательский интерфейс
def user_interface():
    header = 'Заметки'.center(50, '-')
    print(header)
    m.notepad_menu()
    


user_interface()