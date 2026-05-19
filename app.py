import streamlit as st
from generator import generar_posts

# Configuración de la página
st.set_page_config(
    page_title="ContentFlow",
    page_icon="✍️",
    layout="centered"
)

# Título
st.title("✍️ ContentFlow")
st.subheader("Generador de contenido para redes sociales con IA")
st.divider()

# Formulario
tema = st.text_input(
    "¿Sobre qué querés generar contenido?",
    placeholder="Ej: beneficios del trabajo remoto, tips de productividad..."
)

col1, col2 = st.columns(2)

with col1:
    red_social = st.selectbox(
        "Red social",
        ["LinkedIn", "Twitter", "Instagram"]
    )

with col2:
    tono = st.selectbox(
        "Tono",
        ["Profesional", "Casual", "Divertido"]
    )

st.divider()

# Botón para generar
if st.button("🚀 Generar posts", use_container_width=True, type="primary"):
    if not tema:
        st.warning("Escribí un tema primero.")
    else:
        with st.spinner("Generando tus posts..."):
            resultado = generar_posts(tema, red_social, tono)

        st.success("¡Posts generados!")
        st.divider()

        # Separar y mostrar cada post
        posts = resultado.split("---")

for i, post in enumerate(posts):
    post = post.strip()
    # Elimina el "POST 1:", "POST 2:", etc. del inicio
    if post.upper().startswith(f"POST {i+1}:"):
        post = post[len(f"POST {i+1}:"):].strip()
    if post:
        st.markdown(f"#### Post {i+1}")
        st.text_area(
            label="",
            value=post,
            height=150,
            key=f"post_{i}"
        )
        st.divider()