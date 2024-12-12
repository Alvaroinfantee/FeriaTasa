import streamlit as st

# Datos
rates_data = {
    "2023-2025": [15.49, 18.24, 21.49, 60, 75],
    "2022": [15.74, 18.24, 21.49, 60, 75],
    "2021": [15.94, 18.44, 22.74, 60, 75],
    "2020": [15.94, 18.44, 22.74, 60, 75],
    "2019": [16.24, 18.74, 22.74, 60, 75],
    "2018": [16.49, 18.99, 22.99, 60, 75],
    "2017": [16.74, 19.24, 23.24, 60, 75],
    "2016": [16.94, 19.24, 23.24, 60, 75],
    "2015": [18.49, 20.49, 24.49, 60, 75],
    "2014": [20.74, 22.74, 26.74, 60, 75],
    "2013": [20.74, 22.74, 26.74, 48, 70],
    "2010-2012": [21.24, 23.24, 27.24, 42, 70],
    "2004-2009": [23.24, 25.24, 29.24, 42, 65],
}

# Título de la aplicación
st.title("Calculadora de Tasas de Interés")

# Selección de año
año = st.selectbox("Selecciona el año:", options=list(rates_data.keys()))

# Selección del plazo
plazo = st.selectbox(
    "Selecciona el plazo fijo:",
    options=["6 meses", "2 años", "3 años"],
    index=0,
)

# Mapeo de plazos a índices
plazo_map = {"6 meses": 0, "2 años": 1, "3 años": 2}
plazo_index = plazo_map[plazo]

# Mostrar datos de referencia
st.subheader("Detalles de Referencia:")
tasa_seleccionada = rates_data[año][plazo_index]
plazo_maximo = rates_data[año][3]
porcentaje_tasacion = rates_data[año][4]

st.write(f"**Tasa fija seleccionada:** {tasa_seleccionada:.2f}%")
st.write(f"**Plazo máximo:** {plazo_maximo} meses")
st.write(f"**Porcentaje de referencia tasación:** {porcentaje_tasacion}%")

# Entrada de monto
monto = st.number_input("Ingresa el monto del préstamo:", min_value=0.0, step=1000.0)

# Cálculo de la cuota mensual
if monto > 0:
    tasa_mensual = tasa_seleccionada / 100 / 12
    cuota_mensual = monto * (tasa_mensual * (1 + tasa_mensual) ** plazo_maximo) / (
        (1 + tasa_mensual) ** plazo_maximo - 1
    )
    st.write(f"**Cuota mensual estimada:** {cuota_mensual:.2f}")
