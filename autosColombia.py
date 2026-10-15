import tkinter as tk
from tkinter import messagebox
import mysql.connector
from datetime import datetime

# MODELO FÍSICO / CONEXIÓN A BASE DE DATOS

def conectar():

    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="autos_colombia"
    )

# CONTROLADOR Y PATRÓN DAO
def registrar_entrada():
    placa = entry_placa.get().upper()
    if not placa:
        messagebox.showwarning("Error", "La placa no puede estar vacía")
        return
    try:
        db = conectar()
        cursor = db.cursor()
        hora_actual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Inserción en la base de datos (Entrada)
        sql = "INSERT INTO registros (placa, tipo, hora_entrada, estado) VALUES (%s, %s, %s, 'Adentro')"
        cursor.execute(sql, (placa, "Vehiculo", hora_actual))
        db.commit()
        db.close()

        messagebox.showinfo("Éxito", f"Entrada registrada: {placa}\nHora: {hora_actual}")
        entry_placa.delete(0, tk.END)
    except Exception as e:
        messagebox.showerror("Error de Base de Datos", str(e))

def registrar_salida():
    placa = entry_buscar.get().upper()
    if not placa:
        messagebox.showwarning("Error", "Ingrese una placa para dar salida")
        return
    try:
        db = conectar()
        cursor = db.cursor()
        hora_actual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Actualización en la base de datos (Salida)
        sql = "UPDATE registros SET hora_salida = %s, estado = 'Afuera' WHERE placa = %s AND estado = 'Adentro'"
        cursor.execute(sql, (hora_actual, placa))

        if cursor.rowcount > 0:
            db.commit()
            messagebox.showinfo("Éxito", f"Salida registrada: {placa}\nHora: {hora_actual}")
        else:
            messagebox.showwarning("Error", "Vehículo no encontrado o ya salió")

        db.close()
        entry_buscar.delete(0, tk.END)
    except Exception as e:
        messagebox.showerror("Error de Base de Datos", str(e))

# VISTA

root = tk.Tk()
root.title("Sistema Autos Colombia - Iteración 1")
root.geometry("400x350")
root.configure(bg="#F0F0F0")

# Entrada

tk.Label(root, text="Parqueadero Autos Colombia - Ingreso", font=("Arial", 12, "bold"), bg="#F0F0F0").pack(pady=10)
tk.Label(root, text="Número de Placa:", bg="#F0F0F0").pack()
entry_placa = tk.Entry(root, font=("Arial", 14), justify="center")
entry_placa.pack(pady=5)

btn_entrada = tk.Button(root, text="REGISTRAR ENTRADA", bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), command=registrar_entrada)
btn_entrada.pack(pady=10)

tk.Frame(root, height=2, bd=1, relief="sunken").pack(fill="x", pady=10)

# Salida

tk.Label(root, text="Registro de Salida", font=("Arial", 12, "bold"), bg="#F0F0F0").pack(pady=10)
tk.Label(root, text="Buscar Placa:", bg="#F0F0F0").pack()
entry_buscar = tk.Entry(root, font=("Arial", 14), justify="center")
entry_buscar.pack(pady=5)

btn_salida = tk.Button(root, text="REGISTRAR SALIDA", bg="#F44336", fg="white", font=("Arial", 10, "bold"), command=registrar_salida)
btn_salida.pack(pady=10)

# Ejecutar la aplicación

root.mainloop()