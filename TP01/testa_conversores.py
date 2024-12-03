import conversores as con


def teste():

    # C° para F°
    print(f'{con.celsius_para_fahrenheit(5)} graus F°')

    # F° para C°
    print(f'{con.fahrenheit_para_celsius(5)} graus C°')

    # M para Pés
    print(f'{con.metros_para_pes(5)} pés')

    # Pés para M
    print(f'{con.pes_para_metros(5)}m')

    # Km para milhas
    print(f'{con.quilometros_para_milhas(5)} milhas')

    # Milhas para Km
    print(f'{con.milhas_para_quilometros(5)}km')

    # Dia para horas
    print(f'{con.dia_para_horas(5)}h')


teste()
