import pandas as pd 
import streamlit as st
import joblib
import sklearn


Model = joblib.load('dCTM.h5')

def Predict(online_order, book_table, location, rest_type, cuisines,
       listed_in_type, listed_in_city , approx_cost_for_two_people , votes):
    
    
    test = pd.DataFrame(data = {'online_order' : [online_order], 'book_table' : [book_table],
                                'location' : [location], 'rest_type' : [rest_type], 'cuisines' : [cuisines],
       'listed_in(type)' : [listed_in_type], 'listed_in(city)' : [listed_in_city] ,
                                'approx_cost(for two people)' : approx_cost_for_two_people , 
                               'votes' : [votes]})
    
    return Model.predict(test)[0]


def main():
    st.header('ZOMATO RESTAURANT CLASSIFIER APP'.capitalize())
    
    online_order = st.selectbox('is there is online orders'.title() ,['Yes' ,'No'] )
    
    
    book_table = st.selectbox('is there is book table'.title() , ['Yes', 'No'])
    
    
    location = st.selectbox('choose location'.title() ,
                                    ['Other', 'Jayanagar', 'JP Nagar', 'Bannerghatta Road' ,'BTM',
                                         'Koramangala 5th Block', 'HSR', 'Marathahalli', 'Koramangala 7th Block',
                                         'Bellandur', 'Whitefield', 'Indiranagar', 'Brigade Road',
                                         'Koramangala 6th Block'])
    
    
    rest_type = st.selectbox('what is rest type'.title() ,
                                   ['Casual Dining', 'Other', 'Quick Bites', 'Cafe', 'Delivery', 'Dessert Parlor',
                                     'Takeaway, Delivery', 'Casual Dining, Bar'])
    
    
    cuisines = st.selectbox('what is cuisines'.title() , ['Other', 'North Indian', 'Cafe', 'Bakery, Desserts', 'Biryani', 'South Indian'
                                         'North Indian, Chinese', 'Ice Cream, Desserts', 'Chinese', 'Bakery'
                                         'Fast Food', 'Mithai, Street Food', 'Desserts',
                                         'South Indian, North Indian, Chinese', 'Chinese, North Indian'])
    
    
    listed_in_type = st.selectbox('what is your listed in type'.title() 
                                       , ['Buffet', 'Cafes', 'Delivery', 'Desserts', 'Dine-out', 'Drinks & nightlife',
                                                 'Pubs and bars'])
    
    listed_in_city = st.selectbox('what is listed in city'.title() ,['Other' ,'Bannerghatta Road' ,'Basavanagudi',
                                                                     'Brigade Road' ,'Brookefield',
                                     'BTM', 'Church Street', 'HSR', 'Indiranagar', 'Jayanagar', 'JP Nagar',
                                     'Kalyan Nagar', 'Kammanahalli' ,'Koramangala 4th Block',
                                     'Koramangala 5th Block', 'Koramangala 6th Block', 'Koramangala 7th Block',
                                     'Lavelle Road', 'Marathahalli', 'MG Road', 'Old Airport Road',
                                     'Residency Road', 'Sarjapur Road', 'Whitefield'])
    
    approx_cost_for_two_people = st.slider('what is approx cost for two people',  min_value=40.0 , max_value=6000.0,
                                          value=60.0 , step=10.0)
    
    
    votes = st.slider('what is approx cost for two people',  min_value=0 , max_value=6832,
                                          value=100 , step=10)#16832
    
    
    
    if st.button('predict'.title()):
        ans = Predict(online_order, book_table, location, rest_type, cuisines,
                       listed_in_type, listed_in_city , approx_cost_for_two_people , votes)
        st.write(ans)
main()
