import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from streamlit_option_menu import option_menu
pd.set_option('display.max_columns', None)
from PIL import Image
import base64

#setting page configuration

img=Image.open("C://Users//JAYAKAVI//Downloads//download (1).png")
st.set_page_config(page_title="Zomato", 
                    page_icon=img, 
                    layout="wide",
                    initial_sidebar_state="auto") 

# page header transparent color
page_background_color = """
<style>

[data-testid="stHeader"] 
{
background: rgba(0,0,0,0);
}

</style>
"""
st.markdown(page_background_color, unsafe_allow_html=True)

# title and position
st.markdown(f'<h1 style="text-align: center; color: red">Zomato Data Analysis and Visualization</h1>',
            unsafe_allow_html=True)
# Add colored divider
st.markdown(
    """<div style="height: 2px; background-color:teal; margin: 20px 0;"></div>""",
    unsafe_allow_html=True)

def dataframe():
    df=pd.read_csv("C:/Users/JAYAKAVI/New folder/zomato.csv")
    df1= pd.read_excel("https://github.com/nethajinirmal13/Training-datasets/raw/main/zomato/Country-Code.xlsx")
    
    # convert 1 Indian Rupee (INR) to the currency of multiple countries
    exchange_rates_data = {

        'Currency': ['Botswana Pula(P)', 'Brazilian Real(R$)', 'Dollar($)', 'Emirati Diram(AED)', 'Indian Rupees(Rs.)',
                    'Indonesian Rupiah(IDR)', 'NewZealand($)', 'Pounds(專)', 'Qatari Rial(QR)', 'Rand(R)', 
                    'Sri Lankan Rupee(LKR)', 'Turkish Lira(TL)'],
        'Exchange Rate (1 INR to X Currency)': [0.048, 0.058, 0.014, 0.052, 1.0, 0.0014, 0.017, 0.011, 0.051, 0.071, 0.23, 0.12]
    }

    # Create DataFrame from exchange rate data
    exchange_rates_df = pd.DataFrame(exchange_rates_data)
    
    df2=pd.merge(df,exchange_rates_df,on='Currency')
    
    #Let us merge both the datasets. This will help us to understand the dataset country wise.
    df4= pd.merge(df2,df1,on='Country Code',how='left')

    df5=pd.read_csv("C:/Users/JAYAKAVI/New folder/zo_file.csv")
    df5.drop('Unnamed: 0', inplace=True, axis=1)
    
    return df5

df3= dataframe()

# CREATING OPTION MENU
selected = option_menu(None,  ["Home", "Data Visualization", "Insights"],
                       icons=["house", "bar-chart","Magnifying Glass"],
                       default_index=0,
                       orientation="horizontal",
                       styles={"nav-link": {"font-size": "20px", "text-align": "centre", "margin": "-3px",
                                            "--hover-color": "#545454"},
                               "icon": {"font-size": "20px"},
                               "container": {"max-width": "3000px"},
                               "nav-link-selected": {"background-color": "violet"}})

if selected=='Home':

    col1,col2=st.columns([2,4],gap='medium')   

    with col1:
        
        file_ = open("C:/Users/JAYAKAVI/Downloads/967f19111202195.5ffdfc0e915cb.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()

        st.markdown(
            f'<img src="data:image/gif;base64,{data_url}"  width="320" height="200" alt="cat gif">',
            unsafe_allow_html=True,
        )

    with col2:
        st.subheader(':orange[Zomato]')
        st.markdown('####  Zomato is an Indian multinational company that aggregates restaurants and delivers food. It was founded in 2008 by Deepinder Goyal and Pankaj Chaddah as Foodiebay,and was later renamed Zomato in 2010. Zomato provides information on restaurant menus, prices, locations, user reviews, and ratings. It also offers online ordering and delivery services.')

  
    st.subheader(':orange[Technologies] : Python scripting, Pandas and Plotly ')

if selected=='Data Visualization':
    with st.sidebar:
        select = option_menu(None, ["currency","Country","City Analysis","City comparision","Top Charts"], 
                            default_index=0,
                            orientation="horizontal",
                            styles={"nav-link": {"font-size": "20px", "text-align": "centre", "margin": "0px", 
                                                    "--hover-color": "white"},
                                    "icon": {"font-size": "15px"},
                                    "container" : {"max-width": "3000px"},
                                    "nav-link-selected": {"background-color": "violet"}})
        
    if select=='currency':

        # convert 1 Indian Rupee (INR) to the currency of multiple countries
        exchange_rates_data = {

            'Currency': ['Botswana Pula(P)', 'Brazilian Real(R$)', 'Dollar($)', 'Emirati Diram(AED)', 'Indian Rupees(Rs.)',
                        'Indonesian Rupiah(IDR)', 'NewZealand($)', 'Pounds(專)', 'Qatari Rial(QR)', 'Rand(R)', 
                        'Sri Lankan Rupee(LKR)', 'Turkish Lira(TL)'],
            'Exchange Rate (1 INR to X Currency)': [0.048, 0.058, 0.014, 0.052, 1.0, 0.0014, 0.017, 0.011, 0.051, 0.071, 0.23, 0.12]
        }

        # Create DataFrame from exchange rate data
        exchange_rates_df = pd.DataFrame(exchange_rates_data)

        # compares indian currency with other country’s currency
        fig = px.bar(exchange_rates_df, x='Currency', y='Exchange Rate (1 INR to X Currency)',color='Currency',
                    labels={'Exchange Rate (1 INR to X Currency)': 'Exchange Rate (1 INR to X Currency)'},width=800,height=500,
                    title='Comparison of Indian Currency with Other Countries\' Currencies')
        fig.update_layout(yaxis_title='Exchange Rate (1 INR to X Currency)',title_font_color='orange',title_font=dict(size=20),title_x=0.1)
        fig.update_traces(dict(marker_line_width=0))
        st.plotly_chart(fig)
    
    if select=='Country':
        
        selected_country = st.selectbox('Select Country', df3['Country'].unique())

            
        # Chart 1: Distribution of Ratings
        
        fig_1= px.histogram(df3[df3['Country'] ==selected_country], x='Aggregate rating',color='Aggregate rating',width=700,height=500,
                            title='Distribution of Restaurant Ratings')
        fig_1.update_layout(title_font_color='orange',title_font=dict(size=20),title_x=0.3)
        fig_1.update_traces(showlegend=False)
        st.plotly_chart(fig_1)

        # chart2: Most Costly Cuisines 
        
        country_data = df3[df3['Country'] ==selected_country ]

        cuisine_counts = country_data['Cuisines'].str.split(', ', expand=True).stack().value_counts()
        top_cuisines = cuisine_counts.head(10)
        fig_2 = px.pie(names=top_cuisines.index, values=top_cuisines.values, 
                    title=f'Top 10 Favorite Cuisines in {selected_country}',color_discrete_sequence=px.colors.sequential.Oryel_r,
                    labels={'x': 'Cuisine', 'y': 'Number of Restaurants'})
        fig_2.update_layout( height=480,width=700,title_font_color='orange',title_font=dict(size=20),title_x=0.2)
        st.plotly_chart(fig_2)


        # Chart 3: Cuisine Cost Comparison
        
        country_data = df3[df3['Country'] == selected_country]
        top_cuisines = country_data.groupby('Cuisines')['Average Cost for two'].sum().nlargest(10).reset_index()
    
        fig1= px.bar(top_cuisines, x='Cuisines', y='Average Cost for two', title='Cuisine Cost Comparison')
        fig1.update_layout( height=550,width=700,title_font_color='orange',title_font=dict(size=20),title_x=0.3)
        fig1.update_traces(textfont_size=12,marker_color=px.colors.diverging.PiYG)
        st.plotly_chart(fig1)

    if select=='City Analysis':

        # Filter data for India
        india_data = df3[df3['Country'] == 'India']

        # Calculate average cost for two people for each cuisine
        avg_cost_by_cuisine = india_data.groupby('Cuisines')['Average Cost for two'].mean().reset_index()

        # Sort cuisines by average cost in descending order
        top_expensive_cuisines = avg_cost_by_cuisine.sort_values(by='Average Cost for two', ascending=False)

        # Create a bar chart to visualize top costly cuisines
        fig_3 = px.bar(top_expensive_cuisines.head(10), x='Cuisines', y='Average Cost for two',title='Top 10 Costliest Cuisines in India')
        fig_3.update_layout( height=580,width=800,title_font_color='orange',title_font=dict(size=18),title_x=0.3)
        fig_3.update_traces(textfont_size=12,marker_color=px.colors.diverging.curl_r)
        fig_3.update_xaxes(title='Cuisine')
        fig_3.update_yaxes(title='Average Cost for two (INR)')
        st.plotly_chart(fig_3)

        # 4. Filter based on the city

        st.subheader(':violet[Filter based on the city]')

        st.sidebar.header(":green[Choose your filter:]")

        selected_country_1 = st.sidebar.selectbox('Select Country', df3['Country'].unique(),index=None,placeholder="Select")
        selected_city = st.sidebar.selectbox('Select City', df3[df3['Country'] == selected_country_1]['City'].unique(),index=None,placeholder="Select")
        
        city_data = df3[df3['City'] == selected_city]
        
        # Find which is famous cuisine in the city
        # Count the occurrences of each cuisine
        cuisine_counts = city_data['Cuisines'].value_counts().head(5)

        fig_4 =px.pie(cuisine_counts, 
                    values=cuisine_counts.values, 
                    names=cuisine_counts.index,
                    hole=0.5,color_discrete_sequence=px.colors.sequential.Tealgrn_r,
                    title=f'Famous Cuisine in {selected_city}')
        fig_4.update_traces(textposition='outside', textinfo='percent')
        fig_4.update_layout( height=450,width=900,title_font_color='orange',title_font=dict(size=20),title_x=0.2)
        st.plotly_chart(fig_4)

        #  Find which is costlier cuisine
        avg_cost_by_cuisine = city_data.groupby('Cuisines')['Average Cost for two'].mean().reset_index()

        # Sort cuisines by average cost in descending order
        sorted_cuisines = avg_cost_by_cuisine.sort_values(by='Average Cost for two', ascending=False)

        # Plot the bar chart
        fig_5 = px.bar(sorted_cuisines.head(10), x='Cuisines', y='Average Cost for two',
                    title=f'Costlier Cuisines in {selected_city}', labels={'x':'Cuisine', 'y':'Average Cost for two (INR)'})
        fig_5.update_traces(textfont_size=12,marker_color=px.colors.diverging.RdYlBu)
        fig_5.update_layout( height=580,width=700,title_font_color='orange',title_font=dict(size=20),title_x=0.3)
        st.plotly_chart(fig_5)

        # Rating count in the city (based on rating test)
        rating_counts = city_data['Rating text'].value_counts().reset_index()
        fig_6=px.bar(rating_counts, x='Rating text', y='count',color='Rating text',
                                title=f' Rating Count in {selected_city} based on Rating Test')
        fig_6.update_layout( height=550,width=600,title_font_color='orange',title_font=dict(size=20),title_x=0.2)
        st.plotly_chart(fig_6)

        delivery_counts = city_data['Has Online delivery'].value_counts()
        fig_7 = px.pie(values=delivery_counts.values, names=delivery_counts.index,color_discrete_sequence=px.colors.diverging.Spectral,
                    title=f'Online Delivery vs. Dine-in (in {selected_city})')
        fig_7.update_layout( height=450,width=700,title_font_color='orange',title_font=dict(size=20),title_x=0.2)
        st.plotly_chart(fig_7)
    
    if select=='City comparision':
        
        #part of India spends more on online delivery
        city_restaurants_count = df3[df3['Country'] == 'India']
        city_spending =city_restaurants_count.groupby(['City', 'Has Online delivery'])['Average Cost for two'].mean().reset_index()

        city_online_delivery_spending = city_spending[city_spending['Has Online delivery'] == 'Yes']
        city_online=city_online_delivery_spending.sort_values(by='Average Cost for two', ascending=False).head(10)
        fig_8 = px.bar(city_online, x='City', y='Average Cost for two',hover_data='Has Online delivery',
               title='Part of India spends more on online delivery')
        fig_8.update_traces(textfont_size=12,marker_color=px.colors.diverging.Spectral_r)
        fig_8.update_layout( height=500,width=700,title_font_color='orange',title_font=dict(size=20),title_x=0.3,xaxis_title='City', yaxis_title='Online Delivery Spending')
        st.plotly_chart(fig_8)

        #  part of India spends more on dine-in

        city_dine_in_spending = city_spending[city_spending['Has Online delivery'] == 'No']
        city_dine=city_dine_in_spending.sort_values(by='Average Cost for two', ascending=False).head(10)

        fig_9 = px.pie(city_dine, names='City', values='Average Cost for two', labels={'x' :'City', 'y':'Online Delivery Spending'},hover_data='Has Online delivery',
               title='Part of India spends more on dine in')
        fig_9.update_traces(textfont_size=12)
        fig_9.update_layout( height=480,width=800,title_font_color='orange',title_font=dict(size=20),title_x=0.2)
        st.plotly_chart(fig_9)


        # Define the data
        locations =['Mumbai', 'Delhi', 'Bangalore', 'Kolkata', 'Chennai']
        living_costs = [9000,8000,7500,6000,6500] 
        threshold =7000  # Define a threshold for high and low living costs

        # Create a DataFrame
        df_l = pd.DataFrame({'Location': locations, 'Living Cost': living_costs})

        # Categorize cities into high and low living costs
        df_l['Cost Category'] = 'High Cost'
        df_l.loc[df_l['Living Cost'] < threshold, 'Cost Category'] = 'Low Cost'
        colors = {'High Cost': 'salmon', 'Low Cost': 'cyan'}
        
        fig_l = px.bar(df_l, x='Location', y='Living Cost', color='Cost Category',
                    title='Comparison of High and Low Living Costs in Different Locations',
                    labels={'Living Cost': 'Living Cost ($)', 'Location': 'Location'},
                    barmode='group',pattern_shape_sequence = [ '.'],color_discrete_map=colors)

        # Add threshold line
        fig_l.add_hline(y=threshold, line_dash="dot", line_color="violet", annotation_text="Threshold", 
                    annotation_position="top right", annotation_font_color="red")
        fig_l.update_layout( height=500,width=680,title_font_color='orange',title_font=dict(size=20),title_x=0.1)
        fig_l.update_traces( marker_line_color = 'red')
        st.plotly_chart(fig_l)


    if select=='Top Charts':
        
        tab1,tab2,tab3,tab4,tab5,tab6=st.tabs(['Top 10','Ratings','Locality','Rating text','Rating colors','correlation'])

        with tab1:

            # Top 10 Cuisines
            top_cuisines_1 = df3['Cuisines'].value_counts().head(10).reset_index()
            top_cuisines_1.columns = ['Cuisine', 'Number of Restaurants']
            fig_10 = px.bar(top_cuisines_1, x='Number of Restaurants', y='Cuisine', orientation='h', 
                        color='Cuisine', color_discrete_sequence=['#7eb54e']*len(top_cuisines_1))
            fig_10.update_layout(title='Top 10 Cuisines', xaxis_title='Number of Restaurants', yaxis_title='Cuisine',
                                 title_font_color='orange',title_font=dict(size=20),title_x=0.3)
            st.plotly_chart(fig_10)

            # Distribution of Restaurants by City
            fig_m = px.scatter_mapbox(df3, lat="Latitude", lon="Longitude", hover_name="City", zoom=3,color='City')

            fig_m.update_layout(mapbox_style="open-street-map", title="Distribution of Restaurants by City",
                            margin={"r":0,"t":30,"l":0,"b":0},title_font_color='orange',title_font=dict(size=20),title_x=0.3)
            fig_m.update_traces(showlegend=False)
            st.plotly_chart(fig_m)
            

            # Top 10 Restaurant Chains
            restaurant_chain_counts = df3['Restaurant Name'].value_counts().head(10)
            restaurant_chain_df = pd.DataFrame({'Restaurant Chain': restaurant_chain_counts.index, 'Number of Outlets': restaurant_chain_counts.values})
            fig_11 = px.bar(restaurant_chain_df, x='Restaurant Chain', y='Number of Outlets', 
                        title='Top 10 Restaurant',
                        labels={'Number of Outlets': 'Number of Outlets'},
                        color='Number of Outlets',
                        color_continuous_scale=px.colors.sequential.Sunsetdark_r)
            fig_11.update_layout(xaxis={'categoryorder':'total descending'}, height=450,width=700,title_font_color='orange',title_font=dict(size=18),title_x=0.3)
            st.plotly_chart(fig_11)
    

        with tab2:

            # Aggregate Rating vs. Cost for Two People by Price range
            fig_12 = px.scatter(df3, y='Aggregate rating', x='Average Cost for two', color='Price range',
                 title='Aggregate Rating vs. Cost for Two People by Price range',color_continuous_scale='viridis',
                 labels={'Aggregate Rating': 'Aggregate Rating', 'Average Cost for two': 'Average Cost for Two'})
            fig_12.update_layout( height=500,width=800,title_font_color='orange',title_font=dict(size=20),title_x=0.2)
            fig_12.update_traces(marker=dict(size=9))
            st.plotly_chart(fig_12)

            #Comparison of Table Booking and Online Delivery by Aggregate Rating
            grouped_data = df3.groupby(['Aggregate rating', 'Has Table booking', 'Has Online delivery']).size().reset_index(name='Count')
            aggregate_ratings = sorted(df3['Aggregate rating'].unique())
            fig_13= px.bar(grouped_data, x='Aggregate rating', y='Count', color='Has Online delivery',
                        facet_col='Has Table booking', category_orders={'Aggregate rating': aggregate_ratings},
                        labels={'Aggregate rating': 'Aggregate Rating', 'Count': 'Number of Restaurants',
                                'Has Table booking': 'Table Booking', 'Has Online delivery': 'Online Delivery'},
                        title='Comparison of Table Booking and Online Delivery by Aggregate Rating')
            fig_13.update_traces(textfont_size=12)
            fig_13.update_layout( height=450,width=800,title_font_color='orange',title_font=dict(size=20),title_x=0.1)
            st.plotly_chart(fig_13)

            # Rating vs Votes
            fig_14 = px.scatter(df3, x='Aggregate rating', y='Votes', 
                 title='Rating vs Votes',color='Aggregate rating',
                 labels={'Aggregate rating': 'Aggregate Rating', 'Votes': 'Votes'},color_continuous_scale='Inferno',
                 opacity=0.5)

            fig_14.update_traces(marker=dict(size=10))
            fig_14.update_layout( height=450,width=900,title_font_color='orange',title_font=dict(size=20),title_x=0.3)
            st.plotly_chart(fig_14)

        
        with tab3:

            # Top 10 number of restaurants by locality
            restaurant_count_by_locality = df3['Locality'].value_counts().sort_values(ascending=False).head(10)

            fig_15 = px.bar(restaurant_count_by_locality, 
                        x=restaurant_count_by_locality.index, 
                        y=restaurant_count_by_locality.values,
                        labels={'x': 'Locality', 'y': 'Number of Restaurants'},
                        title='Top 10 Restaurants by Locality',
                        color=restaurant_count_by_locality.index,
                        color_discrete_sequence=px.colors.qualitative.Safe)

            fig_15.update_layout(xaxis_tickangle=-45,height=470,width=700,title_font_color='orange',title_font=dict(size=20),title_x=0.2)
            st.plotly_chart(fig_15)

            #Top 10 Localities with Online Delivery
            online_delivery_df = df3[df3['Has Online delivery'] == 'Yes']
            online_delivery_count_by_locality = online_delivery_df['Locality'].value_counts().head(10)

            fig_16 = px.bar(online_delivery_count_by_locality, y=online_delivery_count_by_locality.index, x=online_delivery_count_by_locality.values,
                        orientation='h')
            fig_16.update_layout(title='Top 10 Localities with Online Delivery', xaxis_title='Number of Restaurants with Online Delivery',
                            yaxis_title='Locality',height=450,width=600,title_font_color='orange',title_font=dict(size=20),title_x=0.2)

            st.plotly_chart(fig_16)

            # Average Cost for Two by Locality (Top 10)
            average_cost_by_locality = df3.groupby('Locality')['Average Cost for two'].mean().sort_values(ascending=False).head(10)

            fig_17 = px.bar(x=average_cost_by_locality.index, 
                        y=average_cost_by_locality.values,
                        labels={'x': 'Locality', 'y': 'Average Cost for Two'},color_discrete_sequence=px.colors.sequential.haline_r,
                        title='Top 10 Average Cost for Two by Locality ')
            fig_17.update_layout(xaxis_tickangle=18,height=550,width=700,title_font_color='orange',title_font=dict(size=20),title_x=0.2)
            st.plotly_chart(fig_17)
        
        with tab4:

            # Distribution of Rating Texts
            rating_text_counts = df3['Rating text'].value_counts().reset_index()
            rating_text_counts.columns = ['Rating Text', 'Count']

            fig_18 = px.pie(rating_text_counts, names='Rating Text',values='Count',color_discrete_sequence=px.colors.sequential.Oryel_r, 
                        title='Distribution of Rating Texts',
                        labels={'Rating Text': 'Rating Text', 'Count': 'Count'},hole=0.5)
            fig_18.update_traces(textposition='outside', textinfo='percent')
            fig_18.update_layout( height=450,width=800,title_font_color='orange',title_font=dict(size=20),title_x=0.3)
            st.plotly_chart(fig_18)
        
            # Number of Restaurants by Rating Text for Online Delivery
            grouped_data = df3.groupby(['Rating text', 'Has Online delivery']).size().reset_index(name='Count')
            fig_19 = px.bar(grouped_data, x='Rating text', y='Count', color='Has Online delivery', pattern_shape = 'Count',
                        labels={'Rating Text': 'Rating Text', 'Count': 'Number of Restaurants',
                                'Has Online delivery': 'Online Delivery'},pattern_shape_sequence = ['x', '.', '+', '/', '.'],
                        title='Number of Restaurants by Rating Text for Online Delivery')
            fig_19.update_layout( height=450,width=850,title_font_color='orange',title_font=dict(size=20),title_x=0.2)
            st.plotly_chart(fig_19)
        
        
        
        with tab5:
        
            # Proportion of Rating Colors
            rating_color_count = df3['Rating color'].value_counts().reset_index()
            rating_color_count.columns = ['Rating color', 'Count']
            fig_20 = px.pie(rating_color_count, values='Count', names='Rating color',
                        title='Proportion of Rating Colors')

            fig_20.update_traces(textposition='inside', textinfo='percent')
            fig_20.update_layout( height=450,width=800,title_font_color='orange',title_font=dict(size=20),title_x=0.3)
            st.plotly_chart(fig_20)

            # Rating Color vs. Online Delivery Availability
            
            Cross_tab = pd.crosstab(df3['Rating color'], df3['Has Online delivery'])
            cross_tab = Cross_tab.reset_index()
            cross_tab_melted = cross_tab.melt(id_vars='Rating color', var_name='Has Online delivery', value_name='Count')
            fig_21 = px.bar(cross_tab_melted, x='Rating color', y='Count', color='Has Online delivery',
                        title='Rating Color vs. Online Delivery Availability',
                        labels={'Rating color': 'Rating Color', 'Count': 'Number of Restaurants', 'Has Online delivery': 'Has Online Delivery'},
                        barmode='stack',
                        color_discrete_sequence=['skyblue','pink'])
            fig_21.update_layout(xaxis_tickangle=-45,height=550,width=700,title_font_color='orange',title_font=dict(size=20),title_x=0.3)
            st.plotly_chart(fig_21)

            # Average Price Range by Rating Colo
            average_price_range = df3.groupby('Rating color')['Price range'].mean().reset_index()
            fig_22 = px.line(average_price_range, x='Rating color', y='Price range', 
                        title='Average Price Range by Rating Color',
                        labels={'Rating Color': 'Rating Color', 'Price Range': 'Average Price Range'})

            fig_22.update_layout(xaxis_tickangle=-45,width=650,height=600,title_font_color='orange',title_font=dict(size=20),title_x=0.3)
            fig_22.update_traces(mode="markers+lines",line_color='#147852')
            st.plotly_chart(fig_22)


        with tab6:

            # Filter columns with float and integer data types
            numeric_columns = df3.select_dtypes(include=['float64', 'int64'])

            # Calculate the correlation matrix
            correlation_matrix = numeric_columns.corr()

            # Create a Plotly figure for the heatmap
            fig = px.imshow(correlation_matrix.values,
                            labels=dict(color="Correlation"),
                            x=correlation_matrix.columns,
                            y=correlation_matrix.columns,
                            color_continuous_scale='RdBu',  # Choose a diverging color scale
                            color_continuous_midpoint=0,  # Center color scale at 0 correlation
                        )

            # Add annotations for correlation values inside the heatmap cells
            for i in range(len(correlation_matrix.columns)):
                for j in range(len(correlation_matrix.columns)):
                    fig.add_annotation(
                        x=correlation_matrix.columns[i],
                        y=correlation_matrix.columns[j],
                        text=str(correlation_matrix.values[i, j].round(2)),
                        showarrow=False,
                        font=dict(color="black", size=10),
                    )

            # Customize the figure layout
            fig.update_layout(title="Correlation Matrix Heatmap",
                            width=800, height=600,title_font_color='orange',title_font=dict(size=20),title_x=0.3)

            # Update the color bar to show correlation values
            fig.update_coloraxes(colorbar=dict(title="Correlation"))

            # Display the heatmap using Streamlit
            st.plotly_chart(fig)


if selected=='Insights':

    st.markdown(""" 
            1. :blue[Popular Cuisines:]
                Identify the most popular cuisines in different regions/countries based on the number of restaurants offering them.
            
            2. :blue[Restaurant Ratings:]
                Analyze the distribution of restaurant ratings and identify factors that correlate with higher ratings, such as price range, location, or cuisine type.
                
            3. :blue[Cost Analysis:]
                Compare the average cost for two people across different cities or countries to understand variations in dining expenses.
            
            4. :blue[Online Delivery:]
                Analyze online delivery services among restaurants and how it correlates with factors such as cuisine type, location, and customer ratings. Identify trends in online ordering behavior and customer preferences.

            5. :blue[User Reviews:]
                Analyze user reviews to identify common positive and negative aspects mentioned by customers, helping restaurants understand areas for improvement.
            
            6. :blue[Restaurant:]
                    Identify popular restaurant and analyze their distribution across different regions.
            
            7. :blue[Location-based Analysis:]
                To visualize the distribution of restaurants across different cities or regions. Identify areas with high restaurant density and areas where dining options may be limited.
            
            8. :blue[Price Analysis:]
                Analyze how price range affects restaurant popularity and user ratings, and identify the price range segments with the highest customer satisfaction.

            9. :blue[Customer Preferences by Cuisine:]
                Analyze customer preferences for different cuisines based on ratings and reviews. Identify cuisines that consistently receive high ratings and those that may be less popular among dinners.""")
    

    button_1 = st.button("EXIT!")

    if button_1:
        st.success("**Thank you for utilizing this platform.I hope these insights helps to improve zomato's business!**")
