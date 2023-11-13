from ship_types import get_ship_class_by_name, ShipType

if __name__ == '__main__':
    print(ShipType.INTERCEPTOR)
    # print(get_ship_class_by_name('interceptor'))
    print(get_ship_class_by_name('interceptor') == ShipType.INTERCEPTOR)
    print(get_ship_class_by_name('intERCEptoR') == ShipType.INTERCEPTOR)