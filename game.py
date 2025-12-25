import file_operations
import random
from faker import Faker

fake = Faker("ru_RU")

dictionary = {
    'а': 'а͠', 'б': 'б̋', 'в': 'в͒͠',
    'г': 'г͒͠', 'д': 'д̋', 'е': 'е͠',
    'ё': 'ё͒͠', 'ж': 'ж͒', 'з': 'з̋̋͠',
    'и': 'и', 'й': 'й͒͠', 'к': 'к̋̋',
    'л': 'л̋͠', 'м': 'м͒͠', 'н': 'н͒',
    'о': 'о̋', 'п': 'п̋͠', 'р': 'р̋͠',
    'с': 'с͒', 'т': 'т͒', 'у': 'у͒͠',
    'ф': 'ф̋̋͠', 'х': 'х͒͠', 'ц': 'ц̋',
    'ч': 'ч̋͠', 'ш': 'ш͒͠', 'щ': 'щ̋',
    'ъ': 'ъ̋͠', 'ы': 'ы̋͠', 'ь': 'ь̋',
    'э': 'э͒͠͠', 'ю': 'ю̋͠', 'я': 'я̋',
    'А': 'А͠', 'Б': 'Б̋', 'В': 'В͒͠',
    'Г': 'Г͒͠', 'Д': 'Д̋', 'Е': 'Е',
    'Ё': 'Ё͒͠', 'Ж': 'Ж͒', 'З': 'З̋̋͠',
    'И': 'И', 'Й': 'Й͒͠', 'К': 'К̋̋',
    'Л': 'Л̋͠', 'М': 'М͒͠', 'Н': 'Н͒',
    'О': 'О̋', 'П': 'П̋͠', 'Р': 'Р̋͠',
    'С': 'С͒', 'Т': 'Т͒', 'У': 'У͒͠',
    'Ф': 'Ф̋̋͠', 'Х': 'Х͒͠', 'Ц': 'Ц̋',
    'Ч': 'Ч̋͠', 'Ш': 'Ш͒͠', 'Щ': 'Щ̋',
    'Ъ': 'Ъ̋͠', 'Ы': 'Ы̋͠', 'Ь': 'Ь̋',
    'Э': 'Э͒͠͠', 'Ю': 'Ю̋͠', 'Я': 'Я̋',
    ' ': ' '
}

skills = ["Стремительный прыжок", "Электрический выстрел", "Ледяной удар", "Стремительный удар", "Кислотный взгляд", "Тайный побег", "Ледяной выстрел", "Огненный заряд"]
names = ["charsheet1.svg", "charsheet2.svg", "charsheet3.svg", "charsheet4.svg", "charsheet5.svg", "charsheet6.svg", "charsheet7.svg", "charsheet8.svg", "charsheet9.svg", "charsheet10.svg"]

for i in range(10):
	random_skills = random.sample(skills,3)

	player_characteristics = {
  "first_name": fake.first_name_male(),
  "last_name": fake.last_name_male(),
  "job": fake.job(),
  "town": fake.city(),
  "strength": random.randint(3, 18),
  "agility": random.randint(3, 18),
  "endurance": random.randint(3, 18),
  "intelligence": random.randint(3, 18),
  "luck": random.randint(3, 18),
  "skill_1": random_skills[0],
  "skill_2": random_skills[1],
  "skill_3": random_skills[2]
}

	file_operations.render_template("template.svg", names[i], player_characteristics)
	print(f"Файл {names[i]} создан!")






