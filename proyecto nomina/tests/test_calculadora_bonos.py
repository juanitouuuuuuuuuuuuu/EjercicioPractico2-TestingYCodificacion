import pytest
from modulos.calculadora_bonos import CalculadoraBonos

class TestCalculadoraBonos:
    """Aqui pruebo tramos de antigüedad y productividad con parametrización."""

    def setup_method(self):
        self.cb = CalculadoraBonos()

    @pytest.mark.parametrize("anios,salario,esperado", [
        (0, 10000, 0), (1, 10000, 500), (3, 12000, 600),
        (4, 10000, 1000), (7, 8000, 800), (8, 10000, 1500), (12, 20000, 3000),
    ])
    def test_bono_antiguedad_tramos(self, anios, salario, esperado):
        assert self.cb.calcular_bono_antiguedad(anios, salario) == esperado

    @pytest.mark.parametrize("puntaje,salario,esperado", [
        (40, 8000, 0), (50, 8000, 400), (79, 10000, 500),
        (80, 10000, 1000), (94, 12000, 1200), (95, 8000, 1200), (100, 10000, 1500),
    ])
    def test_bono_productividad_tramos(self, puntaje, salario, esperado):
        assert self.cb.calcular_bono_productividad(puntaje, salario) == esperado

    @pytest.mark.parametrize("puntaje,salario,esperado", [(-10, 10000, 0), (120, 10000, 1500)])
    def test_bono_productividad_bounds(self, puntaje, salario, esperado):
        assert self.cb.calcular_bono_productividad(puntaje, salario) == esperado
