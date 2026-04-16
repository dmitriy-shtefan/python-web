# Робота з товарами (E-commerce API)

```python
(product_id, name, price, category)
```

```python
products = [
    (1, "Laptop", 1200, "electronics"),
    (2, "Mouse", 25, "electronics"),
    (3, "Keyboard", 75, "electronics"),
    (4, "Monitor", 300, "electronics"),
    (5, "Headphones", 150, "electronics"),
    (6, "Webcam", 80, "electronics"),
    (7, "USB Cable", 10, "accessories"),
    (8, "Charger", 40, "accessories"),
    (9, "Tablet", 600, "electronics"),
    (10, "Smartphone", 900, "electronics"),

    (11, "Desk", 250, "furniture"),
    (12, "Chair", 180, "furniture"),
    (13, "Lamp", 60, "furniture"),
    (14, "Microphone", 200, "electronics"),
    (15, "Speaker", 120, "electronics"),
    (16, "Router", 130, "network"),
    (17, "SSD", 160, "hardware"),
    (18, "HDD", 90, "hardware"),
    (19, "GPU", 1500, "hardware"),
    (20, "CPU", 400, "hardware"),

    (21, "Motherboard", 220, "hardware"),
    (22, "RAM 8GB", 70, "hardware"),
    (23, "RAM 16GB", 130, "hardware"),
    (24, "Power Supply", 110, "hardware"),
    (25, "Cooling Fan", 35, "hardware"),
    (26, "Laptop Stand", 45, "accessories"),
    (27, "Docking Station", 180, "electronics"),
    (28, "External SSD", 210, "hardware"),
    (29, "External HDD", 100, "hardware"),
    (30, "Graphics Tablet", 350, "electronics"),

    (31, "Smartwatch", 250, "wearables"),
    (32, "Fitness Tracker", 90, "wearables"),
    (33, "Camera", 800, "electronics"),
    (34, "Tripod", 70, "accessories"),
    (35, "Drone", 1200, "electronics"),
    (36, "VR Headset", 500, "electronics"),
    (37, "Gamepad", 60, "gaming"),
    (38, "Console", 700, "gaming"),
    (39, "TV 50\"", 650, "electronics"),
    (40, "TV 65\"", 1200, "electronics"),

    (41, "Projector", 900, "electronics"),
    (42, "Soundbar", 300, "electronics"),
    (43, "Blu-ray Player", 150, "electronics"),
    (44, "NAS Storage", 600, "network"),
    (45, "Server Rack", 800, "network"),
    (46, "Switch", 200, "network"),
    (47, "Access Point", 180, "network"),
    (48, "Firewall Device", 1000, "network"),
    (49, "Smart Plug", 30, "smart_home"),
    (50, "Smart Bulb", 20, "smart_home"),

    (51, "Smart Thermostat", 220, "smart_home"),
    (52, "Security Camera", 140, "smart_home"),
    (53, "Door Lock Smart", 260, "smart_home"),
    (54, "Electric Scooter", 700, "transport"),
    (55, "E-bike", 1500, "transport"),
    (56, "Power Bank", 50, "accessories"),
    (57, "Wireless Charger", 45, "accessories"),
    (58, "Car Charger", 25, "accessories"),
    (59, "Dash Cam", 120, "automotive"),
    (60, "GPS Navigator", 200, "automotive"),

    (61, "Office Software License", 120, "software"),
    (62, "Antivirus License", 60, "software"),
    (63, "Cloud Storage 1TB", 100, "software"),
    (64, "Domain Name", 15, "software"),
    (65, "Web Hosting", 80, "software"),
    (66, "VPS Hosting", 200, "software"),
    (67, "Dedicated Server", 1200, "software"),
    (68, "SSL Certificate", 50, "software"),
    (69, "Email Hosting", 40, "software"),
    (70, "VPN Subscription", 70, "software"),

    (71, "Keyboard Mechanical", 180, "gaming"),
    (72, "Mouse Gaming", 90, "gaming"),
    (73, "Monitor 144Hz", 400, "gaming"),
    (74, "Monitor 240Hz", 600, "gaming"),
    (75, "Laptop Gaming", 1800, "gaming"),
    (76, "Chair Gaming", 350, "gaming"),
    (77, "Desk Gaming", 450, "gaming"),
    (78, "RGB Lights", 70, "gaming"),
    (79, "Capture Card", 220, "gaming"),
    (80, "Streaming Mic", 250, "gaming"),

    (81, "Smart Glasses", 900, "wearables"),
    (82, "3D Printer", 700, "hardware"),
    (83, "Filament PLA", 30, "hardware"),
    (84, "Filament ABS", 35, "hardware"),
    (85, "Laser Cutter", 2000, "hardware"),
    (86, "CNC Machine", 3000, "hardware"),
    (87, "Toolkit", 120, "tools"),
    (88, "Soldering Station", 90, "tools"),
    (89, "Multimeter", 60, "tools"),
    (90, "Oscilloscope", 800, "tools"),

    (91, "Arduino Kit", 80, "hardware"),
    (92, "Raspberry Pi", 120, "hardware"),
    (93, "Sensor Kit", 70, "hardware"),
    (94, "Robot Kit", 200, "hardware"),
    (95, "AI Camera Module", 150, "hardware"),
    (96, "Edge TPU", 180, "hardware"),
    (97, "Smart Mirror", 500, "smart_home"),
    (98, "Digital Frame", 100, "electronics"),
    (99, "E-reader", 220, "electronics"),
    (100, "Portable Monitor", 300, "electronics")
]
```
## Завдання

Використай той самий список `products`.

1. Знайти найдешевший товар у списку `products`
2. Знайти всі унікальні категорії товарів
3. Побудувати словник: `{category: count_products}`. Тобто порахувати, скільки товарів у кожній категорії
4. Відсортувати список `products` за `price` за зростанням
5. Реалізувати генератор, який:
   приймає `products` і повертає тільки назви товарів з категорії `"electronics"`
6. Реалізувати функцію:
```python
def create_category_filter(category):
```
яка повертає функцію, що перевіряє, чи належить товар до переданої категорії

Використання:
```python
electronics_filter = create_category_filter("electronics")
list(filter(electronics_filter, products))
```

7. Написати декоратор `show_calls`, який при кожному виклику функції виводить повідомлення:
`Функцію викликано`

Використання:
```python
@show_calls
def get_cheap_products(products):
    return [p for p in products if p[2] < 100]
```

## Завдання (more complex)

1. Знайти найдорожчий товар у списку products
2. Знайти категорії, які: мають і дешеві товари (<100) і дорогі (>500)
3. Побудувати словник: {category: average_price}. Потім знайти категорію з максимальним середнім чеком
4. Відсортувати список products: спочатку за category, потім за price (за зростанням)
5. Реалізувати генератор, який: приймає products і повертає тільки назви товарів дорожче 500
6. Реалізувати функцію: def create_price_filter(min_price): яка повертає функцію, що перевіряє чи товар дорожчий за min_price
Використання:
```python
    expensive_filter = create_price_filter(500)
    list(filter(expensive_filter, products))
```
7. Написати декоратор count_calls, який рахує, скільки разів була викликана функція і виводить це число
Використання:
```python
@count_calls
def get_expensive_products(products):
    return [p for p in products if p[2] > 500]
```