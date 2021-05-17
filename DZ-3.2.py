def form():
    name = input('Заполните анкету: имя - ')
    surname = input('фамилия - ')
    year = int(input('год рождения - '))
    city = input('город проживаня - ')
    email = input('email - ')
    phone = int(input('мобильный телефон - +7'))
    print(name.title(), surname.title(), year, city.title(), email, phone)

form()
