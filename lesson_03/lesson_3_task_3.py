from address import Address
from mailing import Mailing

to_addr = Address("101000", "Москва", "Тверская", "12", "45")
from_addr = Address("610000", "Киров", "Ленина", "84", "12")

mailing = Mailing(
    to_address=to_addr,
    from_address=from_addr,
    cost=350.50,
    track="TRACK123456RU",
)

f_addr = mailing.from_address
t_addr = mailing.to_address

print(
    f"Отправление {mailing.track} "
    f"из {f_addr.index}, {f_addr.city}, {f_addr.street}, {f_addr.house} - {f_addr.apartment} "
    f"в {t_addr.index}, {t_addr.city}, {t_addr.street}, {t_addr.house} - {t_addr.apartment}. "
    f"Стоимость {mailing.cost} рублей."
)
