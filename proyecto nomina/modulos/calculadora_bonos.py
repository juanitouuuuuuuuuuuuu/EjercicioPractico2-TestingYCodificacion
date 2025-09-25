class CalculadoraBonos:
    """
    En este modulo se implementan cálculos:
    - Bonos por antigüedad y productividad con tramos deterministas.
    - Esto permite pruebas unitarias exactas y reproducibles.
    """

    def calcular_bono_antiguedad(self, anios_servicio: int, salario_base: float) -> float:
        """
        Antigüedad:
          < 1        -> 0%
          1 a 3      -> 5%
          4 a 7      -> 10%
          >= 8       -> 15%
        """
        if anios_servicio < 1:
            tasa = 0.00
        elif anios_servicio <= 3:
            tasa = 0.05
        elif anios_servicio <= 7:
            tasa = 0.10
        else:
            tasa = 0.15
        return salario_base * tasa

    def calcular_bono_productividad(self, puntaje: int, salario_base: float) -> float:
        """
        Productividad (se 'clamp' el puntaje a [0,100]):
          0-49   -> 0%
          50-79  -> 5%
          80-94  -> 10%
          95-100 -> 15%
        """
        p = 0 if puntaje < 0 else 100 if puntaje > 100 else puntaje

        if p < 50:
            tasa = 0.00
        elif p <= 79:
            tasa = 0.05
        elif p <= 94:
            tasa = 0.10
        else:
            tasa = 0.15
        return salario_base * tasa
