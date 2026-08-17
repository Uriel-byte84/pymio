class Auto:
    # --- ATRIBUTO DE CLASE ---
    # Todos los autos creados comparten esta misma cantidad de ruedas
    ruedas = 4 

    # --- EL CONSTRUCTOR ---
    def __init__(self, marca, modelo):
        # --- ATRIBUTOS DE INSTANCIA ---
        # Cada auto tendrá su propia marca y modelo únicos
        self.marca = marca
        self.modelo = modelo
        self.__encendido = False  # Atributo privado

    # --- 1. MÉTODO DE INSTANCIA ---
    # Necesita usar 'self' para modificar el estado de este auto en particular
    def encender_motor(self):
        self.__encendido = True
        return f"El {self.marca} ha encendido el motor."

    # --- 2. MÉTODO DE CLASE ---
    # Usa 'cls'. Puede crear un auto preconfigurado sin que el usuario llene los datos
    @classmethod
    def crear_auto_de_fabrica(cls):
        # Retorna una instancia con valores por defecto
        return cls("Fiat", "Cronos")

    # --- 3. MÉTODO ESTÁTICO ---
    # No usa datos internos. Es solo una función utilitaria del ecosistema Auto
    @staticmethod
    def kilometros_a_millas(kms):
        return kms * 0.621371


# --- PRUEBA DEL EJEMPLO EN CONSOLA ---

# Uso de Atributo de Clase (No requiere crear un objeto)
print(f"Cualquier auto tiene: {Auto.ruedas} ruedas.")

# Uso de Método Estático (No requiere crear un objeto)
print(f"100 km son: {Auto.kilometros_a_millas(100)} millas.")

# Creación de un objeto (Constructor en acción)
mi_auto = Auto("Ford", "Mustang") 

# Uso de Método de Instancia
print(mi_auto.encender_motor()) 

# Uso de Método de Clase para fabricar otro auto automáticamente
auto_por_defecto = Auto.crear_auto_de_fabrica()
print(f"Auto de fábrica creado: {auto_por_defecto.marca} {auto_por_defecto.modelo}")