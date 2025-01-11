import streamlit as st
import pickle
import numpy as np
from streamlit_extras.colored_header import colored_header
from streamlit_extras.button_selector import button_selector

def load_model(model_path):
    with open(model_path, 'rb') as file:
        return pickle.load(file)
def home():
    st.write("")
def kidney_pred(age,bp,sg,al,su,rbc,pc,pcc,ba,bgr,bu,sc,sod,pot,hemo,pcv,wc,rc,htn,dm,cad,appet,pe,ane):
    ipk=np.array([[float(age),float(bp),float(sg),float(al),float(su),(rbc),(pc),(pcc),(ba),float(bgr),float(bu),float(sc),float(sod),
                  float(pot),float(hemo),float(pcv),float(wc),float(rc),float(htn),float(dm),float(cad),float(appet),float(pe),float(ane)]])
    resultk = load_model("E:\Project1\project2\kidney.pkl").predict(ipk)
    return resultk

def parkinsons_pred(MDVP_Fo	,MDVP_Fhi,MDVP_Flo,MDVP_Jitter,MDVP_jitter_Abs,MDVP_RAP,MDVP_PPQ,Jitter_DDP,MDVP_Shimmer,MDVP_Shimmer_db,
                    Shimmer_APQ3,Shimmer_APQ5,MDVP_APQ,Shimmer_DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE):
    ipp=np.array([[float(MDVP_Fo),float(MDVP_Fhi),float(MDVP_Flo),float(MDVP_Jitter),float(MDVP_jitter_Abs),float(MDVP_RAP),float(MDVP_PPQ),
                   float(Jitter_DDP),float(MDVP_Shimmer),float(MDVP_Shimmer_db),float(Shimmer_APQ3),float(Shimmer_APQ5),float(MDVP_APQ),float(Shimmer_DDA),
                   float(NHR),float(HNR),float(RPDE),float(DFA),float(spread1),float(spread2),float(D2),float(PPE)]])
    resultp=load_model("E:\Project1\project2\parkinsons.pkl").predict(ipp)
    return resultp
def liver_pred(Age,Gender,Total_Bilirubin,Direct_Bilirubin,Alkaline_Phosphotase,Alamine_Aminotransferase,Aspartate_Aminotransferase,Total_Protiens,Albumin,
          Albumin_and_Globulin_Ratio):
    ipl=np.array([[float(Age),float(Gender),float(Total_Bilirubin),float(Direct_Bilirubin),int(Alkaline_Phosphotase),float(Alamine_Aminotransferase),
                   float(Aspartate_Aminotransferase),float(Total_Protiens),float(Albumin),float(Albumin_and_Globulin_Ratio)]])
    resultl=load_model("E:\Project1\project2\liver.pkl").predict(ipl)
    return resultl
def kidney():
    try:
        st.title("Kidney disease prediction")
        age=st.text_input("Age")
        bp=st.text_input("Blood pressure")
        sg=st.text_input("Specific gravity")
        al=st.text_input("Albumin")
        su=st.text_input("Sugar")
        rbc=st.selectbox("Red blood cell",("Normal","Abnormal"))
        rbc_map={"Normal":1,"Abnormal":0}
        rbc_act=rbc_map[rbc]
        pc=st.selectbox("Pus cell",("Normal","Abnormal"))
        pc_map={"Normal":1,"Abnormal":0}
        pc_act=pc_map[pc]
        pcc=st.selectbox("Pus cell clumps",("Present","Not present"))
        pcc_map={"Present":1,"Not present":0}
        pcc_act=pcc_map[pcc]
        ba=st.selectbox("Bacteria",("Present","Not present"))
        ba_map={"Present":1,"Not present":0}
        ba_act=ba_map[ba]
        bgr=st.text_input("Blood glucose random")
        bu=st.text_input("Blood urea")
        sc=st.text_input("serum creatinine")
        sod=st.text_input("Sodium")
        pot=st.text_input("Potassium")
        hemo=st.text_input("Hemoglobin")
        pcv=st.text_input("Packed cell volume")
        wc=st.text_input("White blood cell count")
        rc=st.text_input("Red blood cell count")
        htn=st.selectbox("Hypertension",("Yes","No"))
        htn_map={"Yes":1,"No":0}
        htn_act=htn_map[htn]
        dm=st.selectbox("Diabetes mellitus",("Yes","No"))
        dm_map={"Yes":1,"No":0}
        dm_act=dm_map[dm]
        cad=st.selectbox("Coronary artery disease",("Yes","No"))
        cad_map={"Yes":1,"No":0}
        cad_act=cad_map[cad]
        appet=st.selectbox("Appetite",("Good","Bad"))
        appet_map={"Bad":1,"Good":0}
        appet_act=appet_map[appet]
        pe=st.selectbox("Pedal edema",("Yes","No"))
        pe_map={"Yes":1,"No":0}
        pe_act=pe_map[pe]
        ane=st.selectbox("Anemia",("Yes","No"))
        ane_map={"Yes":1,"No":0}
        ane_act=ane_map[ane]
        if st.button("Predict"):
            op= kidney_pred(age,bp,sg,al,su,rbc_act,pc_act,pcc_act,ba_act,bgr,bu,sc,sod,pot,hemo,pcv,wc,rc,htn_act,dm_act,cad_act,appet_act,pe_act,ane_act)
            if op==1:
                st.markdown("""
            <div style="background-color: #d4edda; color: #155724; padding: 20px; border-radius: 10px;">
                <h2>✅ You are healthy!</h2>
                <p>Keep maintaining a healthy lifestyle and regular check-ups.</p>
            </div>
        """, unsafe_allow_html=True)
            else:
                st.markdown("""
            <div style="background-color: #f8d7da; color: #721c24; padding: 20px; border-radius: 10px;">
                <h2>⚠️ You might have kidney disease</h2>
                <p>Please consult a doctor immediately for further diagnosis and treatment.</p>
            </div>
        """, unsafe_allow_html=True)  
    except ValueError or TypeError:
        st.error("Please enter valid data")
def parkinsons():
    try:
        st.title("Parkinsons disease prdiction")
        MDVP_Fo=st.text_input("MDVP:Fo(Hz)")
        MDVP_Fhi=st.text_input("MDVP:Fhi(Hz)")
        MDVP_Flo=st.text_input("MDVP:Flo(Hz)")
        MDVP_Jitter=st.text_input("MDVP:Jitter(%)")
        MDVP_jitter_Abs=st.text_input("MDVP:Jitter(Abs)")
        MDVP_RAP=st.text_input("MDVP:RAP")
        MDVP_PPQ=st.text_input("MDVP:PPQ")
        Jitter_DDP=st.text_input("Jitter:DDP")
        MDVP_Shimmer=st.text_input("MDVP:Shimmer")
        MDVP_Shimmer_db=st.text_input("MDVP:Shimmer(dB)")
        Shimmer_APQ3=st.text_input("Shimmer:APQ3")
        Shimmer_APQ5=st.text_input("Shimmer:APQ5")
        MDVP_APQ=st.text_input("MDVP:APQ")
        Shimmer_DDA=st.text_input("Shimmer:DDA")
        NHR=st.text_input("NHR")
        HNR=st.text_input("HNR")
        RPDE=st.text_input("RPDE")
        DFA=st.text_input("DFA")
        spread1=st.text_input("spread1")
        spread2=st.text_input("spread2")
        D2=st.text_input("D2")
        PPE=st.text_input("PPE")
        if st.button("Predict"):
            op=parkinsons_pred(MDVP_Fo,MDVP_Fhi,MDVP_Flo,MDVP_Jitter,MDVP_jitter_Abs,MDVP_RAP,MDVP_PPQ,Jitter_DDP,MDVP_Shimmer,MDVP_Shimmer_db,
                        Shimmer_APQ3,Shimmer_APQ5,MDVP_APQ,Shimmer_DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE)
            if op==1:
                st.markdown("""
            <div style="background-color: #f8d7da; color: #721c24; padding: 20px; border-radius: 10px;">
                <h2>⚠️ You might have parkinsons disease</h2>
                <p>Please consult a doctor immediately for further diagnosis and treatment.</p>
            </div>
        """, unsafe_allow_html=True)       
            else:
                st.markdown("""
            <div style="background-color: #d4edda; color: #155724; padding: 20px; border-radius: 10px;">
                <h2>✅ You are healthy!</h2>
                <p>Keep maintaining a healthy lifestyle and regular check-ups.</p>
            </div>
        """, unsafe_allow_html=True)
    except ValueError or TypeError:
        st.error("Please enter valid data")
def liver():
    try:
        st.title("Liver Disease")
        Age=st.text_input("Age")
        Gender = st.selectbox("Gender",("Male","Female"))
        Gender_map={"Male":1,"Female":0}
        Gender_act=Gender_map[Gender]
        Total_Bilirubin=st.text_input("Total_Bilirubin")
        Direct_Bilirubin=st.text_input("Direct_Bilirubin")
        Alkaline_Phosphotase=st.text_input("Alkaline_Phosphotase")
        Alamine_Aminotransferase=st.text_input("Alamine_Aminotransferase")
        Aspartate_Aminotransferase=st.text_input("Aspartate_Aminotransferase")
        Total_Protiens	=st.text_input("Total_Protiens")
        Albumin=st.text_input("Albumin")
        Albumin_and_Globulin_Ratio=st.text_input("Albumin_and_Globulin_Ratio")	


        if st.button("Predict"):
            op=liver_pred(Age,Gender_act,Total_Bilirubin,Direct_Bilirubin,Alkaline_Phosphotase,Alamine_Aminotransferase,Aspartate_Aminotransferase,
                          Total_Protiens,Albumin,Albumin_and_Globulin_Ratio)
            if op==1:    
                st.markdown("""
            <div style="background-color: #f8d7da; color: #721c24; padding: 20px; border-radius: 10px;">
                <h2>⚠️ You might have liver disease</h2>
                <p>Please consult a doctor immediately for further diagnosis and treatment.</p>
            </div>
        """, unsafe_allow_html=True)
            else:
                st.markdown("""
            <div style="background-color: #d4edda; color: #155724; padding: 20px; border-radius: 10px;">
                <h2>✅ You are healthy!</h2>
                <p>Keep maintaining a healthy lifestyle and regular check-ups.</p>
            </div>
        """, unsafe_allow_html=True)
    except ValueError or TypeError:
        st.error("Please enter valid data")

css = """
<style>
.stApp {
    background-image: url("https://png.pngtree.com/thumb_back/fh260/background/20210923/pngtree-health-care-gradient-blue-theme-light-effect-background-image_904155.png");
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
    font-family: 'Arial', sans-serif;
    color:Black; /* set color to black */
}
</style>
"""
st.markdown(css, unsafe_allow_html=True)

# Home Page Content
st.title("Welcome to Health Prediction System 🩺")
st.markdown("""
This application helps you predict the likelihood of having specific health conditions using machine learning models. 
Select a disease from the options below to proceed with the prediction.
""")

# Features Overview
colored_header(
    label="Features of the Application",
    description="",
    color_name="violet-70"
)

st.markdown("""
- **Chronic Kidney Disease Prediction**: Input your health parameters to check if you're at risk of kidney disease.
- **Parkinson’s Disease Prediction**: Assess the likelihood of Parkinson's disease based on specific medical metrics.
- **Liver Disease Prediction**: Analyze your liver health through key indicators.
""")

# Instructions for Users
st.markdown("""
### How to Use:
1. Select a disease from the options below.
2. Fill in the required health parameters.
3. Click the "Predict" button to get your result.
""")

# Button Selector for Navigation
from streamlit_extras.button_selector import button_selector

selected_option = button_selector(
    options=["Chronic Kidney Disease", "Parkinson's Disease", "Liver Disease"],
    key="home_selector",
    spec=3
)

# Navigate to the selected page
if selected_option == 0:
    kidney()
elif selected_option == 1:
    parkinsons()
elif selected_option == 2:
    liver()
