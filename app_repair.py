import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

# =====================================================================
# PUNTO 3.3: PANTALLA DE LOGIN (Ventana inicial)
# =====================================================================
class VentanaLogin:
    def __init__(self, root, callback_ingreso):
        self.root = root
        self.callback_ingreso = callback_ingreso
        self.root.title("Repair Center - Login")
        self.root.geometry("350x250")
        self.root.resizable(False, False)
        
        # Centrar elementos de forma estética
        frame = ttk.Frame(root, padding="20")
        frame.pack(expand=True)
        
        ttk.Label(frame, text="SISTEMA REPAIR CENTER", font=("Arial", 12, "bold")).grid(row=0, column=0, columnspan=2, pady=10)
        
        ttk.Label(frame, text="Usuario:").grid(row=1, column=0, sticky="w", pady=5)
        self.txt_usuario = ttk.Entry(frame, width=20)
        self.txt_usuario.grid(row=1, column=1, pady=5)
        self.txt_usuario.insert(0, "admin") # Usuario por defecto para el TP
        
        ttk.Label(frame, text="Contraseña:").grid(row=2, column=0, sticky="w", pady=5)
        self.txt_clave = ttk.Entry(frame, width=20, show="*")
        self.txt_clave.grid(row=2, column=1, pady=5)
        self.txt_clave.insert(0, "1234") # Clave por defecto para el TP
        
        btn_ingresar = ttk.Button(frame, text="Ingresar", command=self.validar_credenciales)
        btn_ingresar.grid(row=3, column=0, columnspan=2, pady=15)
        
    def validar_credenciales(self):
        usuario = self.txt_usuario.get()
        clave = self.txt_clave.get()
        
        if usuario == "admin" and clave == "1234":
            # Si es correcto, destruimos esta ventana y abrimos la app principal
            self.root.destroy()
            self.callback_ingreso()
        else:
            messagebox.showerror("Error", "Usuario o Contraseña incorrectos")


# =====================================================================
# APLICACIÓN PRINCIPAL (Contenedor con Pestañas)
# =====================================================================
class AplicacionPrincipal:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Sistema Integrado - Repair Center")
        self.root.geometry("600x500")
        
        # Componente Notebook para separar el sistema por pestañas
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True)
        
        # Crear los contenedores para cada pestaña
        self.tab_calculadora = ttk.Frame(self.notebook)
        self.tab_repair = ttk.Frame(self.notebook)
        
        self.notebook.add(self.tab_calculadora, text="3.1 Calculadora")
        self.notebook.add(self.tab_repair, text="3.2 Repair Center")
        
        # Cargar los componentes internos de cada pantalla
        self.construir_calculadora()
        self.construir_repair_center()
        
        self.root.mainloop()

    # =====================================================================
    # PUNTO 3.1: CONSTRUIR UNA CALCULADORA (GUI)
    # =====================================================================
    def construir_calculadora(self):
        frame = ttk.LabelFrame(self.tab_calculadora, text=" Operaciones Básicas ", padding="20")
        frame.pack(padx=20, pady=20, fill="both", expand=True)
        
        # Campos numéricos
        ttk.Label(frame, text="Primer Número:").grid(row=0, column=0, sticky="w", pady=5)
        self.num1 = ttk.Entry(frame, width=15)
        self.num1.grid(row=0, column=1, pady=5, padx=5)
        
        ttk.Label(frame, text="Segundo Número:").grid(row=1, column=0, sticky="w", pady=5)
        self.num2 = ttk.Entry(frame, width=15)
        self.num2.grid(row=1, column=1, pady=5, padx=5)
        
        # Botones de Operación
        frame_botones = ttk.Frame(frame)
        frame_botones.grid(row=2, column=0, columnspan=2, pady=15)
        
        ttk.Button(frame_botones, text="Sumar (+)", command=lambda: self.calcular("+")).pack(side="left", padx=2)
        ttk.Button(frame_botones, text="Restar (-)", command=lambda: self.calcular("-")).pack(side="left", padx=2)
        ttk.Button(frame_botones, text="Multiplicar (*)", command=lambda: self.calcular("*")).pack(side="left", padx=2)
        ttk.Button(frame_botones, text="Dividir (/)", command=lambda: self.calcular("/")).pack(side="left", padx=2)
        
        # Pantalla de resultado
        self.lbl_resultado_calc = ttk.Label(frame, text="Resultado: -", font=("Arial", 12, "bold"))
        self.lbl_resultado_calc.grid(row=3, column=0, columnspan=2, pady=10)

    def calcular(self, operacion):
        try:
            val1 = float(self.num1.get())
            val2 = float(self.num2.get())
            
            if operacion == "+": res = val1 + val2
            elif operacion == "-": res = val1 - val2
            elif operacion == "*": res = val1 * val2
            elif operacion == "/":
                if val2 == 0:
                    messagebox.showerror("Error", "No se puede dividir por cero.")
                    return
                res = val1 / val2
            
            # Quitar decimal .0 si es entero puro
            if res.is_integer(): res = int(res)
            self.lbl_resultado_calc.config(text=f"Resultado: {res}")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese números válidos.")

    # =====================================================================
    # PUNTO 3.2: ADMINISTRACIÓN DE REPAIR CENTER (GUI + Lógica)
    # =====================================================================
    def construir_repair_center(self):
        # Frame del Formulario de Entrada
        form = ttk.LabelFrame(self.tab_repair, text=" Registro de Pedido Técnico ", padding="15")
        form.pack(padx=15, pady=10, fill="x")
        
        # 3.2.1 Nombre y Apellido
        ttk.Label(form, text="Cliente (Apellido y Nombre):").grid(row=0, column=0, sticky="w", pady=3)
        self.txt_cliente = ttk.Entry(form, width=35)
        self.txt_cliente.grid(row=0, column=1, columnspan=3, pady=3, sticky="w")
        
        # 3.2.2 Dirección (Calle y Altura)
        ttk.Label(form, text="Calle:").grid(row=1, column=0, sticky="w", pady=3)
        self.txt_calle = ttk.Entry(form, width=20)
        self.txt_calle.grid(row=1, column=1, pady=3, sticky="w")
        
        # Cambié a texto simple para evitar bloqueos por tipo
        ttk.Label(form, text="Altura:").grid(row=1, column=2, sticky="w", pady=3, padx=5)
        self.txt_altura = ttk.Entry(form, width=8)
        self.txt_altura.grid(row=1, column=3, pady=3, sticky="w")
        
        # 3.2.3 Inconveniente
        ttk.Label(form, text="Inconveniente:").grid(row=2, column=0, sticky="w", pady=3)
        self.txt_falla = ttk.Entry(form, width=35)
        self.txt_falla.grid(row=2, column=1, columnspan=3, pady=3, sticky="w")
        
        # 3.2.4 Asignar Técnico
        ttk.Label(form, text="Técnico Asignado:").grid(row=3, column=0, sticky="w", pady=3)
        self.combo_tecnico = ttk.Combobox(form, values=["Ing. Carlos Gómez", "Tec. Sofía Rossi", "Tec. Marcos Díaz"], width=22, state="readonly")
        self.combo_tecnico.grid(row=3, column=1, pady=3, sticky="w")
        self.combo_tecnico.current(0)
        
        # 3.2.5 Agendar Visita (Fecha y Hora)
        ttk.Label(form, text="Fecha (DD/MM/AAAA):").grid(row=4, column=0, sticky="w", pady=3)
        self.txt_fecha = ttk.Entry(form, width=12)
        self.txt_fecha.grid(row=4, column=1, pady=3, sticky="w")
        # Ponemos la fecha del día de hoy como sugerencia
        self.txt_fecha.insert(0, datetime.now().strftime("%d/%m/%Y"))
        
        ttk.Label(frame_hora := ttk.Frame(form), text="Hora (HH:MM):").pack(side="left")
        self.txt_hora = ttk.Entry(frame_hora, width=6)
        self.txt_hora.pack(side="left", padx=5)
        self.txt_hora.insert(0, "15:30")
        frame_hora.grid(row=4, column=2, columnspan=2, sticky="w", pady=3)
        
        # Botón de Registrar Orden
        btn_guardar = ttk.Button(form, text="Agendar Servicio", command=self.registrar_pedido)
        btn_guardar.grid(row=5, column=0, columnspan=4, pady=10)
        
        # Tabla visual para listar los pedidos agendados (Grid/Treeview)
        frame_tabla = ttk.LabelFrame(self.tab_repair, text=" Órdenes Agendadas ", padding="5")
        frame_tabla.pack(padx=15, pady=5, fill="both", expand=True)
        
        self.tabla = ttk.Treeview(frame_tabla, columns=("Cliente", "Direccion", "Falla", "Tecnico", "Turno"), show="headings", height=6)
        self.tabla.pack(side="left", fill="both", expand=True)
        
        # Encabezados de la tabla
        self.tabla.heading("Cliente", text="Cliente")
        self.tabla.heading("Direccion", text="Dirección")
        self.tabla.heading("Falla", text="Inconveniente")
        self.tabla.heading("Tecnico", text="Técnico")
        self.tabla.heading("Turno", text="Fecha/Hora")
        
        # Anchos de columnas
        self.tabla.column("Cliente", width=110)
        self.tabla.column("Direccion", width=110)
        self.tabla.column("Falla", width=120)
        self.tabla.column("Tecnico", width=110)
        self.tabla.column("Turno", width=100)
        
        # Scrollbar para la tabla
        scroll = ttk.Scrollbar(frame_tabla, orient="vertical", command=self.tabla.yview)
        scroll.pack(side="right", fill="y")
        self.tabla.configure(yscrollcommand=scroll.set)

    def registrar_pedido(self):
        cliente = self.txt_cliente.get().strip()
        calle = self.txt_calle.get().strip()
        altura = self.txt_altura.get().strip()
        falla = self.txt_falla.get().strip()
        tecnico = self.combo_tecnico.get()
        fecha = self.txt_fecha.get().strip()
        hora = self.txt_hora.get().strip()
        
        # Validar campos vacíos
        if not (cliente and calle and altura and falla and fecha and hora):
            messagebox.showwarning("Campos Incompletos", "Por favor complete todos los datos del formulario.")
            return
            
        direccion_completa = f"{calle} {altura}"
        turno_completo = f"{fecha} - {hora}"
        
        # Insertar los datos en la tabla visual (Treeview)
        self.tabla.insert("", "end", values=(cliente, direccion_completa, falla, tecnico, turno_completo))
        
        # Notificación de éxito y limpieza de campos
        messagebox.showinfo("Éxito", f"Pedido técnico registrado correctamente para {cliente}.")
        
        self.txt_cliente.delete(0, "end")
        self.txt_calle.delete(0, "end")
        self.txt_altura.delete(0, "end")
        self.txt_falla.delete(0, "end")


# =====================================================================
# SCRIPT DE ARRANQUE GENERAL DEL PROGRAMA
# =====================================================================
if __name__ == "__main__":
    # Creamos la primera ventana (Login)
    raiz_login = tk.Tk()
    
    # Cuando el login sea correcto, esta función abrirá la App Principal
    def ingresar_al_sistema():
        AplicacionPrincipal()
        
    app_login = VentanaLogin(raiz_login, ingresar_al_sistema)
    raiz_login.mainloop()