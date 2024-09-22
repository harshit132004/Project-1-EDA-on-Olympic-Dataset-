import streamlit as st 
import pandas as pd
from helpers import *

summer,Winter=data_preprocessor()

summer,Winter=duplicate_rows_remover(summer,Winter)

summer.dropna(subset=["region"] , inplace=True)
Winter.dropna(subset=["region"] , inplace=True)



st.sidebar.title("Menu")
season=st.sidebar.radio("Choose Season : ",("Summer","Winter"))
options=st.sidebar.radio("Options : ",("Medal Tally" ,"Country Wise","Year Wise","Year Wise Progress"))

#Medal Tally
if season== "Summer" and options=="Medal Tally":
    st.subheader("Summer Olympic Medal Tally")
    medal_pivot_summer=medal_tally_calculator(summer)
    medal_pivot_summer=medal_pivot_summer.sort_values(by=['Gold','Silver','Bronze'],ascending=False)
    st.dataframe( medal_pivot_summer,width=900)
    
elif season== "Winter" and options=="Medal Tally":
    st.subheader("Winter Olympic Medal Tally")
    medal_pivot_Winter=medal_tally_calculator(Winter)
    medal_pivot_Winter=medal_pivot_Winter.sort_values(by=['Gold','Silver','Bronze'],ascending=False)
    st.dataframe( medal_pivot_Winter,width=900)
        
    
#country wise
elif season== "Summer" and options=="Country Wise":
    st.subheader("Summer Countery-Wise Search")
    medal_pivot_summer=medal_tally_calculator(summer)
    noc=st.selectbox("Select Summer : ",medal_pivot_summer.index.tolist())
    details=country_wise_search(noc,medal_pivot_summer)
    table=pd.DataFrame.from_dict(details,orient="index",columns=["value"])
    st.dataframe(table)
    
elif season== "Winter" and options=="Country Wise":
    st.subheader("Winter Countery-Wise Search")
    medal_pivot_winter=medal_tally_calculator(Winter)
    noc=st.selectbox("Select Winter : ",medal_pivot_winter.index.tolist())
    details=country_wise_search(noc,medal_pivot_winter)
    table=pd.DataFrame.from_dict(details,orient="index",columns=["value"])
    st.dataframe(table)
    

#year wise
elif season== "Summer" and options=="Year Wise":
    st.subheader("Summer Year-Wise Search")
    
    years=sorted(summer["Year"].unique())
    select_year=st.selectbox("Select Year",years)
    
    countries=sorted(summer[summer["Year"]==select_year]['region'].unique())
    select_countries=st.selectbox("Select Countries",countries)
    
    plot_medals(select_year,select_countries,summer)
    
    
    
elif season== "Winter" and options=="Year Wise":
    st.subheader("Winter Year-Wise Search")
    
    years=sorted(Winter["Year"].unique())
    select_year=st.selectbox("Select Year",years)
    
    countries=sorted(Winter[Winter["Year"]==select_year]["region"].unique())
    select_countries=st.selectbox("Select Countries",countries)
    
    plot_medals(select_year,select_countries,Winter)
    
    
### YEAR WISE ANALYSIS

elif season=="Summer" and options=="Year-Wise Progress":
    st.subheader("OVERALL ANALYSIS OF A COUNTRY")

    countries = sorted(summer["region"].unique())
    selected_country = st.selectbox("Choose country : ",countries)

    year_analysis(selected_country,summer)

else:

    st.subheader("OVERALL ANALYSIS OF A COUNTRY")

    countries = sorted(Winter["region"].unique())
    selected_country = st.selectbox("Choose country : ",countries)

    year_analysis(selected_country,Winter)

    
