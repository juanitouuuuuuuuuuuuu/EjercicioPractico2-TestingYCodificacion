# __test__ evita que pytest intente recolectar esta clase como tests.
__test__ = False

class TestDriver:
    """
    NOTA: No es un test de pytest, es una utilidad de apoyo para ejecutar
    métodos y registrar resultados de manera manual.
    Permite ejecutar métodos de un módulo con parámetros y comparar
    contra valores esperados.

    """

    def __init__(self, modulo):
        #'modulo' es una instancia (p. ej., CalculadoraImpuestos)
        self.modulo = modulo
        self.resultados = []

    def ejecutar_prueba_unitaria(self, metodo, parametros, esperado):
        """
        Ejecuta el método 'metodo' del módulo con 'parametros' y compara contra 'esperado'.
        Dejo una pequeña tolerancia por si hubiera decimales.
        
        """
        resultado = getattr(self.modulo, metodo)(*parametros)
        exito = abs(resultado - esperado) < 1e-6
        self.resultados.append({
            "metodo": metodo,
            "parametros": parametros,
            "resultado": resultado,
            "esperado": esperado,
            "exito": exito
        })
        return exito
