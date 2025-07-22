
import streamlit as st

st.set_page_config(page_title="Controller Fénix", layout="centered")
st.title("🤖 Controller Fénix Automotriz")
st.write("Hola 👋 Soy tu controller financiero personal. Pregúntame sobre facturación, costos o clientes del 2025.")

pregunta = st.text_input("💬 Escribe tu pregunta aquí")

if pregunta:
    pregunta = pregunta.lower()

    if "facturación" in pregunta:
        st.success("💰 La facturación acumulada en 2025 es de $76.563.813 CLP.")

    elif "materiales" in pregunta or "pintura" in pregunta:
        st.success("🎨 Los materiales y pintura representan el 29.02% de las ventas en 2025.")

    elif "financiero" in pregunta:
        st.success("📉 El costo financiero representa el 4.58% de las ventas en 2025.")

    elif "cliente" in pregunta:
        st.success("👥 Último trimestre por tipo de cliente:\n- Particular: $19.039.407\n- Seguro: $20.053.234")

    elif "vehículo" in pregunta or "vehiculo" in pregunta:
        st.success("🚗 Último trimestre por tipo de vehículo:\n- Liviano: $11.706.036\n- Pesado: $27.386.605")

    else:
        st.warning("🤔 No entendí tu pregunta. Prueba con: 'Facturación 2025', '% materiales', 'clientes'.")
