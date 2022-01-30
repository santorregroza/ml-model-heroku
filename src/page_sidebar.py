import streamlit as st


def sidebar(ls_page_name):

    # Resources
    #image_spainai_url = ""
    edition = "Taller despliegue ML"
    title = "### Páginas"

    #st.sidebar.image(image_spainai_url)
    st.sidebar.write(edition)
    st.sidebar.write(title)
    page_name = st.sidebar.selectbox("", ls_page_name)

    return page_name
