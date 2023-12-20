import win32print

def imprimir_en_impresora(datos, nombre_impresora='NombreDeTuImpresora'):
    try:
        printer = win32print.OpenPrinter(nombre_impresora)
        win32print.StartDocPrinter(printer, 1, ('documento.txt', None, 'RAW'))
        win32print.WritePrinter(printer, datos.encode('utf-8'))
        win32print.EndDocPrinter(printer)
        win32print.ClosePrinter(printer)
        print("Imprimiendo en", nombre_impresora)
    except Exception as e:
        print("Error al imprimir:", e)

# Ejemplo de uso
datos_a_imprimir = "Hola, esta es la información que quiero imprimir."

imprimir_en_impresora(datos_a_imprimir)