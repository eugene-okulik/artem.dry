class Flower:
    def __init__(self, name, fresh, length, cost, color, life_time):
        self.name = name
        self.fresh = fresh
        self.length = length
        self.cost = cost
        self.color = color
        self.life_time = life_time


class Rose(Flower):
    def __init__(self, fresh, length, cost, color):
        super().__init__('Роза', fresh, length, cost, color, life_time=7)


class Tulip(Flower):
    def __init__(self, fresh, length, cost, color):
        super().__init__('Тюльпан', fresh, length, cost, color, life_time=5)


class Lily(Flower):
    def __init__(self, fresh, length, cost, color):
        super().__init__('Лилия', fresh, length, cost, color, life_time=10)


class Bouquet:
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def get_cost(self):
        total = 0
        for flower in self.flowers:
            total += flower.cost
        return total

    def get_average_wilting_time(self):
        if len(self.flowers) == 0:
            return 0
        total = 0
        for flower in self.flowers:
            remaining = flower.life_time - flower.fresh
            if remaining < 0:
                remaining = 0
            total += remaining
        return total / len(self.flowers)

    def sort_by_fresh(self):
        self.flowers.sort(key=lambda flower: flower.fresh)

    def sort_by_color(self):
        self.flowers.sort(key=lambda flower: flower.color)

    def sort_by_stem_length(self):
        self.flowers.sort(key=lambda flower: flower.length)

    def sort_by_cost(self):
        self.flowers.sort(key=lambda flower: flower.cost)

    def find_by_life_time(self, min_days, max_days):
        result = []
        for flower in self.flowers:
            if min_days <= flower.life_time <= max_days:
                result.append(flower)
        return result

    def show(self):
        if not self.flowers:
            print("Букет пуст.")
            return
        for i, flower in enumerate(self.flowers, 1):
            print(f"{i}. {flower.name}, цвет: {flower.color}, "
                  f"свежесть: {flower.fresh}, "
                  f"стебель: {flower.length} см, "
                  f"цена: {flower.cost} руб., "
                  f"живёт: {flower.life_time} дней")


if __name__ == "__main__":
    bouquet = Bouquet()
    bouquet.add_flower(Rose(fresh=1, length=50, cost=200, color="Красный"))
    bouquet.add_flower(Rose(fresh=0, length=55, cost=220, color="Белый"))
    bouquet.add_flower(Tulip(fresh=2, length=30, cost=100, color="Жёлтый"))
    bouquet.add_flower(Lily(fresh=1, length=60, cost=300, color="Розовый"))
    print("Содержимое букета:")
    bouquet.show()
    print(f"\nОбщая стоимость: {bouquet.get_cost()} руб.")
    print(f"Среднее время до увядания: {bouquet.get_average_wilting_time():.1f} дня(ей)")
    print("\nПосле сортировки по цвету:")
    bouquet.sort_by_color()
    bouquet.show()
    print("\nЦветы с временем жизни от 6 до 10 дней:")
    long_living = bouquet.find_by_life_time(6, 10)
    for flower in long_living:
        print(f"  - {flower.name} ({flower.color})")
