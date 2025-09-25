from modulos.calculadora_impuestos import CalculadoraImpuestos
from modulos.calculadora_deducciones import CalculadoraDeducciones
from modulos.calculadora_bonos import CalculadoraBonos
from nomina_sistema import NominaSistema

def test_nivel_2_integracion_sin_bonos():
    """
    Como estudiante, primero integro impuestos + deducciones.
    Caso: salario=10000
      ISR (5%)=500, Seguro(6.25%)=625 → Impuestos=1125
      Deducciones: pensión(4%)=400 + salud(3%)=300 → 700
      Neto sin bonos = 10000 - 1125 - 700 = 8175
    """
    sistema = NominaSistema(CalculadoraImpuestos(), CalculadoraDeducciones(), CalculadoraBonos())
    resumen = sistema.calcular_resumen(10000, anios_servicio=0, productividad=0)
    assert resumen["neto_sin_bonos"] == 8175

def test_nivel_3_integracion_completa_con_bonos():
    """
    Integro todo: impuestos + deducciones + bonos.
    Mismos datos, pero con bonos:
      Antigüedad (4 años)=10% de 10000=1000
      Productividad (95)=15% de 10000=1500
      Bonos totales = 2500
      Neto final = 8175 + 2500 = 10675
    """
    sistema = NominaSistema(CalculadoraImpuestos(), CalculadoraDeducciones(), CalculadoraBonos())
    resumen = sistema.calcular_resumen(10000, anios_servicio=4, productividad=95)
    assert resumen["neto"] == 10675
