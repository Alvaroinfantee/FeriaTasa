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

def main():
    st.title("Consulta de Tasas de Interés")

    # Elección del tipo de tabla
    tabla_tipo = st.radio(
        "Selecciona el tipo de cliente:",
        ("Clientes estándar", "Clientes hasta $400,000 y hasta 600 puntos")
    )

    if tabla_tipo == "Clientes estándar":
        data = create_dataframe(rates_data_default)
    else:
        data = create_dataframe(rates_data_high_risk)

    # Mostrar tabla
    st.subheader(f"Tabla de tasas: {tabla_tipo}")
    st.dataframe(data)

    # Búsqueda interactiva
    año_seleccionado = st.selectbox("Selecciona el año para consultar:", data["Año"].unique())

    if año_seleccionado:
        fila = data[data["Año"] == año_seleccionado]
        st.write(f"### Tasas para {año_seleccionado}")
        st.write(f"Tasa fija hasta 6 meses: {fila['TASA FIJA HASTA 6 MESES'].values[0]}%")
        st.write(f"Tasa fija hasta 2 años: {fila['TASA FIJA HASTA 2 AÑOS'].values[0]}%")
        st.write(f"Tasa fija hasta 3 años: {fila['TASA FIJA HASTA 3 AÑOS'].values[0]}%")
        st.write(f"Plazo máximo: {fila['Plazo Máximo'].values[0]} meses")
        st.write(f"Porcentaje de referencia tasación: {fila['Porcentaje de Referencia Tasación'].values[0]}%")

if __name__ == "__main__":
    main()

