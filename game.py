import file_operations
import random
from faker import Faker
import os

PLAYER_CARDS = "player cards"
os.makedirs(PLAYER_CARDS, exist_ok=True)

SKILLS = ["Стремительный прыжок", "Электрический выстрел", "Ледяной удар", "Стремительный удар", "Кислотный взгляд", "Тайный побег", "Ледяной выстрел", "Огненный заряд"]
NAMES = ["charsheet1.svg", "charsheet2.svg", "charsheet3.svg", "charsheet4.svg", "charsheet5.svg", "charsheet6.svg", "charsheet7.svg", "charsheet8.svg", "charsheet9.svg", "charsheet10.svg"]


DICTIONARY = {
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
    'Л': 'Л̋͠', 'м': 'м͒͠', 'Н': 'Н͒',
    'О': 'О̋', 'П': 'П̋͠', 'Р': 'Р̋͠',
    'С': 'С͒', 'Т': 'Т͒', 'У': 'У͒͠',
    'Ф': 'Ф̋̋͠', 'Х': 'Х͒͠', 'Ц': 'Ц̋',
    'Ч': 'Ч̋͠', 'Ш': 'Ш͒͠', 'Щ': 'Щ̋',
    'Ъ': 'Ъ̋͠', 'Ы': 'Ы̋͠', 'Ь': 'Ь̋',
    'Э': 'Э͒͠͠', 'Ю': 'Ю̋͠', 'Я': 'Я̋',
    ' ': ' '
}


def convert_text_to_runes(text: str) -> str:
    converted_text = text
    for key, value in DICTIONARY.items():
        converted_text = converted_text.replace(key, value)
    return converted_text


def generate_random_skills() -> list:
    random_skills = random.sample(SKILLS, 3)
    runic_skills = []
    
    for skill in random_skills:
        runic_skill = convert_text_to_runes(skill)
        runic_skills.append(runic_skill)
    
    return runic_skills


def generate_player_characteristics(fake_instance: Faker) -> dict:
    runic_skills = generate_random_skills()
    
    return {
        "first_name": fake_instance.first_name_male(),
        "last_name": fake_instance.last_name_male(),
        "job": fake_instance.job(),
        "town": fake_instance.city(),
        "strength": random.randint(3, 18),
        "agility": random.randint(3, 18),
        "endurance": random.randint(3, 18),
        "intelligence": random.randint(3, 18),
        "luck": random.randint(3, 18),
        "skill_1": runic_skills[0],
        "skill_2": runic_skills[1],
        "skill_3": runic_skills[2]
    }


def main() -> None:
    os.makedirs(PLAYER_CARDS, exist_ok=True)
    fake = Faker("ru_RU")
    
    for i in range(10):
        player_characteristics = generate_player_characteristics(fake)
        file_path = os.path.join(PLAYER_CARDS, NAMES[i])
        file_operations.render_template("charsheet.svg", file_path, player_characteristics)


if __name__ == '__main__':
    main()