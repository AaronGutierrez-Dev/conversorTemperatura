#Importar librerias necesarias. Para este caso se utilizaran customtkinter ya que presenta una estética mejor que tkinter.
import customtkinter as ctk

#Creación de la lista: celsius, fahrenheit y kelvin como principales temperaturas (más utilizadas).

magnitudes = ["Celsius", "Fahrenheit", "Kelvin"]

#Se plantea la función de conversión base donde por medio de condicionales se establecen las posibles operaciones de conversión que el usuari opodrá seleccionar.

def conversion_temperatura():
    #Se utiliza la estructura de manejo de excepciones TRY - EXCEPT para tener mayor control en caso de que ocurra un error al momento de ejecutar el código.
    try:
        #Por medio del método .get se obtienen los datos como lo son el valor de temperatura a convertir y la selección de las temperaturas desde a hacia.
        valor_ingreso = float(entry_temperatura_desde.get())
        desde = combobox_temperatura_desde.get()
        hacia = combobox_temperatura_hacia.get()

        #Conversión según las fórmulas conocidas.

        if desde == hacia:
            resultado = valor_ingreso
        elif desde == "Celsius" and hacia == "Fahrenheit":
            resultado = ((1.8 * valor_ingreso)+32)
        elif desde == "Fahrenheit" and hacia == "Celsius":
            resultado = 1.8*(valor_ingreso - 32)
        elif desde == "Celsius" and hacia == "Kelvin":
            resultado = valor_ingreso + 273
        elif desde == "Kelvin" and hacia == "Celsius":
            resultado = valor_ingreso - 273
        elif desde == "Fahrenheit" and hacia == "Kelvin":
            resultado = (1.8 * (valor_ingreso-32)) + 273
        elif desde == "Kelvin" and hacia == "Fahrenheit":
            resultado = (1.8 * (valor_ingreso - 273)) + 32
        else:
            resultado = None

        
        #Mostrar el resultado: por medio de los métodos .configure(), .delete(), e insert() se establecen las ordenes de que la casilla de resultado pueda ser modificada, se borre cualquier resultado anterior, aparezca el resultado nuevo y este permaneza en solo lectura para que no sea modificado.
        if resultado is not None:
            label_resultado.configure(state="normal")
            label_resultado.delete(0, ctk.END)
            label_resultado.insert(0, f"°{valor_ingreso} {desde} equivalen a °{resultado: .2f} {hacia}")
            label_resultado.configure(state="readonly")
        #En caso de que la conversión no sea válida por errores numéricos por ejemplo, se mostrará el mensaje de que la conversión no es válida entre las unidades.
        else:
            label_resultado.configure(state="normal")
            label_resultado.delete(0, ctk.END)
            label_resultado.insert(0, "Conversión no válida")
            label_resultado.configure(state="readonly")

    
    #Control errores: según el tipo de error que aparezca en la plataforma, se mostrará en la casilla de resultado.
    except ValueError:
        label_resultado.configure(state="normal")
        label_resultado.delete(0, ctk.END)
        label_resultado.inster(0, "Entrada inválida")
        label_resultado.configure(state="readonly")

#Configuración de la ventana principal.
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

#Creación de la ventana principal.
conversor = ctk.CTk()
conversor.title("Conversor de temperatura")
conversor.geometry('370x500')
conversor.resizable(width=False, height=False)

#crear fuente en negrita.
fuente_negrita_texto = ctk.CTkFont(family= "Segoe UI", size=20, weight="bold")

#Label encabezado.
label_encabezado = ctk.CTkLabel(master=conversor, text="Conversor de temperatura", font=fuente_negrita_texto)
label_encabezado.place(relx=0.5, rely=0.05, anchor="center")

#Label descripción
label_descripcion = ctk.CTkLabel(master=conversor, text="Convierte entre grados celcius, Fahrenheit y Kelvin.", font=("Segoe UI", 15), wraplength=250, anchor="nw", justify="left")
label_descripcion.place(relx=0.1, rely=0.1)

#Label, combobox y entrada temperatura - desde.
label_temperatura_desde = ctk.CTkLabel(master=conversor, text="Desde", font=("Segoe UI", 15))
label_temperatura_desde.place(relx=0.5, rely=0.25, anchor="center")

combobox_temperatura_desde = ctk.CTkComboBox(master=conversor, values=magnitudes, font=("Segoe UI", 15))
combobox_temperatura_desde.place(relx=0.5, rely=0.3, anchor="center")

entry_temperatura_desde = ctk.CTkEntry(master=conversor, placeholder_text="Ingresa el valor", font=("Segoe UI", 15))
entry_temperatura_desde.place(relx=0.5, rely=0.4, anchor="center")


#label, combobox, boton y resultado temperatura - hacia.
label_temperatura_hacia = ctk.CTkLabel(master=conversor, text="Hacia", font=("Segoe UI", 15))
label_temperatura_hacia.place(relx=0.5, rely=0.5, anchor="center")

combobox_temperatura_hacia = ctk.CTkComboBox(master=conversor, values=magnitudes, font=("Segoe UI", 15))
combobox_temperatura_hacia.place(relx=0.5, rely=0.55, anchor="center")

button_convertir = ctk.CTkButton(master=conversor, text="Convertir", command=conversion_temperatura)
button_convertir.place(relx=0.5, rely=0.7, anchor="center")

label_resultado = ctk.CTkEntry(master=conversor, width=350, height=20, state='readonly', font=("Segoe UI", 15))
label_resultado.place(relx=0.5, rely=0.85, anchor="center")

conversor.mainloop()