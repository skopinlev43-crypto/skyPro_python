from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 15", "+79111111111"),
    Smartphone("Samsung", "Galaxy S24", "+79222222222"),
    Smartphone("Xiaomi", "14 Ultra", "+79333333333"),
    Smartphone("Google", "Pixel 8 Pro", "+79444444444"),
    Smartphone("Huawei", "Pura 70", "+79555555555"),
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
