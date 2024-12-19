import pickle
import streamlit as st



# Sarlavha va kirish matni
st.title("🩺 Diabet Tashxislash Dasturi")
st.write("""
Ushbu dastur diabet tashxisini bashorat qilish uchun ishlatiladi. Ma'lumotlaringizni kiriting va natijani ko'ring.
""")

# Foydalanuvchi kiritmalari uchun qatorlar
st.sidebar.header("Ma'lumotlaringizni kiriting")
pregnancies = st.sidebar.number_input("Homiladorliklar soni", min_value=0, max_value=20, step=1, value=0)
glucose = st.sidebar.number_input("Qondagi glyukoza miqdori (mg/dL)", min_value=0, max_value=300, step=1, value=120)
blood_pressure = st.sidebar.number_input("Qon bosimi (mm Hg)", min_value=0, max_value=200, step=1, value=80)
skin_thickness = st.sidebar.number_input("Terining qalinligi (mm)", min_value=0, max_value=100, step=1, value=20)
insulin = st.sidebar.number_input("Insulin darajasi (IU/mL)", min_value=0, max_value=900, step=1, value=30)
bmi = st.sidebar.number_input("BMI (Tana massasi indeksi)", min_value=0.0, max_value=100.0, step=0.1, value=25.0)
dpf = st.sidebar.number_input("Diabetes Pedigree Function (DPF)", min_value=0.0, max_value=5.0, step=0.001, value=0.5)
age = st.sidebar.number_input("Yosh", min_value=0, max_value=150, step=1, value=30)

# Modelni yuklash
with open('diabetes_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Foydalanuvchi ma'lumotlari asosida natija chiqarish
if st.button("Natijani ko'rish 🩺"):
    input_data = [[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age]]
    prediction = model.predict(input_data)[0]
    
    if prediction == 1:
        st.error("❌ Natija: Diabetga chalinish ehtimoli mavjud.")
    else:
        st.success("✅ Natija: Diabetga chalinish ehtimoli yo'q.")

