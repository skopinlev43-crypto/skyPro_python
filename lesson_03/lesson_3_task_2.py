from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 15", "+79111234567"),
    Smartphone("Samsung", "Galaxy S24", "+79223334568"),
    Smartphone("Xiaomi", "14 Pro", "+79121234569"),
    Smartphone("Google", "Pixel 8", "+79991234570"),
    Smartphone("Huawei", "Pura 70", "+74951234572")
]

for phone in catalog:
    print(f"{phone.brand}  {phone.model}: {phone.phone_number}")