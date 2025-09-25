class CalculadoraDeducciones:
    """
    En este modulo se implementan cálculos, en los cuales se maneja los siguientes parametros:
    - Deducciones “empleado” simples: pensión 4% y salud 3%.
    - La total es la suma de ambas, para facilitar la integración posterior.
    """

    def calcular_pension(self, salario_base: float) -> float:
        """Pensión: 4% del salario base."""
        return salario_base * 0.04

    def calcular_salud(self, salario_base: float) -> float:
        """Salud: 3% del salario base."""
        return salario_base * 0.03

    def calcular_total(self, salario_base: float) -> float:
        """Total deducciones = pensión + salud."""
        return self.calcular_pension(salario_base) + self.calcular_salud(salario_base)
