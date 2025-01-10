import time
import streamlit as st
import sklearn
import pickle
import numpy as np
from numpy import dtype
from altair.theme import options

modelk=pickle.load(open("E:\Project1\kidney.pkl","rb"))
modelp=pickle.load(open("E:\Project1\parkinsons.pkl","rb"))
modell=pickle.load(open("E:\Project1\liver.pkl","rb"))
def BMI_page():
    st.subheader("But first, let's find your BMI")
    weight = st.number_input("Enter your weight (kg)", min_value=0.0)  
    height = st.number_input("Enter your height (m)", min_value=0.0)
    if st.button("Calculate BMI"):
        if weight > 0 and height > 0:  
            result = weight / (height ** 2)
            st.write(f"Your BMI is: {result:.2f}") 
        else:
            st.write("Please enter valid weight and height.") 

st.title("Predict Your Health Condition")
home=st.sidebar.radio("********Select which disease to predict********",("Chronic kidney disease"))
def kidney_pred(age,bp,sg,al,su,rbc,pc,pcc,ba,bgr,bu,sc,sod,pot,hemo,pcv,wc,rc,htn,dm,cad,appet,pe,ane):
    ipk=np.array([[float(age),float(bp),float(sg),float(al),float(su),(rbc),(pc),(pcc),(ba),float(bgr),float(bu),float(sc),float(sod),
                  float(pot),float(hemo),float(pcv),float(wc),float(rc),(htn),(dm),(cad),(appet),(pe),(ane)]])
    resultk = modelk.predict(ipk)
    return resultk

def parkinsons_pred(MDVP_Fo	,MDVP_Fhi,MDVP_Flo,MDVP_Jitter,MDVP_jitter_Abs,MDVP_RAP,MDVP_PPQ,Jitter_DDP,MDVP_Shimmer,MDVP_Shimmer_db,
                    Shimmer_APQ3,Shimmer_APQ5,MDVP_APQ,Shimmer_DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE):
    ipp=np.array([[float(MDVP_Fo),float(MDVP_Fhi),float(MDVP_Flo),float(MDVP_Jitter),float(MDVP_jitter_Abs),float(MDVP_RAP),float(MDVP_PPQ),
                   float(Jitter_DDP),float(MDVP_Shimmer),float(MDVP_Shimmer_db),float(Shimmer_APQ3),float(Shimmer_APQ5),float(MDVP_APQ),float(Shimmer_DDA),
                   float(NHR),float(HNR),float(RPDE),float(DFA),float(spread1),float(spread2),float(D2),float(PPE)]])
    resultp=modelp.predict(ipp)
    return resultp
def liver_pred(Age,Gender,Total_Bilirubin,Direct_Bilirubin,Alkaline_Phosphotase,Alamine_Aminotransferase,Aspartate_Aminotransferase,Total_Protiens,Albumin,
          Albumin_and_Globulin_Ratio):
    ipl=np.array([[int(Age),(Gender),float(Total_Bilirubin),float(Direct_Bilirubin),int(Alkaline_Phosphotase),int(Alamine_Aminotransferase),
                   int(Aspartate_Aminotransferase),float(Total_Protiens),float(Albumin),float(Albumin_and_Globulin_Ratio)]])
def kidney():
    st.title("Kidney disease prediction")
    age=st.text_input("Age")
    bp=st.number_input("Blood pressure")
    sg=(st.text_input("Specific gravity"))
    al=(st.text_input("Albumin"))
    su=st.number_input("Sugar")
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
    ba_act=ba_map[pcc]
    bgr=st.number_input("Blood glucose random")
    bu=st.number_input("Blood urea")
    sc=(st.text_input("serum creatinine"))
    sod=st.number_input("Sodium")
    pot=(st.text_input("Potassium"))
    hemo=(st.text_input("Hemoglobin"))
    pcv=st.number_input("Packed cell volume")
    wc=st.number_input("White blood cell count")
    rc=(st.text_input("Red blood cell count"))
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
            st.write("You dont have have kidney disease")
        else:
            st.write("You have kidney disease")
def parkinsons():
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
            st.write("You have Parkinsons disease")
        else:
            st.write("You are not affected by parkinsons disease")
def liver(Age,Gender,Total_Bilirubin,Direct_Bilirubin,Alkaline_Phosphotase,Alamine_Aminotransferase,Aspartate_Aminotransferase,Total_Protiens,
          Albumin,Albumin_and_Globulin_Ratio):
    st.title("Liver Disease")
    Age=st.number_input("Age")
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
            st.write("You might have liver disease")
        else:
            st.write("You might not have liver disease")
if home=="Chronic kidney disease":
    kidney()
elif home=="Parkinsons":
    parkinsons()
elif home=="Liver":
    liver()