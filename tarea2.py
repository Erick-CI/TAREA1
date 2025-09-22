import streamlit as st
import matplotlib.pyplot as plt

st.title("PA03")
st.subheader("Teoría de conjuntos, relaciones y funciones")

st.markdown("""
**Integrantes del grupo:**
- Juan Pérez  
- María López  
- Carlos Ramírez  
""")

# Caso práctico 01
st.header("Caso práctico 01 - Conjuntos")
lista1 = [1, 2, 3, 4, -4, -5, -6, 23, 25, 27, 100, 200, 240, 240]
lista2 = [-4, -5, -6, 300, 400, 600, 500, 500]

lista1 = list(set(lista1))
lista2 = list(set(lista2))

opcion1 = st.selectbox("Operaciones con listas:", 
    ["Cardinal 1", "Cardinal 2", "Unión", "Diferencia 1", "Diferencia 2", "Intersección"])

if opcion1 == "Cardinal 1":
    st.write("Cardinal de Lista1:", len(lista1))
elif opcion1 == "Cardinal 2":
    st.write("Cardinal de Lista2:", len(lista2))
elif opcion1 == "Unión":
    st.write("Unión:", list(set(lista1) | set(lista2)))
elif opcion1 == "Diferencia 1":
    st.write("Diferencia 1:", list(set(lista1) - set(lista2)))
elif opcion1 == "Diferencia 2":
    st.write("Diferencia 2:", list(set(lista2) - set(lista1)))
elif opcion1 == "Intersección":
    st.write("Intersección:", list(set(lista1) & set(lista2)))


# Caso práctico 02
st.header("Caso práctico 02 - Funciones")

opcion2 = st.selectbox("Funciones:", 
    ["Función de una variable", "Función de dos variables", "Función compuesta", "Gráfica"])

if opcion2 == "Función de una variable":
    x = st.number_input("Ingrese valor de x", value=0)
    f = lambda x: x**2 + 3
    st.write(f"f({x}) = {f(x)}")

elif opcion2 == "Función de dos variables":
    x = st.number_input("x", value=0)
    y = st.number_input("y", value=0)
    f = lambda x, y: x**2 + y**2
    st.write(f"f({x},{y}) = {f(x,y)}")

elif opcion2 == "Función compuesta":
    x = st.number_input("Ingrese valor de x", value=0)
    f = lambda x: 2*x + 1
    g = lambda x: x**2
    st.write(f"f(g({x})) = {f(g(x))}")

elif opcion2 == "Gráfica":
    f = lambda x: x**2 + 2
    x_vals = list(range(-10, 11))
    y_vals = [f(x) for x in x_vals]

    fig, ax = plt.subplots()
    ax.plot(x_vals, y_vals, marker="o")
    ax.set_title("f(x) = x^2 + 2")
    st.pyplot(fig)

