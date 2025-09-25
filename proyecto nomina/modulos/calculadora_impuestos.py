class CalculadoraImpuestos:
    """
    Explico:
    - Este módulo calcula impuestos de nómina básicos.
    - ISR por tramos (5%, 10%, 15%) según salario.
    - Seguro social fijo de 6.25%.
    """

    def calcular_isr(self, salario_base: float) -> float:
        """
        ISR por tramos:
          <= 10,000  -> 5%
          <= 20,000  -> 10%
          >  20,000  -> 15%
        """
        if salario_base <= 10000:
            return salario_base * 0.05
        elif salario_base <= 20000:
            return salario_base * 0.10
        else:
            return salario_base * 0.15

    def calcular_seguro_social(self, salario_base: float) -> float:
        """Seguro social: 6.25% del salario base."""
        return salario_base * 0.0625
