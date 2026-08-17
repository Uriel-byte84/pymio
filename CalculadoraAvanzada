class CalculadoraAvanzada:
    # =====================================================================
    # 1. ATRIBUTO DE CLASE
    # =====================================================================
    # Esta variable es compartida por todas las calculadoras que se creen.
    # Cuenta el total global de operaciones realizadas en el sistema.
    total_operaciones_globales = 0

    def __init__(self, marca, propietario):
        # =====================================================================
        # 2. CONSTRUCTOR Y ATRIBUTOS DE INSTANCIA
        # =====================================================================
        # Cada calculadora tendrá su propia marca, dueño e historial de operaciones.
        self.marca = marca
        self.propietario = propietario
        self.historial_local = []

    # =====================================================================
    # 3. MÉTODOS DE INSTANCIA (Llevan 'self')
    # =====================================================================
    # Estos métodos modifican el historial de esta calculadora específica
    # e incrementan el contador global de la clase.
    
    def registrar_operacion(self, operacion, resultado):
        # Agrega el registro al historial único del objeto
        self.historial_local.append(f"{operacion} = {resultado}")
        # Modifica el atributo de clase sumando 1 al contador global
        CalculadoraAvanzada.total_operaciones_globales += 1

    def ver_historial(self):
        print(f"\n>> Historial de la calculadora de {self.propietario} ({self.marca}):")
        if not self.historial_local:
            print("No se realizaron operaciones aún.")
        for registro in self.historial_local:
            print(f"  - {registro}")


    # =====================================================================
    # 4. MÉTODOS ESTÁTICOS (Decorador @staticmethod - No llevan self ni cls)
    # =====================================================================
    # Son funciones matemáticas puras independientes que pertenecen a la clase
    # por pura organización. No tocan variables internas.
    
    @staticmethod
    def sumar(a, b):
        return a + b

    @staticmethod
    def restar(a, b):
        return a - b

    @staticmethod
    def multiplicar(a, b):
        return a * b

    @staticmethod
    def dividir(a, b):
        if b == 0:
            return "Error: No se puede dividir por cero"
        return a / b


    # =====================================================================
    # 5. MÉTODOS DE CLASE (Decorador @classmethod - Llevan 'cls')
    # =====================================================================
    # Trabajan sobre la clase entera. Lo usamos como una 'fábrica' para crear
    # rápidamente calculadoras preconfiguradas para estudiantes.
    
    @classmethod
    def crear_calculadora_escolar(cls, nombre_alumno):
        # Retorna una nueva instancia pasándole marca 'Casio Escolar' por defecto
        return cls(marca="Casio Escolar", propietario=nombre_alumno)


# =====================================================================
# SCRIPT DE PRUEBA: Consumiendo la Calculadora por Consola
# =====================================================================
if __name__ == "__main__":
    print("--- PROGRAMA PRINCIPAL: CALCULADORA ORIENTADA A OBJETOS ---\n")

    # A) Uso de la Fábrica (Método de Clase) para crear dos calculadoras distintas
    calc1 = CalculadoraAvanzada("Texas Instruments", "Carlos")
    calc2 = CalculadoraAvanzada.crear_calculadora_escolar("Sofía") # Usa @classmethod

    # B) Realizar operaciones usando los Métodos Estáticos y guardando historial
    print("Realizando cálculos...")
    
    # Operaciones de Carlos (calc1)
    res_suma = CalculadoraAvanzada.sumar(10, 5) # Método Estático
    calc1.registrar_operacion("10 + 5", res_suma) # Método de Instancia

    res_div = CalculadoraAvanzada.dividir(20, 4)
    calc1.registrar_operacion("20 / 4", res_div)

    # Operaciones de Sofía (calc2)
    res_mult = CalculadoraAvanzada.multiplicar(6, 7)
    calc2.registrar_operacion("6 * 7", res_mult)

    print("¡Cálculos finalizados exitosamente!")
    print("-" * 60)

    # C) Visualizar historiales locales (Métodos de Instancia)
    # Cada calculadora recuerda únicamente sus operaciones propias
    calc1.ver_historial()
    calc2.ver_historial()
    print("-" * 60)

    # D) Verificar el Atributo de Clase Global
    # Muestra la suma total de operaciones hechas por ambas calculadoras unificadas
    print(f">> REPORTE DEL SISTEMA:")
    print(f"Total global de operaciones matemáticas realizadas: {CalculadoraAvanzada.total_operaciones_globales}")