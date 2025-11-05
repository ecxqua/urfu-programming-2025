"""Цель - создать менеджера команды Pokémon,
который позволит пользователям:
• Добавлять покемонов в свою команду. (если такого
покемона еще нет в команде)
• Удалять покемонов из их команды.
• Просматривать подробную информацию обо всех
покемонах в команде.
• Находить покемона по имени.
• Устраивать тренировочный бой между двумя
покемонами
• Для данной задачи используйте: https://pokeapi.co/"""

import requests
import random
import json


class Pokemon:
    """Класс для представления покемона.
    Этот класс предоставляет функциональность для получения и хранения информации о покемоне
    из PokeAPI.
    Атрибуты:
        name (str): Имя покемона.
        data (dict): Словарь, содержащий данные покемона, полученные из PokeAPI.
    Методы:
        fetch_data(): Получает данные покемона из PokeAPI.
        get_info(): Возвращает основную информацию о покемоне.  
        get_attack_power(): Вычисляет и возвращает силу атаки покемона.
    """

    def __init__(self, name):
        self.name = name
        self.data = self.fetch_data()

    def fetch_data(self):
        response = requests.get(
            f'https://pokeapi.co/api/v2/pokemon/{self.name.lower()}')
        if response.status_code == 200:
            return response.json()
        else:
            raise ValueError(f"Pokémon {self.name} not found.")

    def get_info(self):
        info = {
            'Имя': self.data['name'],
            'Рост': self.data['height'],
            'Вес': self.data['weight'],
            'Типы': [t['type']['name'] for t in self.data['types']],
            'Способности': [a['ability']['name'] for a in self.data['abilities']],
            'Базовые характеристики': {stat['stat']['name']: stat['base_stat'] for stat in self.data['stats']}
        }
        return info

    def get_attack_power(self):
        return sum(stat['base_stat'] for stat in self.data['stats']) // len(self.data['stats'])


class PokemonManager:

    """Класс для управления командой покемонов.
    Этот класс предоставляет функциональность для управления командой покемонов, включая
    добавление и удаление покемонов, просмотр информации о команде, поиск конкретных
    покемонов и проведение боев между членами команды.
    Атрибуты:
        team (dict): Словарь, хранящий объекты Pokemon с их именами в качестве ключей.
    Методы:
        add_pokemon(name): Добавляет покемона в команду.
        remove_pokemon(name): Удаляет покемона из команды.
        view_team(): Отображает информацию обо всех покемонах в команде.
        find_pokemon(name): Отображает информацию о конкретном покемоне.
        battle(name1, name2): Проводит бой между двумя покемонами в команде.
    """

    def __init__(self):
        self.team = {}

    def add_pokemon(self, name):
        if name in self.team:
            print(f"{name} уже в вашей команде.")
        else:
            try:
                pokemon = Pokemon(name)
                self.team[name] = pokemon
                print(f"{name} добавлен в вашу команду.")
            except ValueError as e:
                print(e)

    def remove_pokemon(self, name):
        if name in self.team:
            del self.team[name]
            print(f"{name} удален из вашей команды.")
        else:
            print(f"{name} не найден в вашей команде.")

    def view_team(self):
        if not self.team:
            print("Ваша команда пуста.")
        else:
            for name, pokemon in self.team.items():
                info = pokemon.get_info()
                print(json.dumps(info, indent=4, ensure_ascii=False))

    def find_pokemon(self, name):
        if name in self.team:
            info = self.team[name].get_info()
            print(json.dumps(info, indent=4, ensure_ascii=False))
        else:
            print(f"{name} не найден в вашей команде.")

    def battle(self, name1, name2):
        if name1 not in self.team or name2 not in self.team:
            print("Оба покемона должны быть в вашей команде для боя.")
            return

        power1 = self.team[name1].get_attack_power()
        power2 = self.team[name2].get_attack_power()

        print(f"Бой между {name1} (сила: {power1}) и {name2} (сила: {power2})")

        if power1 > power2:
            print(f"{name1} побеждает!")
        elif power2 > power1:
            print(f"{name2} побеждает!")
        else:
            print("Ничья!")


if __name__ == "__main__":
    manager = PokemonManager()
    # Пример использования менеджера
    manager.add_pokemon("Pikachu")
    manager.add_pokemon("Charmander")
    manager.view_team()
    manager.battle("Pikachu", "Charmander")
    manager.find_pokemon("Pikachu")
    manager.remove_pokemon("Pikachu")
    manager.view_team()
