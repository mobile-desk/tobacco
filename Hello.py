# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
import pandas as pd
from joblib import load
import plotly.express as px

from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Tobacco",
        page_icon="🚬",
    )
    
    st.link_button("Back To Project", "https://journeygenius.pythonanywhere.com/tobacco")

    df = pd.read_csv('tobacco_analysis.csv')
    df.dropna(inplace=True)

    st.title("Tobacco Use Prevalence Analysis")

    # Model
    st.subheader('Get Prediction')
    # Year with the highest cigarette use prevalence
    highest_prevalence_year = df.loc[df['Cigarette Use Prevalence % (Focus group)'].idxmax()]['Year']
    highest_prevalence_value = df['Cigarette Use Prevalence % (Focus group)'].max()
    highest_prevalence_state = df.loc[df['Cigarette Use Prevalence % (Focus group)'].idxmax()]['State']
    
    lowest_prevalence_year = df.loc[df['Cigarette Use Prevalence % (Focus group)'].idxmin()]['Year']
    lowest_prevalence_value = df['Cigarette Use Prevalence % (Focus group)'].min()
    lowest_prevalence_state = df.loc[df['Cigarette Use Prevalence % (Focus group)'].idxmin()]['State']
    
    

    with st.sidebar:
        # Display the information
        st.title('Cigarette Use Prevalence Analysis')
        st.header('Statistics')
        st.success(
            f"The year with the highest cigarette use prevalence was {highest_prevalence_year} with a prevalence of {highest_prevalence_value}%.")
        st.info(f"The state with the highest cigarette use prevalence was {highest_prevalence_state}.")
        st.warning(
            f"The year with the lowest cigarette use prevalence was {lowest_prevalence_year} with a prevalence of {lowest_prevalence_value}%.")
        st.error(f"The state with the lowest cigarette use prevalence was {lowest_prevalence_state}.")

    state_data = {
        "Alabama": 0,
        "Alaska": 1,
        "Arizona": 2,
        "Arkansas": 3,
        "California": 4,
        "Colorado": 5,
        "Connecticut": 6,
        "Delaware": 7,
        "District of Columbia": 8,
        "Florida": 9,
        "Georgia": 10,
        "Hawaii": 11,
        "Idaho": 12,
        "Illinois": 13,
        "Indiana": 14,
        "Iowa": 15,
        "Kansas": 16,
        "Kentucky": 17,
        "Louisiana": 18,
        "Maine": 19,
        "Maryland": 20,
        "Massachusetts": 21,
        "Michigan": 22,
        "Minnesota": 23,
        "Mississippi": 24,
        "Missouri": 25,
        "Montana": 26,
        "Nebraska": 27,
        "Nevada": 28,
        "New Hampshire": 29,
        "New Jersey": 30,
        "New Mexico": 31,
        "New York": 32,
        "North Carolina": 33,
        "North Dakota": 34,
        "Ohio": 35,
        "Oklahoma": 36,
        "Oregon": 37,
        "Pennsylvania": 38,
        "Rhode Island": 39,
        "South Carolina": 40,
        "South Dakota": 41,
        "Tennessee": 42,
        "Texas": 43,
        "Utah": 44,
        "Vermont": 45,
        "Virginia": 46,
        "Washington": 47,
        "West Virginia": 48,
        "Wisconsin": 49,
        "Wyoming": 50
    }

    demographic_data = {
        "Age":0,
        "Disability":1,
        "Education":2,
        "Employment":3,
        "Income":4,
        "Mental Health":5,
        "Race and Ethnicity":6,
        "Sex at Birth":7,
        "Urban-Rural":8
    }

    comparing_data = {
        "$75,000 or above": 0,
        "Age 18-24": 1,
        "Age 25-44": 2,
        "Age 45-64": 3,
        "Age 65 or older": 4,
        "Employed or Self": 5,
        "Female": 6,
        "From $20,000-$74,999": 7,
        "Graduated from college": 8,
        "Having any Disability": 9,
        "High School": 10,
        "Hispanic": 11,
        "Homemaker or Student": 12,
        "Less than $20,000": 13,
        "Less than High School": 14,
        "Male": 15,
        "Mild Mental Distress": 16,
        "No Disability": 17,
        "No Mental Distress": 18,
        "Non-Hispanic AIAN": 19,
        "Non-Hispanic Asian": 20,
        "Non-Hispanic Black": 21,
        "Non-Hispanic White": 22,
        "Retired": 23,
        "Rural": 24,
        "Severe Mental Distress": 25,
        "Unable to work": 26,
        "Unemployed": 27,
        "Urban": 28
    }


    col333, col444, col555 = st.columns(3)
    with col333:
        with st.popover("Open states popover"):
            num_states = len(state_data)
            half_states = num_states // 2
            keys = list(state_data.keys())
            values = list(state_data.values())

            # Create two columns for displaying data side by side
            col1, col2, col3, col4 = st.columns(4)

            # Create a table in the first column
            with col1:
                st.write("State Names")
                for i in range(half_states):
                    st.write(keys[i])

            # Create a table in the second column
            with col2:
                st.write("State Numbers")
                for i in range(half_states):
                    st.write(values[i])

            # Create a table in the third column
            with col3:
                st.write("State Names")
                for i in range(half_states, num_states):
                    st.write(keys[i])

            # Create a table in the fourth column
            with col4:
                st.write("State Numbers")
                for i in range(half_states, num_states):
                    st.write(values[i])


    with col444:
        with st.popover("Open demographics popover"):
            num_demographic = len(demographic_data)
            half_demographic = num_demographic // 2
            keyss = list(demographic_data.keys())
            valuess = list(demographic_data.values())

            # Create two columns for displaying data side by side
            col1a, col2a, col3a, col4a = st.columns(4)

            # Create a table in the first column
            with col1a:
                st.write("Demographic Names")
                for i in range(half_demographic):
                    st.write(keyss[i])

            # Create a table in the second column
            with col2a:
                st.write("Demographic Numbers")
                for i in range(half_demographic):
                    st.write(valuess[i])

            # Create a table in the third column
            with col3a:
                st.write("Demographic Names")
                for i in range(half_demographic, num_demographic):
                    st.write(keyss[i])

            # Create a table in the fourth column
            with col4a:
                st.write("Demographic Numbers")
                for i in range(half_demographic, num_demographic):
                    st.write(valuess[i])

    with col555:
        with st.popover("Open comparing popover"):
            num_comparing = len(comparing_data)
            half_comparing = num_comparing // 2
            keyssg = list(comparing_data.keys())
            valuessg = list(comparing_data.values())

            # Create two columns for displaying data side by side
            col1a3, col2a4, col3ay, col4as = st.columns(4)

            # Create a table in the first column
            with col1a3:
                st.write("Comparing Names")
                for i in range(half_comparing):
                    st.write(keyssg[i])

            # Create a table in the second column
            with col2a4:
                st.write("Comparing Numbers")
                for i in range(half_comparing):
                    st.write(valuessg[i])

            # Create a table in the third column
            with col3ay:
                st.write("Comparing Names")
                for i in range(half_comparing, num_comparing):
                    st.write(keyssg[i])

            # Create a table in the fourth column
            with col4as:
                st.write("Comparing Numbers")
                for i in range(half_comparing, num_comparing):
                    st.write(valuessg[i])



    # model form
    col11, col22 = st.columns(2)

    Year = col11.number_input("Year", min_value=2011, max_value=2022, value=2022)
    State = col11.number_input("State", min_value=0, max_value=50, value=50)
    Demographic = col22.number_input("Demographic", min_value=0, max_value=8, value=8)
    Comparing = col22.number_input("Comparing", min_value=0, max_value=28, value=28)

    model = load('model_best.joblib')

    # Make predictions
    input_data = [[Year, State, Demographic, Comparing]]
    prediction = model.predict(input_data)

    st.markdown(f":blue-background[{prediction}%]")
    #col1 = st.columns(1)
    #col1.metric(label="Tobacco Use Prevalence", value=f"{prediction:,.2f}%")





    st.header('State-wise Analysis')
    # Bar chart showing average cigarette use prevalence across different states
    state_avg = df.groupby('State')['Cigarette Use Prevalence % (Focus group)'].mean().reset_index()
    bar_chart = px.bar(state_avg, x='State', y='Cigarette Use Prevalence % (Focus group)',
                      title='Average Cigarette Use Prevalence by State')
    bar_chart.update_layout(
        xaxis_title= 'State',
        yaxis_title= 'Prevalence %',
        )

    st.plotly_chart(bar_chart)


    # Heatmap displaying cigarette use prevalence over the years for each state
    heatmap_data = df.pivot_table(index='State', columns='Year', values='Cigarette Use Prevalence % (Focus group)')
    heatmap = px.imshow(heatmap_data, labels=dict(x="Year", y="State", color="Prevalence %"),
                        title='Cigarette Use Prevalence Over Years by State')

    st.plotly_chart(heatmap)


    # Demographic Analysis



    # Bar chart showing average cigarette use prevalence across different demographic groups
    demo_avg = df.groupby('Demographic')['Cigarette Use Prevalence % (Focus group)'].mean().reset_index()
    bar_chart_demo = px.bar(demo_avg, x='Demographic', y='Cigarette Use Prevalence % (Focus group)',
                            title='Average Cigarette Use Prevalence by Demographic Group')


    bar_chart_demo.update_layout(
    xaxis_title='Demographic',
    yaxis_title='Prevalence %',
    )


    st.plotly_chart(bar_chart_demo)
    # Line chart displaying trends in cigarette use prevalence over the years for specific demographic groups



   # selected_demo = st.selectbox('Select Demographic Group:', df['Demographic'].unique())
  #  demo_data = df[df['Demographic'] == selected_demo]

   # demo_trends = demo_data.groupby('Year')['Cigarette Use Prevalence % (Focus group)'].mean().reset_index()
   # line_chart_demo = px.line(demo_trends, x='Year', y='Cigarette Use Prevalence % (Focus group)',
                        #      title=f'Cigarette Use Prevalence Trend for {selected_demo}')


    selected_demo = st.selectbox('Select Demographic Group:', df['Demographic'].unique())
    demo_data = df[df['Demographic'] == selected_demo]

    # Group by 'Year' and 'Demographic Comparing (Focus group)', calculate mean prevalence
    demo_trends = demo_data.groupby(['Year', 'Demographic Comparing (Focus group)'])['Cigarette Use Prevalence % (Focus group)'].mean().reset_index()

    # Plotting
    line_chart_demo = px.line(demo_trends, x='Year', y='Cigarette Use Prevalence % (Focus group)',
                            title=f'Cigarette Use Prevalence Trend for {selected_demo}',
                            color='Demographic Comparing (Focus group)')


    line_chart_demo.update_layout(
        xaxis_title='Year',
        yaxis_title='Prevalence %',
        )
    
    st.plotly_chart(line_chart_demo)
    
    

    # Comparative Analysis


    # Scatter plot comparing cigarette use prevalence between different demographic groups
    scatter_plot = px.scatter(df, x='Comparing (Focus group)', y='Cigarette Use Prevalence % (Focus group)',
                              color='Demographic', title='Comparative Cigarette Use Prevalence')

    st.plotly_chart(scatter_plot)
    
    
    
    # Temporal Analysis


  

    # Bar chart displaying change in cigarette use prevalence from a reference year to the latest year available
    ref_year = 2011  # Change this to your reference year
    latest_year = df['Year'].max()
    change_df = df[df['Year'].isin([ref_year, latest_year])]
    change_chart = px.bar(change_df, x='State', y='Cigarette Use Prevalence % (Focus group)',
                          color='Year', barmode='group',
                          title=f'Change in Cigarette Use Prevalence ({latest_year} - {ref_year})')

    st.plotly_chart(change_chart) 
    
    # Box plot showing the distribution of cigarette use prevalence for each demographic group
    box_plot = px.box(df, x='Demographic', y='Cigarette Use Prevalence % (Focus group)',
                      title='Distribution of Cigarette Use Prevalence by Demographic Group')

    st.plotly_chart(box_plot)

    # Display performance metrics (e.g., Mean Squared Error, R-squared)
    mse = 25.47
    r2 = 0.71


  


    # Map Visualization
    st.link_button("View More Info", "https://journeygenius.pythonanywhere.com/tobacco")



if __name__ == "__main__":
    run()
