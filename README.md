# EjercicioPractico2-TestingYCodificacion

# Test del Bottom Up.py

<img width="1213" height="868" alt="Captura de pantalla 2025-09-24 233131" src="https://github.com/user-attachments/assets/a7e27ea0-464d-4752-b32a-547f6e934e70" />

# Test y demostración del Coverage

<img width="1919" height="428" alt="Captura de pantalla 2025-09-24 233147" src="https://github.com/user-attachments/assets/26ddc7d8-dd34-4c32-92dc-d9c7b3870113" />

# Diagrama de Integración

<img width="1678" height="635" alt="DiagramadeIntegracion" src="https://github.com/user-attachments/assets/3df73510-4a01-4419-8a99-ced25cf341f6" />

# Análisis general del conjunto e impacto de la estrategia Bottom-Up

## Contexto del proyecto
El sistema de nómina quedó estructurado en módulos atómicos y bien delimitados:
- **CalculadoraImpuestos**: tramos de ISR y cálculo de seguro social.
- **CalculadoraDeducciones**: pensión, salud y total de deducciones.
- **CalculadoraBonos**: bonos por antigüedad y productividad (con límites y tramos claros).
- **NominaSistema**: capa de integración que orquesta los tres módulos para producir el resumen de nómina (neto sin bonos y neto final).

Se añadieron pruebas unitarias por módulo y pruebas de integración progresiva (parcial y completa), más configuración para generar reporte de cobertura en **HTML** y hacer cumplir un umbral **≥ 80%**.

---

## Qué se entregó (alcance técnico)
- **Módulos base** con reglas deterministas, documentados con docstrings y comentarios.
- **Pruebas unitarias (Nivel 0)** para cada cálculo: tramos, bordes, valores fuera de rango y casos de salario cero.
- **Integración parcial (Nivel 2)**: combinación de impuestos + deducciones para obtener `neto_sin_bonos`.
- **Integración completa (Nivel 3)**: suma de bonos (antigüedad y productividad) para obtener `neto` final.
- **Driver de apoyo** (no recolectado por pytest) para ejecutar métodos manualmente cuando se necesite.
- **Cubrimiento** con `pytest-cov` y reporte navegable en `htmlcov/index.html`. Se configuró `--cov-fail-under=80` para garantizar el mínimo de calidad.

---

## Flujo de integración (progresiva)
1. **Nivel 0 – Pruebas unitarias**: cada módulo valida sus reglas sin dependencias externas.  
2. **Nivel 2 – Integración parcial**: `NominaSistema` usa Impuestos y Deducciones; se verifica `neto_sin_bonos`.  
3. **Nivel 3 – Integración completa**: se añaden Bonos; se valida el `neto` final con escenarios representativos.

Este enfoque escalonado permitió aislar errores en la capa exacta donde se originan y avanzar sin fricción entre niveles.

---

## Beneficios concretos de haber usado Bottom-Up
1. **Calidad desde la base**: al blindar primero los módulos, la integración se volvió un ensamblaje predecible, sin sorpresas de reglas mal definidas.  
2. **Detección temprana de defectos**: errores de bordes (p. ej., 49/50, 79/80, 94/95 de productividad; 10k/20k de ISR) se capturaron en unit tests, no en la integración.  
3. **Feedback rápido**: pruebas muy veloces y deterministas (cero I/O) facilitan iterar y refactorizar sin miedo.  
4. **Diseño claro y mantenible**: interfaces pequeñas, responsabilidad única y contratos explícitos; facilita agregar nuevos tramos, prestaciones o deducciones sin romper lo existente.  
5. **Cobertura sostenida**: el objetivo ≥ 80% (ampliable a 100%) con reporte HTML hace visible dónde falta probar y guía mejoras continuas.  
6. **Menor acoplamiento**: `NominaSistema` depende de comportamientos estables; cambiar fórmulas internas no afecta la orquestación si se respetan contratos.  
7. **Escalabilidad funcional**: nuevos módulos (p. ej., retenciones adicionales) pueden entrar por el mismo patrón: primero unit, luego integración parcial, luego completa.

---

## Comparación breve con Top-Down (complementariedad)
- **Top-Down** ayuda a validar pronto el recorrido de negocio “end-to-end” (útil cuando se quiere ver rápido el caso de uso funcionando).  
- **Bottom-Up** asegura que los bloques que alimentan ese recorrido estén sólidos y probados exhaustivamente antes de ensamblarlos.

En este proyecto, el **Bottom-Up** resultó **decisivo** para la robustez de las fórmulas y la facilidad de integración. Si en fases previas se usó Top-Down para visualizar el flujo, el Bottom-Up terminó de consolidar la calidad técnica y la mantenibilidad.

---

## Riesgos y cómo se mitigaron
- **Pruebas que no cargan cobertura** → se mitigó midiendo por paquete (`--cov=modulos`) y asegurando `__init__.py`.  
- **Falsos positivos por rutas no ejecutadas** → se añadieron casos de borde y `term-missing` para detectar líneas sin cubrir.  
- **Utilitarios confundidos como tests** → se renombró/“silenció” el driver para que pytest no lo recolecte.

---

## Resultados y métricas
- **Cobertura ≥ 80%** (configurada como umbral mínimo) y **reporte HTML** para revisión.  
- **Pruebas unitarias** que cubren tramos, límites y valores fuera de rango.  
- **Pruebas de integración** que validan el cálculo completo de nómina paso a paso.  
- **Código documentado** “como estudiante”, legible y listo para evaluación.

---

## Lecciones aprendidas
- Diseñar primero **contratos simples** y **tablas de decisión** acelera tanto los tests como el desarrollo.  
- La **integración progresiva** evita “debacles de última hora”: cada nivel agrega valor y confirma estabilidad.  
- Mantener la **cobertura visible** en HTML motiva a cerrar huecos y deja evidencia clara para revisión académica o de pares.

---

## Trabajo futuro
- Añadir **ramas** en cobertura (`--cov-branch`) si se requiere granularidad sobre decisiones internas.  
- Extender **bonos/deducciones** con nuevas reglas y parametrizaciones (p. ej., topes, exenciones).  
- Incorporar **validación de entradas** y manejo de errores explícito (tipos y rangos), con sus tests correspondientes.  
- Publicar **diagramas** (componentes y secuencia) en formato SVG/PNG dentro del repositorio para documentación completa.

---

**Conclusión**: la estrategia **Bottom-Up** fue altamente influyente en la calidad final. Permitió asegurar exactitud numérica, simplicidad de mantenimiento y una integración sin fricciones, con evidencia objetiva (cobertura y tests) de que el sistema cumple los criterios funcionales y de calidad definidos.
