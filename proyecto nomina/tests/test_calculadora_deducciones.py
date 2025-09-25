from modulos.calculadora_deducciones import CalculadoraDeducciones

class TestCalculadoraDeducciones:
    """Como estudiante, separo pensión y salud para comprobar el total."""

    def setup_method(self):
        self.cd = CalculadoraDeducciones()

    def test_pension_4_por_ciento(self):
        assert self.cd.calcular_pension(20000) == 800

    def test_salud_3_por_ciento(self):
        assert self.cd.calcular_salud(10000) == 300

    def test_total_deducciones(self):
        # 4% de 15000 = 600; 3% = 450; total 1050
        assert self.cd.calcular_total(15000) == 1050

    def test_salario_cero(self):
        assert self.cd.calcular_pension(0) == 0
        assert self.cd.calcular_salud(0) == 0
        assert self.cd.calcular_total(0) == 0
