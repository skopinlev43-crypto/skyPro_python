from adress import Address
from mailing import Mailing

from_adr = Address("610035", "г.Киров", "ул.Сурикова", "д.4", "кв.5")
to_adr = Address("610000", "г.Санкт-Петербург", "Невский проспект", "д.25", "кв.18")

shipment = Mailing(
    to_address=to_adr,
    from_address=from_adr,
    cost=450.50,
    track="RU123456780"
)

print(
    f"Отправление {shipment.track} из {shipment.from_address.index}, {shipment.from_address.city}, "
    f"{shipment.from_address.street}, {shipment.from_address.house} - {shipment.from_address.apartment} "
    f"в {shipment.to_address.index}, {shipment.to_address.city}, {shipment.to_address.street}, "
    f"{shipment.to_address.house} - {shipment.to_address.apartment}. Стоимость {shipment.cost} рублей."
)
