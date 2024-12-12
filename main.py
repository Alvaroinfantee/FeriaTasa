import pandas as pd
import streamlit as st

# Datos de la tabla principal
rates_data_default = {
    "Año": ["2023-2025", "2022", "2021", "2020", "2019", "2018", "2017", "2016", "2015", "2014", "2013", "2010-2012", "2004-2009"],
    "TASA FIJA HASTA 6 MESES": [15.49, 15.74, 15.94, 15.94, 16.24, 16.49, 16.74, 16.94, 18.49, 20.74, 20.74, 21.24, 23.24],
    "TASA FIJA HASTA 2 AÑOS": [18.24, 18.24, 18.44, 18.44, 18.74, 18.99, 19.24, 19.24, 20.49, 22.74, 22.74, 23.24, 25.24],
    "TASA FIJA HASTA 3 AÑOS": [21.49, 21.49, 22.74, 22.74, 22.74, 22.99, 23.24, 23.24, 24.49, 26.74, 26.74, 27.24, 29.24],
    "Plazo Máximo": [60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 48, 42, 42],
    "Porcentaje de Referencia Tasación": [75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 70, 70, 65]
}

# Datos para clientes hasta $400,000 y hasta 600 puntos
rates_data_high_risk = {
    "Año": ["2023-2025", "2022", "2021", "2020", "2019", "2018", "2017", "2016", "2015", "2014", "2013", "2010-2012", "2004-2009"],
    "TASA FIJA HASTA 6 MESES": [16.99, 17.24, 17.44, 17.44, 17.74, 17.99, 18.24, 18.44, 19.99, 22.24, 22.24, 22.74, 24.74],
    "TASA FIJA HASTA 2 AÑOS": [18.24, 18.24, 18.44, 18.44, 18.74, 18.99, 19.24, 19.24, 20.49, 22.74, 22.74, 23.24, 25.24],
    "TASA FIJA HASTA 3 AÑOS": [21.49, 21.49, 22.74, 22.74, 22.74, 22.99, 23.24, 23.24, 24.49, 26.74, 26.74, 27.24, 29.24],
    "Plazo Máximo": [60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 48, 42, 42],
    "Porcentaje de Referencia Tasación": [75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 70, 70, 65]
}

# Conversión de datos a DataFrame
def create_dataframe(data):
    return pd.DataFrame(data)

def calcular_cuota_con_gracia(monto, tasa_anual, plazo, e, gracia):
    tasa_mensual = tasa_anual / 100 / 12
    interes = monto * tasa_mensual
    cuota = monto * (tasa_mensual * (1 + tasa_mensual) ** e) / ((1 + tasa_mensual) ** e - 1)

    if gracia == 0:
        monto_gracia = 0
    else:
        monto_gracia = (monto * tasa_mensual) / e

    cuotafinal = cuota + monto_gracia * gracia
    return cuotafinal

def main():
    st.title("Calculadora de Cuotas de Préstamo")

    # Elección del tipo de cliente
    tabla_tipo = st.radio(
        "Selecciona el tipo de cliente:",
        ("Clientes estándar", "Clientes hasta $400,000 y hasta 600 puntos")
    )

    if tabla_tipo == "Clientes estándar":
        data = create_dataframe(rates_data_default)
    else:
        data = create_dataframe(rates_data_high_risk)

    # Selección del año
    año_seleccionado = st.selectbox("Selecciona el año para consultar:", data["Año"].unique())

    if año_seleccionado:
        fila = data[data["Año"] == año_seleccionado]
        plazo_maximo = int(fila["Plazo Máximo"].values[0])

        # Entrada de datos
        monto = st.number_input("Ingresa el monto del préstamo:", min_value=0.0, step=1000.0)
        plazo_seleccionado = st.selectbox("Selecciona el plazo:", ["6 MESES", "2 AÑOS", "3 AÑOS"])
        e = st.number_input(f"Ingresa el plazo del préstamo en meses (máximo {plazo_maximo}):", min_value=1, max_value=plazo_maximo, step=1)
        gracia = st.selectbox("Selecciona el periodo de gracia en meses:", [0, 1, 2])

        # Mapear plazo a meses y columna correcta
        plazo_map = {"6 MESES": 6, "2 AÑOS": 24, "3 AÑOS": 36}
        columna_map = {"6 MESES": "TASA FIJA HASTA 6 MESES", "2 AÑOS": "TASA FIJA HASTA 2 AÑOS", "3 AÑOS": "TASA FIJA HASTA 3 AÑOS"}
        plazo = plazo_map[plazo_seleccionado]
        columna_tasa = columna_map[plazo_seleccionado]

        # Cálculo de la cuota
        if monto > 0:
            tasa_anual = fila[columna_tasa].values[0]
            cuota_final = calcular_cuota_con_gracia(monto, tasa_anual, plazo, e, gracia)
            st.write(f"### Tasa de Interés Anual: {tasa_anual:.2f}%")
            st.write(f"### Cuota mensual estimada con gracia: ${cuota_final:.2f}")

if __name__ == "__main__":
    main()
