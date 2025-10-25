
from sklearn.neighbors import NearestCentroid
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from sklearn.cluster import AgglomerativeClustering
import plotly.express as px
import math

if "show_treemap" not in st.session_state:
    st.session_state.show_treemap = False

X_ = pd.read_csv("data_to_test_on.csv")
clust = pd.read_csv("clust.csv")
ac = AgglomerativeClustering(n_clusters=5)
bucket = ac.fit_predict(X_)
centroid_model = NearestCentroid()
centroid_model.fit(X_, bucket)


def suggest_cost(cluster):
    if cluster == 0:
        return "$10,626"
    elif cluster == 1:
        return "$10,933"
    elif cluster == 2:
        return "$10,362"
    elif cluster == 3:
        return "$10,489"
    elif cluster == 4:
        return "$10,626"
    else:
        return "No recommendation can be given."


st.markdown(
    """
     <h1 style="
        text-align: center;
        color: rgb(35, 59, 66);">
        Welcome to Your AI Lead Optimizer Advisor!
    </h1>
    """,
    unsafe_allow_html=True,
)

st.write("Please upload your file below to get acquisition cost suggestions.")
uploaded_file = st.file_uploader("Upload Excel or CSV", type=['xlsx', 'csv'])

if uploaded_file:    
    if uploaded_file.name.endswith('.csv'):
        new_data = pd.read_csv(uploaded_file, encoding='utf-8')
    else:
        new_data = pd.read_excel(uploaded_file)

    st.write("Here is a preview of your data:")
    st.write(new_data.head())  

    new_data['Cluster'] = centroid_model.predict(new_data)
    new_data['Cost to Acquire Suggestion'] = new_data['Cluster'].apply(suggest_cost)

    st.write("Here are the results with cluster numbers and acquisition cost suggestions:")
    st.write(new_data[['Cluster', 'Cost to Acquire Suggestion']])

    # Allow user to download the result
    result_file = new_data.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download Results as CSV",
        data=result_file,
        file_name='acquisition_cost_recommendations.csv',
        mime='text/csv'
    )


############################################# ALL FUNCTIONS SECTION
####### 
# Times Contacted Distribution
def times_contacted_distribution():
    st.title("Times Contacted Distribution")
    stats = clust.groupby("bucket")["Times_Contacted"].describe()
    selected_buckets = st.multiselect("Select one or more buckets:", stats.index, key="unique_key_for_multiselect")

    if selected_buckets:
        bucket_stats = stats.loc[selected_buckets]
        for bucket, stats_row in bucket_stats.iterrows():
          st.write(f"### Times Contacted Distribution for Bucket: {bucket}")

          q1 = stats_row["25%"]
          q2 = stats_row["50%"]
          q3 = stats_row["75%"]
          min_age = stats_row["min"]
          max_age = stats_row["max"]
          bar_width = 500

          q1_pct = (q1 - min_age) / (max_age - min_age) * 100
          q2_pct = (q2 - min_age) / (max_age - min_age) * 100
          q3_pct = (q3 - min_age) / (max_age - min_age) * 100
           
          st.markdown(
            f"""
            <div style='position: relative; width: {bar_width}px; height: 30px; background: linear-gradient(to right,
            #fff4e6 0%, #ffc48c 25%, #ff7b28 50%, #ff506e 75%, #d923a3 100%);
            border-radius: 15px;'>
                <!-- Marker for 25th percentile (Q1) -->
                <div style='position: absolute; left: {25}%; top: 0; bottom: 0; width: 2px; background-color: #f3fafc;'></div>
                <div style='position: absolute; left: {25}%; top: 35px; font-size: 12px; color: black; text-align: center; transform: translateX(-50%);'>25%</div>
                <!-- Marker for 50th percentile (Median) -->
                <div style='position: absolute; left: {50}%; top: 0; bottom: 0; width: 2px; background-color: #f3fafc;'></div>
                <div style='position: absolute; left: {50}%; top: 35px; font-size: 12px; color: black; text-align: center; transform: translateX(-50%);'>50%</div>
                <!-- Marker for 75th percentile (Q3) -->
                <div style='position: absolute; left: {75}%; top: 0; bottom: 0; width: 2px; background-color: #f3fafc;'></div>
                <div style='position: absolute; left: {75}%; top: 35px; font-size: 12px; color: black; text-align: center; transform: translateX(-50%);'>75%</div>
            </div>
            """, unsafe_allow_html=True)

          # Display Quartile Labels
          st.markdown("<br>", unsafe_allow_html=True)  
          st.markdown("<br>", unsafe_allow_html=True)  
          st.write(f"**Min:** {min_age}")
          st.write(f"**25th Percentile (Q1):** {q1}")
          st.write(f"**50th Percentile (Median):** {q2}")
          st.write(f"**75th Percentile (Q3):** {q3}")
          st.write(f"**Max:** {max_age}")
          st.markdown("<br>", unsafe_allow_html=True)
    else:
      st.write("Please select at least one bucket.")


#######
# Days to Respond Distribution
def days_distribution():
    st.title("Days to Respond Distribution by Bucket")
    selected_buckets2 = st.multiselect("Select one or more buckets:", clust['bucket'].unique(), key="unique_key_for_multiselect2")

    if selected_buckets2:
        selected_data = clust[clust['bucket'].isin(selected_buckets2)]
        fig_width = max(8, len(selected_buckets2) * 1.5)  
        fig, ax = plt.subplots(figsize=(fig_width, 6))
        ax.set_facecolor("#ffffff")

        boxprops = dict(facecolor="#233B42", edgecolor = "#233B42")  
        medianprops = dict(color="white", linestyle=":") 
        flierprops = dict(marker="o", markerfacecolor="#ff506e", markeredgecolor = "#ff506e", markersize=5, linestyle=" ")  
        capprops = dict(color="#233B42", linewidth=1.5)
        whiskerprops = dict(color="#233B42", linewidth=1.5)
        bp = selected_data.boxplot(
        column="Days_to_Respond",
        by="bucket",
        ax=ax,
        boxprops=boxprops,
        medianprops=medianprops,
        flierprops=flierprops,
        capprops = capprops,
        whiskerprops = whiskerprops,
        patch_artist=True)

        ax.grid(False)
        plt.suptitle("")
        plt.suptitle("") 
        ax.set_title("Days to Respond Distribution by Selected Buckets")
        ax.set_xlabel("Bucket")
        ax.set_ylabel("Number of Days")
        st.pyplot(fig)

    else:
        st.write("Please select at least one bucket.")


#######
# Campaign Cost Distribution
def cost_ditribution():
    st.title("Total Campaign Cost by Bucket") 
    selected_buckets4 = st.multiselect(
        "Select one or more buckets:",
        clust['bucket'].unique(),
        key="unique_key_for_multiselect4"
    )

    if selected_buckets4:
        filtered_data = clust[clust['bucket'].isin(selected_buckets4)]
        summary_stats = filtered_data.groupby("bucket")["Total_Campaign_Cost"].agg(
            min_val="min",
            q25_val=lambda x: x.quantile(0.25),
            median_val="median",
            q75_val=lambda x: x.quantile(0.75),
            max_val="max"
        ).reset_index()
        plot_data = summary_stats.set_index("bucket")[["min_val", "q25_val", "median_val", "q75_val", "max_val"]]
        plot_data.columns = ["min", "25%", "50%", "75%", "max"]
        custom_colors = ["#fff4e6", "#ffc48c", "#ff7b28", "#ff506e",  "#d923a3"]

        st.write("Summary statistics for Campaign Cost (Selected Percentiles):")
        num_bars = len(selected_buckets4)

        fig, ax = plt.subplots(figsize=(8, max(2, len(selected_buckets4) * 0.8)))
        ax.set_ylim(-1, len(selected_buckets4) + 0.3)

        summary_stats['y_index'] = range(len(summary_stats))
        for index, row in summary_stats.iterrows():
          y_index = row["y_index"]
          min_val = row["min_val"]
          q25_val = row["q25_val"] - min_val
          median_val = row["median_val"] - row["q25_val"]
          q75_val = row["q75_val"] - row["median_val"]
          max_val = row["max_val"] - row["q75_val"]

          ax.barh(index, min_val, color="#233B42", label="min" if index == 0 else "")
          ax.barh(index, q25_val, left=min_val, color="#ffc48c", label="25%" if index == 0 else "")
          ax.barh(index, median_val, left=row["q25_val"], color="#ff7b28", label="median" if index == 0 else "")
          ax.barh(index, q75_val, left=row["median_val"], color="#ff506e", label="75%" if index == 0 else "")
          ax.barh(index, max_val, left=row["q75_val"], color="#d923a3", label="max" if index == 0 else "")

        ax.set_xlabel('Value')
        ax.set_ylabel('Buckets')
        ax.set_yticks(range(len(selected_buckets4)))
        ax.set_yticklabels([f"Bucket {int(b)}" for b in plot_data.index])
        ax.legend(['min', '25%', '50%', '75%', 'max'], title='Statistics')
        st.pyplot(fig)

        for bucket in selected_buckets4:
            summary_stats = filtered_data.groupby("bucket")["Total_Campaign_Cost"].describe()
            bucket_stats = summary_stats.loc[bucket]
            mean_value = bucket_stats['mean']

            st.write(f"Gauge Chart for Bucket: {bucket}")
            st.write(f"Mean of Campaign Cost: {mean_value:.0f}")

            gauge_chart = go.Figure(go.Indicator(
                mode="gauge+number",
                value=mean_value,
                title={'text': f"Bucket {bucket}: Campaign Cost Mean of {mean_value:.0f}"},

                gauge={
                    'axis': {'range': [None, bucket_stats['max']]},
                    'bar': {'color': "#233B42", 'thickness': 0.5},  # Hide the default bar
                    'steps': [
                        {'range': [0, bucket_stats['25%']], 'color': "#5ACE20"},
                        {'range': [bucket_stats['25%'], bucket_stats['50%']], 'color': "#FFFF33"},
                        {'range': [bucket_stats['50%'], bucket_stats['75%']], 'color': "#FF9A00"},
                        {'range': [bucket_stats['75%'], bucket_stats['max']], 'color': "#FF3C00"}
                    ]
                        }
            ))
            st.plotly_chart(gauge_chart)

    else:
      st.write("Please select one or more buckets to visualize the data.")


#######
# Predicted Profit Calculation
def pred_profit_calc():
    clust_0_prof = clust.loc[clust["bucket"] == 0]["predicted_profit"].iloc[0]
    clust_0_cost = clust.loc[clust["bucket"] == 0]["cost_to_acq"].iloc[0] * clust.loc[clust["bucket"] == 0]["predicted_number_of_lead"].iloc[0]
    clust_0_rev = clust.loc[clust["bucket"] == 0]["predicted_number_of_lead"].iloc[0]*25000

    clust_1_prof = clust.loc[clust["bucket"] == 1]["predicted_profit"].iloc[0]
    clust_1_cost = clust.loc[clust["bucket"] == 1]["cost_to_acq"].iloc[0] * clust.loc[clust["bucket"] == 1]["predicted_number_of_lead"].iloc[0]
    clust_1_rev =clust.loc[clust["bucket"] == 1]["predicted_number_of_lead"].iloc[0]*25000

    clust_2_prof = clust.loc[clust["bucket"] == 2]["predicted_profit"].iloc[0]
    clust_2_cost = clust.loc[clust["bucket"] == 2]["cost_to_acq"].iloc[0] * clust.loc[clust["bucket"] == 2]["predicted_number_of_lead"].iloc[0]
    clust_2_rev =clust.loc[clust["bucket"] == 2]["predicted_number_of_lead"].iloc[0]*25000

    clust_3_prof = clust.loc[clust["bucket"] == 3]["predicted_profit"].iloc[0]
    clust_3_cost = clust.loc[clust["bucket"] == 3]["cost_to_acq"].iloc[0] * clust.loc[clust["bucket"] == 3]["predicted_number_of_lead"].iloc[0]
    clust_3_rev =clust.loc[clust["bucket"] == 3]["predicted_number_of_lead"].iloc[0]*25000

    clust_4_prof = clust.loc[clust["bucket"] == 4]["predicted_profit"].iloc[0]
    clust_4_cost = clust.loc[clust["bucket"] == 4]["cost_to_acq"].iloc[0] * clust.loc[clust["bucket"] == 4]["predicted_number_of_lead"].iloc[0]
    clust_4_rev =clust.loc[clust["bucket"] == 4]["predicted_number_of_lead"].iloc[0]*25000

    pred_revenue = clust_0_rev + clust_1_rev + clust_2_rev + clust_3_rev + clust_4_rev
    pred_expense = clust_0_cost + clust_1_cost + clust_2_cost + clust_3_cost + clust_4_cost
    pred_income = clust_0_prof + clust_1_prof + clust_2_prof + clust_3_prof + clust_4_prof

    return pred_expense, pred_income, pred_revenue
pred_profit_calc()    


#######
# Treemap
def plot_treemap():
  df_m = pd.DataFrame(columns=["bucket", "Expense", "Revenue", "Profit", "Profit_check"])
  for i in range(5):
    profit = clust.loc[clust["bucket"] == i]["predicted_profit"].iloc[0]
    exp = clust.loc[clust["bucket"] == i]["cost_to_acq"].iloc[0] * clust.loc[clust["bucket"] == i]["predicted_number_of_lead"].iloc[0]
    revenue = clust.loc[clust["bucket"] == i]["predicted_number_of_lead"].iloc[0]*25000
    profit_check = 0  
    df_m.loc[i] = [i, exp, revenue, profit, profit_check]

  df_map = df_m.copy()
  df_map['bucket_label'] = "Bucket: " + df_map['bucket'].astype(str)
  df_map['profit_label'] = df_map['Profit'].apply(lambda x: f"Predicted Profit: ${x:,.0f}")
  df_map['cost_label'] = df_map['Expense'].apply(lambda x: f"Predicted Cost Acquired: ${x:,.0f}")
  df_map['custom_label'] = df_map['profit_label'] + "<br>" + df_map['cost_label']
  custom_color_scale = [(0, "#d923a3"), (0.025, "#ff506e"), (0.411, "#ff7b28"), (0.954, "#ffc48c"), (1, "#233b42")]

  fig = px.treemap(
       df_map,
       path=['bucket_label'],
       values='Profit',
       color='Profit',  
       color_continuous_scale = custom_color_scale, 
       custom_data=['custom_label']
  )

  fig.update_traces(
      texttemplate="<b>%{label}</b><br>%{customdata[0]}",
      hovertemplate="%{customdata[0]}",
      root_color= "red"
  )

  fig.update_layout(width=1500, height=600, margin=dict(t=50, l=25, r=25, b=25))
  st.plotly_chart(fig, use_container_width=True)


####### 
# Toggle
def toggle_(param):
    e, p, r = pred_profit_calc()    
    if param == "b":      
        return f'${p:,.0f}'
    elif param == "c":
        return f'${e:,.0f}' 
    else:
        return f'${r:,.0f}' 


################################################################################
# Sidebar
with st.sidebar:
  st.sidebar.image("logo_.png", use_container_width = True)
  add_selectbox = st.sidebar.multiselect(
    "**PLEASE SELECT THE TYPE OF ANALYSIS YOU'D LIKE TO REVIEW:**",
    ["Times Contacted Distribution", "Days to Respond Distribution by Bucket", "Total Campaign Cost by Bucket"])

  st.markdown(
        """
        <style>
        /* Hide the sidebar by default */
        [data-testid="stSidebar"] {
            transform: translateX(-100%);
            transition: transform 0.7s ease-in-out;
            background-color: rgb(35, 59, 66);
            color: white;
            overflow-y: auto;
        }

        /* Show the sidebar when hovering over the left edge */
        [data-testid="stAppViewContainer"]:hover [data-testid="stSidebar"],
        [data-testid="stSidebar"].expanded { /* Optional class for expanded state */
        transform: translateX(0%);
        }

        /* Add a small visible edge to hint at the sidebar */
        [data-testid="stAppViewContainer"]::before {
            content: '';
            position: fixed;
            top: 0;
            left: 0;
            width: 5px;
            height: 100%;
            background-color: rgb(35, 59, 66);
            z-index: 1000;
        }

        /* Change the color of the multiselect widget label text */
        [data-testid="stSidebar"] label {
            color: white !important;
        }

        /* Change the color of the text and background in the multiselect widget */
        [data-testid="stSidebar"] .stMultiSelect div[data-baseweb="select"] {
            color: white !important;
        }

        /* Change the dropdown options text color */
        [data-testid="stSidebar"] .stMultiSelect div[data-baseweb="select"] span {
            color: white !important;
            background-color: #ff7b28 !important;
            font-weight: bold !important;
        }

        /* Add space below the multiselect widget */
        [data-testid="stSidebar"] .stMultiSelect {
        margin-bottom: 200px; /* Add space below the multiselect widget */
        }

        </style>
        """,
        unsafe_allow_html=True,
  )

  col1, col2 = st.columns([3, 1])  
  with col1:
    # Clickable phrase styled with HTML and CSS
      st.markdown(
        """
        <style>
        .sidebar-item {
            display: flex;
            align-items: center;
            cursor: pointer;
            margin-top: 14.5px;
            background-color: transparent;
            padding: 0;
            color: white;
            font-size: 20px;
        }

        .sidebar-item .vertical-line {
            border-left: 3px solid white;
            height: 40px;
            margin-right: 10px;
            transition: all 0.3s ease;
        }

        .sidebar-item:hover .vertical-line {
            border-left: 3px solid #ff7b28;
            height: 60px;
        }

        .sidebar-item p {
            margin: 0;
            line-height: 40px;
        }

        .sidebar-item:hover p {
            font-weight: bold;
        }
        </style>
        <div class="sidebar-item" onclick="window.location.href='?link=profit_distribution'">
          <div class="vertical-line"></div>
          <p>Profit per Bucket</p>
        </div>
        """,
        unsafe_allow_html=True,
      )

  with col2:
    st.markdown(
        """
        <style>
        .stToggle div {
            display: flex;
            margin-top: 0px;
            justify-content: flex-start;
            padding: 0px;
            align-items: center; /* Align checkbox vertically */
        }

        </style>
        """,
        unsafe_allow_html=True,
    )
    a = st.toggle("", value=False, key="checkbox_1")

  col3, col4 = st.columns([3, 1]) 
  with col3:
      # Clickable phrase styled with HTML and CSS
    st.markdown(
          """
          <style>
          .sidebar-item {
              display: flex;
              align-items: center;
              cursor: pointer;
              margin-top: 14.5px;
              background-color: transparent;
              padding: 0;
              color: white;
              font-size: 20px;
          }

          .sidebar-item .vertical-line {
              border-left: 3px solid white;
              height: 40px;
              margin-right: 10px;
              transition: all 0.3s ease;
          }

          .sidebar-item:hover .vertical-line {
              border-left: 3px solid #ff7b28;
              height: 60px;
          }

          .sidebar-item p {
              margin: 0;
              line-height: 40px;
          }

          .sidebar-item:hover p {
              font-weight: bold;
          }
          </style>
          <div class="sidebar-item" onclick="window.location.href='?link=profit_distribution'">
            <div class="vertical-line"></div>
            <p>Total Profit per Acquisition Window</p>
          </div>
          """,
          unsafe_allow_html=True,
      )

  with col4:
    st.markdown(
          """
          <style>
          .stToggle div {
              display: flex;
              margin-top: 0px;
              justify-content: flex-start;
              padding: 0px;
              align-items: center; /* Align checkbox vertically */
              height: 40px; /* Matches text height */
          }
          </style>
          """,
          unsafe_allow_html=True,
    )
    b = st.toggle("", value=False, key="checkbox_2")


  col5, col6 = st.columns([3, 1]) 
  with col5:
    # Clickable phrase styled with HTML and CSS
    st.markdown(
          """
          <style>
          .sidebar-item {
              display: flex;
              align-items: center;
              cursor: pointer;
              margin-top: 14.5px;
              background-color: transparent;
              padding: 0;
              color: white;
              font-size: 20px;
          }

          .sidebar-item .vertical-line {
              border-left: 3px solid white;
              height: 40px;
              margin-right: 10px;
              transition: all 0.3s ease;
          }

          .sidebar-item:hover .vertical-line {
              border-left: 3px solid #ff7b28; 
              height: 60px;
          }

          .sidebar-item p {
              margin: 0;
              line-height: 40px;
          }

          .sidebar-item:hover p {
              font-weight: bold;
          }
          </style>
          <div class="sidebar-item" onclick="window.location.href='?link=profit_distribution'">
            <div class="vertical-line"></div>
            <p>Total Expense per Acquisition Window</p>
          </div>
          """,
          unsafe_allow_html=True,
      )

  with col6:
    st.markdown(
        """
        <style>
        .stToggle div {
            display: flex;
            margin-top: 0px;
            justify-content: flex-start;
            padding: 0px;
            align-items: center; /* Align checkbox vertically */
        }

        </style>
        """,
        unsafe_allow_html=True,
    )
    c = st.toggle("", value=False, key="checkbox_3")

  col7, col8 = st.columns([3, 1])  
  with col7:
    # Clickable phrase styled with HTML and CSS
    st.markdown(
          """
          <style>
          .sidebar-item {
              display: flex;
              align-items: center;
              cursor: pointer;
              margin-top: 14.5px;
              background-color: transparent;
              padding: 0;
              color: white;
              font-size: 20px;
          }

          .sidebar-item .vertical-line {
              border-left: 3px solid white;
              height: 40px;
              margin-right: 10px;
              transition: all 0.3s ease;
          }

          .sidebar-item:hover .vertical-line {
              border-left: 3px solid #ff7b28;
              height: 60px;
          }

          .sidebar-item p {
              margin: 0;
              line-height: 40px;
          }

          .sidebar-item:hover p {
              font-weight: bold;
          }
          </style>
          <div class="sidebar-item" onclick="window.location.href='?link=profit_distribution'">
            <div class="vertical-line"></div>
            <p>Total Revenue per Acquisition Window</p>
          </div>
          """,
          unsafe_allow_html=True,
      )

  with col8:
    st.markdown(
        """
        <style>
        .stToggle div {
            display: flex;
            margin-top: 0px;
            justify-content: flex-start;
            padding: 0px;
            align-items: center; /* Align checkbox vertically */
        }

        </style>
        """,
        unsafe_allow_html=True,
    )
    d = st.toggle("", value=False, key="checkbox_4")

if a:
  plot_treemap()

if b:
  total_profit = toggle_("b")
  st.markdown(f'<div class="info-box">Total Profit: {total_profit}</div>', unsafe_allow_html=True)

if c:
  total_exp = toggle_("c")
  st.markdown(f'<div class="info-box">Total Cost: {total_exp}</div>', unsafe_allow_html=True)

if d:
  total_revenue = toggle_("d")
  st.markdown(f'<div class="info-box">Total Revenue: {total_revenue}</div>', unsafe_allow_html=True)

st.markdown(
    """
    <style>
    .info-box {
        background-color: #233B42; /* Blue background */
        color: white; /* White text color */
        border-radius: 10px; /* Rounded edges */
        padding: 20px; /* Padding inside the box */
        text-align: center; /* Center align text */
        font-size: 20px; /* Font size */
        font-weight: bold; /* Bold text */
        box-shadow: 5px 5px 9px rgba( 217, 35, 163, 0.5); /* Subtle shadow */
        width: 300px;
        margin-bottom: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

analysis_functions = {
    "Times Contacted Distribution": times_contacted_distribution, "Days to Respond Distribution by Bucket": days_distribution, "Total Campaign Cost by Bucket": cost_ditribution}

for analysis in add_selectbox:
    analysis_functions[analysis]()

st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background-color: #F0F0F0;
        color: #333;
        text-align: center;
        padding: 15px;
        font-size: 14px;
        border-top: 1px solid #ccc;
    }
    </style>
    <div class="footer">
        &copy; 2025 Copyright: Christina Trowbridge. All rights reserved.
    </div>
    """,
    unsafe_allow_html=True
)
