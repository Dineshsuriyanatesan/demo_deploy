# This is a sample Python script.
import pickle

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# import joblib
import streamlit as st

Area = ['Area_Albania','Area_Algeria','Area_Angola','Area_Argentina','Area_Armenia','Area_Australia','Area_Austria','Area_Azerbaijan','Area_Bahamas','Area_Bahrain','Area_Bangladesh','Area_Belarus','Area_Belgium','Area_Botswana','Area_Brazil','Area_Bulgaria','Area_Burkina Faso','Area_Burundi','Area_Cameroon','Area_Canada','Area_Central African Republic','Area_Chile','Area_Colombia','Area_Croatia','Area_Denmark','Area_Dominican Republic',
        'Area_Ecuador','Area_Egypt','Area_El Salvador','Area_Eritrea','Area_Estonia','Area_Finland','Area_France','Area_Germany','Area_Ghana','Area_Greece','Area_Guatemala','Area_Guinea','Area_Guyana','Area_Haiti','Area_Honduras','Area_Hungary','Area_India','Area_Indonesia','Area_Iraq','Area_Ireland','Area_Italy','Area_Jamaica','Area_Japan','Area_Kazakhstan','Area_Kenya','Area_Latvia','Area_Lebanon','Area_Lesotho','Area_Libya','Area_Lithuania',
        'Area_Madagascar','Area_Malawi','Area_Malaysia','Area_Mali','Area_Mauritania','Area_Mauritius','Area_Mexico','Area_Montenegro','Area_Morocco','Area_Mozambique','Area_Namibia','Area_Nepal','Area_Netherlands','Area_New Zealand','Area_Nicaragua','Area_Niger','Area_Norway','Area_Pakistan','Area_Papua New Guinea','Area_Peru','Area_Poland','Area_Portugal','Area_Qatar','Area_Romania','Area_Rwanda','Area_Saudi Arabia','Area_Senegal','Area_Slovenia',
        'Area_South Africa','Area_Spain','Area_Sri Lanka','Area_Sudan','Area_Suriname','Area_Sweden','Area_Switzerland','Area_Tajikistan','Area_Thailand','Area_Tunisia','Area_Turkey','Area_Uganda','Area_Ukraine','Area_United Kingdom','Area_Uruguay','Area_Zambia','Area_Zimbabwe']

Items = ['Item_Cassava','Item_Maize','Item_Plantains and others','Item_Potatoes','Item_Rice, paddy','Item_Sorghum','Item_Soybeans','Item_Sweet potatoes','Item_Wheat','Item_Yams',]

st.title("Crop Yield Regression")
rain = st.text_input(label = "Average Rainfall :")
presti = st.text_input(label = "Pesticides Used (In tonnes) :")
tempearture = st.text_input(label = "Temp in Year(Avg.) :")
area = st.selectbox(label = "Choose an Area :",options = Area,index = 0,placeholder = "Select the Area")
item = st.selectbox(label = "Choose an Item :",options = Items,placeholder = "Select the Item")

cols = st.columns(7)

with cols[3]:
    st.write("---")
    sub = st.button("SUBMIT")

area_array = [0 for _ in range(len(Area))]
items_array = [0 for _ in range(len(Items))]
# st.write(area_array)
# st.write(len(area_array))
model = pickle.load(open(file = 'model.pkl',mode = "rb"))
# model = joblib.load('model.sav')
if sub:
    if rain and presti and tempearture and area and item:
        rain = float(rain)
        presti = float(presti)
        tempearture = float(tempearture)
        area_array[Area.index(area)]+=1
        items_array[Items.index(item)]+=1

        # st.write(area_array)
        # st.write(items_array)
        test = [rain,presti,tempearture]
        test.extend(area_array)
        test.extend(items_array)
        # st.write(len(test))
        st.write(model.predict([test])[0])

    else:
        st.warning("Please fill all the fields above.")