from modulos.calculadora_impuestos import CalculadoraImpuestos
from modulos.calculadora_deducciones import CalculadoraDeducciones
from modulos.calculadora_bonos import CalculadoraBonos

class NominaSistema:
    """
    Como estudiante, explico mi diseño:
    - Inyecto las calculadoras (Bottom-Up) para poder probarlas por separado y luego integrarlas.
    - El cálculo final integra: ISR, Seguro Social, Deducciones (pensión+salud) y Bonos (antigüedad+productividad).
    """

    def __init__(self,
                 calc_impuestos: CalculadoraImpuestos | None = None,
                 calc_deducciones: CalculadoraDeducciones | None = None,
                 calc_bonos: CalculadoraBonos | None = None):
        # Si no me pasan instancias, creo las “por defecto”.
        self.imp = calc_impuestos or CalculadoraImpuestos()
        self.ded = calc_deducciones or CalculadoraDeducciones()
        self.bon = calc_bonos or CalculadoraBonos()

    def calcular_resumen(self, salario_base: float, anios_servicio: int = 0, productividad: int = 0) -> dict:
        """
        Retorno un resumen con componentes y totales intermedios para facilitar las pruebas:
        - impuestos: {'isr', 'seguro_social'}
        - deducciones: {'pension', 'salud', 'total'}
        - bonos: {'antiguedad', 'productividad', 'total'}
        - neto_sin_bonos, neto
        """
        # Impuestos
        isr = self.imp.calcular_isr(salario_base)
        seguro = self.imp.calcular_seguro_social(salario_base)

        # Deducciones
        pension = self.ded.calcular_pension(salario_base)
        salud = self.ded.calcular_salud(salario_base)
        ded_total = self.ded.calcular_total(salario_base)

        # Bonos
        bono_ant = self.bon.calcular_bono_antiguedad(anios_servicio, salario_base)
        bono_prod = self.bon.calcular_bono_productividad(productividad, salario_base)
        bono_total = bono_ant + bono_prod

        # Neto sin bonos (útil para el nivel 2 de integración)
        neto_sin_bonos = salario_base - isr - seguro - ded_total
        # Neto final (nivel 3)
        neto = neto_sin_bonos + bono_total

        return {
            "impuestos": {"isr": isr, "seguro_social": seguro},
            "deducciones": {"pension": pension, "salud": salud, "total": ded_total},
            "bonos": {"antiguedad": bono_ant, "productividad": bono_prod, "total": bono_total},
            "neto_sin_bonos": neto_sin_bonos,
            "neto": neto,
        }
