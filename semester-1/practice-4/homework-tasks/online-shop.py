"""
Модуль онлайн-магазина.

Этот модуль содержит основные классы для работы интернет-магазина:
Product, Order, Customer и ShoppingCart.
"""


class Product:
    """
    Класс товара в магазине.

    Представляет товар с базовой информацией: название, цена, количество и категория.

    Attributes:
        name (str): Название товара
        price (int): Цена товара в рублях
        availability (int): Количество товара на складе
        category (str): Категория товара
    """

    def __init__(self, name: str, price: int, availability: int, category: str):
        """
        Инициализирует объект товара.

        Args:
            name: Название товара
            price: Цена товара в рублях
            availability: Количество на складе
            category: Категория товара
        """
        self.name = name
        self.price = price
        self.availability = availability
        self.category = category

    def check_availability(self, quantity=1):
        """
        Проверяет, доступно ли нужное количество товара на складе.

        Args:
            quantity: Требуемое количество товара (по умолчанию 1)

        Returns:
            bool: True если товара достаточно, False в противном случае

        Example:
            >>> product = Product("Стул", 1000, 5, "мебель")
            >>> product.check_availability(3)
            True
            >>> product.check_availability(10)
            False
        """
        return self.availability >= quantity

    def reduce_availability(self, quantity):
        """
        Уменьшает количество товара на складе.

        Args:
            quantity: Количество для списания

        Returns:
            bool: True если списание успешно, False если товара недостаточно

        Raises:
            ValueError: Если quantity отрицательное число
        """
        if quantity < 0:
            raise ValueError("Количество не может быть отрицательным")

        if self.check_availability(quantity):
            self.availability -= quantity
            return True
        return False

    def product_info(self):
        """
        Возвращает форматированную информацию о товаре.

        Returns:
            str: Строка с подробной информацией о товаре

        Example:
            >>> product = Product("Стул", 1000, 5, "мебель")
            >>> print(product.product_info())
            Название товара: Стул 
            Цена за ед.: 1000
            Количество на складе: 5
            Категория: мебель
        """
        return f"Название товара: {self.name} \nЦена за ед.: {self.price}\nКоличество на складе: {self.availability}\nКатегория: {self.category}"


class Order:
    """
    Класс заказа в магазине.

    Представляет заказ клиента, обрабатывает расчет стоимости и выполнение заказа.

    Attributes:
        order_id (str): Уникальный идентификатор заказа
        customer (Customer): Клиент, сделавший заказ
        items (list): Список товаров в формате (product, quantity)
        status (str): Статус заказа
        tax_rate (float): Ставка налога (по умолчанию 18%)
        discount (float): Процент скидки
    """

    def __init__(self, order_id, customer, cart):
        """
        Инициализирует объект заказа.

        Args:
            order_id: Уникальный идентификатор заказа
            customer: Объект клиента
            cart: Корзина покупок клиента
        """
        self.order_id = order_id
        self.customer = customer
        self.items = cart.items.copy()  # Копируем товары из корзины
        self.status = "created"
        self.tax_rate = 0.18  # 18% налог
        self.discount = 0

    def calculate_subtotal(self):
        """
        Рассчитывает сумму заказа без учета налогов и скидок.

        Returns:
            float: Сумма всех товаров в заказе

        Example:
            >>> order.calculate_subtotal()
            1500.0
        """
        return sum(product.price * quantity for product, quantity in self.items)

    def apply_discount(self, discount_percent):
        """
        Применяет скидку к заказу.

        Args:
            discount_percent: Процент скидки (0-100)

        Raises:
            ValueError: Если скидка не в диапазоне 0-100
        """
        if not 0 <= discount_percent <= 100:
            raise ValueError("Скидка должна быть в диапазоне от 0 до 100%")
        self.discount = discount_percent

    def calculate_total(self):
        """
        Рассчитывает итоговую сумму с учетом налогов и скидок.

        Returns:
            dict: Словарь с детализацией расчета:
                - subtotal: Сумма без скидок
                - discount_amount: Сумма скидки
                - tax_amount: Сумма налога
                - total: Итоговая сумма к оплате

        Example:
            >>> totals = order.calculate_total()
            >>> print(totals['total'])
            1350.0
        """
        subtotal = self.calculate_subtotal()
        discount_amount = subtotal * (self.discount / 100)
        taxable_amount = subtotal - discount_amount
        tax_amount = taxable_amount * self.tax_rate
        total = taxable_amount + tax_amount

        return {
            'subtotal': subtotal,
            'discount_amount': discount_amount,
            'tax_amount': tax_amount,
            'total': total
        }

    def process_order(self):
        """
        Обрабатывает заказ - проверяет доступность и списывает товары.

        Returns:
            bool: True если заказ успешно обработан

        Raises:
            Exception: Если какого-то товара недостаточно на складе
        """
        # Проверяем доступность всех товаров
        for product, quantity in self.items:
            if not product.check_availability(quantity):
                raise Exception(f"Недостаточно товара: {product.name}")

        # Списываем товары со склада
        for product, quantity in self.items:
            product.reduce_availability(quantity)

        self.status = "completed"
        return True

    def order_info(self):
        """
        Возвращает детальную информацию о заказе.

        Returns:
            str: Форматированная строка с полной информацией о заказе
        """
        totals = self.calculate_total()
        info = f"Заказ #{self.order_id}\n"
        info += f"Клиент: {self.customer.name}\n"
        info += "Товары:\n"

        for product, quantity in self.items:
            info += f"  - {product.name}: {quantity} шт. × {product.price} руб. = {quantity * product.price} руб.\n"

        info += f"Промежуточная сумма: {totals['subtotal']:.2f} руб.\n"
        info += f"Скидка: {self.discount}% ({totals['discount_amount']:.2f} руб.)\n"
        info += f"Налог: {self.tax_rate * 100}% ({totals['tax_amount']:.2f} руб.)\n"
        info += f"ИТОГО: {totals['total']:.2f} руб.\n"
        info += f"Статус: {self.status}"

        return info


class Customer:
    """
    Класс клиента магазина.

    Представляет клиента с корзиной покупок и историей заказов.

    Attributes:
        name (str): Имя клиента
        customer_id (str): Уникальный идентификатор клиента
        cart (ShoppingCart): Корзина покупок клиента
        order_history (list): История заказов клиента
    """

    def __init__(self, name, customer_id):
        """
        Инициализирует объект клиента.

        Args:
            name: Имя клиента
            customer_id: Уникальный идентификатор клиента
        """
        self.name = name
        self.customer_id = customer_id
        self.cart = ShoppingCart()
        self.order_history = []

    def add_to_cart(self, product, quantity=1):
        """
        Добавляет товар в корзину клиента.

        Args:
            product: Объект товара
            quantity: Количество товара (по умолчанию 1)
        """
        self.cart.add_product(product, quantity)

    def remove_from_cart(self, product, quantity=1):
        """
        Удаляет товар из корзины клиента.

        Args:
            product: Объект товара
            quantity: Количество для удаления (по умолчанию 1)
        """
        self.cart.del_product(product, quantity)

    def place_order(self, order_id, discount=0):
        """
        Создает и обрабатывает заказ из текущей корзины.

        Args:
            order_id: Уникальный идентификатор заказа
            discount: Процент скидки (по умолчанию 0)

        Returns:
            Order: Созданный объект заказа

        Raises:
            Exception: Если корзина пуста или товаров недостаточно
        """
        if not self.cart.items:
            raise Exception("Корзина пуста!")

        order = Order(order_id, self, self.cart)
        order.apply_discount(discount)

        # Обрабатываем заказ
        order.process_order()

        # Добавляем в историю заказов
        self.order_history.append(order)

        # Очищаем корзину
        self.cart.clear_cart()

        return order

    def get_order_history(self):
        """
        Возвращает историю заказов клиента.

        Returns:
            list: Список объектов Order
        """
        return self.order_history


class ShoppingCart:
    """
    Класс корзины покупок.

    Представляет корзину для временного хранения товаров перед оформлением заказа.

    Attributes:
        items (list): Список товаров в формате (product, quantity)
    """

    def __init__(self):
        """Инициализирует пустую корзину."""
        self.items = []  # Список кортежей (product, quantity)

    def add_product(self, product, quantity=1):
        """
        Добавляет товар в корзину или обновляет количество.

        Args:
            product: Объект товара
            quantity: Количество товара (по умолчанию 1)

        Raises:
            Exception: Если товара недостаточно на складе
        """
        # Проверяем, есть ли уже такой товар в корзине
        for i, (existing_product, existing_quantity) in enumerate(self.items):
            if existing_product == product:
                # Если товар уже есть, обновляем количество
                new_quantity = existing_quantity + quantity
                self.items[i] = (product, new_quantity)
                return

        # Если товара нет в корзине, добавляем новый
        if product.check_availability(quantity):
            self.items.append((product, quantity))
        else:
            raise Exception(f"Недостаточно товара: {product.name}")

    def del_product(self, product_to_delete, quantity=1):
        """
        Удаляет товар из корзины или уменьшает количество.

        Args:
            product_to_delete: Объект товара для удаления
            quantity: Количество для удаления (по умолчанию 1)

        Returns:
            bool: True если товар найден и удален, False в противном случае
        """
        for i, (product, existing_quantity) in enumerate(self.items):
            if product == product_to_delete:
                new_quantity = existing_quantity - quantity

                if new_quantity <= 0:
                    # Полностью удаляем товар
                    del self.items[i]
                else:
                    # Обновляем количество
                    self.items[i] = (product, new_quantity)
                return True
        return False

    def update_product(self, product, new_quantity):
        """
        Обновляет количество конкретного товара в корзине.

        Args:
            product: Объект товара
            new_quantity: Новое количество

        Returns:
            bool: True если обновление успешно

        Raises:
            Exception: Если товара недостаточно на складе
        """
        if new_quantity <= 0:
            # Если количество 0 или меньше, удаляем товар
            return self.del_product(product)

        for i, (existing_product, existing_quantity) in enumerate(self.items):
            if existing_product == product:
                if product.check_availability(new_quantity):
                    self.items[i] = (product, new_quantity)
                    return True
                else:
                    raise Exception(f"Недостаточно товара: {product.name}")

        # Если товара нет в корзине, добавляем
        return self.add_product(product, new_quantity)

    def clear_cart(self):
        """Очищает корзину полностью."""
        self.items = []

    def get_cart_info(self):
        """
        Возвращает информацию о содержимом корзины.

        Returns:
            str: Форматированная строка с содержимым корзины и общей суммой
        """
        if not self.items:
            return "Корзина пуста"

        info = "Содержимое корзины:\n"
        total = 0

        for product, quantity in self.items:
            item_total = product.price * quantity
            info += f"  - {product.name}: {quantity} шт. × {product.price} руб. = {item_total} руб.\n"
            total += item_total

        info += f"Общая сумма: {total} руб."
        return info


# Демонстрация работы
print("=== ДЕМОНСТРАЦИЯ РАБОТЫ МАГАЗИНА ===\n")

# Создаем товары
product1 = Product('комод', 1000, 10, 'мебель')
product2 = Product('стул', 500, 20, 'мебель')
product3 = Product('лампа', 300, 15, 'освещение')

print("Созданные товары:")
print(product1.product_info())
print()
print(product2.product_info())
print("\n" + "="*50 + "\n")

# Создаем клиента
customer = Customer("Иван Иванов", "C001")

# Работа с корзиной
print("Добавляем товары в корзину:")
customer.add_to_cart(product1, 2)
customer.add_to_cart(product2, 1)
customer.add_to_cart(product3, 3)

print(customer.cart.get_cart_info())
print("\n" + "="*50 + "\n")

# Создаем заказ
print("Создаем заказ:")
try:
    order = customer.place_order("ORD001", discount=10)  # 10% скидка
    print(order.order_info())
except Exception as e:
    print(f"Ошибка: {e}")

print("\n" + "="*50 + "\n")

# Проверяем остатки после заказа
print("Остатки на складе после заказа:")
print(f"{product1.name}: {product1.availability} шт.")
print(f"{product2.name}: {product2.availability} шт.")
print(f"{product3.name}: {product3.availability} шт.")

print("\n" + "="*50 + "\n")

# История заказов
print("История заказов клиента:")
for order in customer.get_order_history():
    print(
        f"- Заказ #{order.order_id} на сумму {order.calculate_total()['total']} руб.")
