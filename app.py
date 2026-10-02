import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os
import plotly.express as px
import plotly.graph_objects as go

# Page Config
st.set_page_config(
    page_title="Smart Property Assistant",
    page_icon="H",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        padding: 1rem;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    .metric-card {
        background: #f0f2f6;
        padding: 1.5rem;
        border-radius: 10px;
        text-align: center;
        border-left: 5px solid #667eea;
    }
    .stButton>button {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 25px;
        padding: 0.5rem 2rem;
        font-weight: bold;
        border: none;
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #764ba2 0%, #667eea 100%);
        transform: scale(1.05);
    }
</style>
""", unsafe_allow_html=True)

# Load Models
@st.cache_resource
def load_models():
    with open("city_models.pkl", "rb") as f:
        city_models = pickle.load(f)
    with open("city_features.pkl", "rb") as f:
        city_features = pickle.load(f)
    with open("locations.pkl", "rb") as f:
        locations = pickle.load(f)
    return city_models, city_features, locations

@st.cache_data
def load_data():
    return pd.read_csv("cleaned_data.csv")

city_models, city_features, locations = load_models()
df = load_data()

# Header
st.markdown('<div class="main-header"><h1>Smart Property Assistant - India</h1><p>AI-Powered House Price Prediction for 6 Major Indian Cities</p></div>', unsafe_allow_html=True)

# Sidebar
st.sidebar.markdown("## Navigation")
page = st.sidebar.radio("", [
    "Home Dashboard",
    "Price Predictor",
    "EMI Calculator",
    "Buy vs Rent",
    "City Comparison",
    "Market Insights",
    "About"
])

st.sidebar.markdown("---")
st.sidebar.markdown("### Quick Stats")
st.sidebar.metric("Total Properties", f"{len(df):,}")
st.sidebar.metric("Cities Covered", df["City"].nunique())
st.sidebar.metric("Avg Price", f"Rs {df['Price'].mean()/100000:.1f} L")

# ============================================
# PAGE 1: HOME DASHBOARD
# ============================================
if page == "Home Dashboard":
    st.header("Dashboard Overview")
    
    # KPIs
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Properties", f"{len(df):,}", "6 Cities")
    with col2:
        st.metric("Avg Price", f"Rs {df['Price'].mean()/100000:.1f}L", "Nationwide")
    with col3:
        st.metric("Highest Price", f"Rs {df['Price'].max()/10000000:.1f}Cr", "Premium")
    with col4:
        st.metric("Locations", f"{df['Location'].nunique()}", "Unique areas")
    
    st.markdown("---")
    
    # Charts Row 1
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Properties by City")
        city_counts = df["City"].value_counts()
        fig = px.pie(values=city_counts.values, names=city_counts.index, 
                     color_discrete_sequence=px.colors.qualitative.Set3,
                     hole=0.4)
        fig.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("Average Price by City")
        city_avg = df.groupby("City")["Price"].mean().sort_values(ascending=True) / 100000
        fig = px.bar(x=city_avg.values, y=city_avg.index, orientation="h",
                     labels={"x": "Price (Lakhs)", "y": "City"},
                     color=city_avg.values, color_continuous_scale="Viridis")
        fig.update_layout(showlegend=False)
        st.plotly_chart(fig, use_container_width=True)
    
    # Price Distribution
    st.subheader("Price Distribution Across Cities")
    fig = px.box(df, x="City", y="Price", color="City",
                 labels={"Price": "Price (Rs)"})
    fig.update_yaxes(range=[0, df["Price"].quantile(0.95)])
    st.plotly_chart(fig, use_container_width=True)

# ============================================
# PAGE 2: PRICE PREDICTOR
# ============================================
elif page == "Price Predictor":
    st.header("AI Price Predictor")
    st.markdown("Get instant price prediction using our ML model")
    
    col1, col2 = st.columns(2)
    with col1:
        city = st.selectbox("Select City", list(city_models.keys()))
        location = st.selectbox("Select Location", locations[city])
    with col2:
        bhk = st.selectbox("BHK Configuration", [1, 2, 3, 4, 5, 6])
        sqft = st.number_input("Area (Sqft)", min_value=300, max_value=10000, value=1000, step=50)
    
    if st.button("Predict Price Now", use_container_width=True):
        try:
            features = city_features[city]
            x = np.zeros(len(features))
            if "Sqft" in features:
                x[features.index("Sqft")] = sqft
            if "BHK" in features:
                x[features.index("BHK")] = bhk
            loc_col = "Location_" + location
            if loc_col in features:
                x[features.index(loc_col)] = 1
            
            model = city_models[city]
            pred_log = model.predict([x])[0]
            price = np.expm1(pred_log)
            
            st.markdown("---")
            st.success(f"### Predicted Price: Rs {price:,.0f}")
            
            col_a, col_b, col_c = st.columns(3)
            with col_a:
                st.metric("Price in Lakhs", f"Rs {price/100000:.2f} L")
            with col_b:
                st.metric("Price per Sqft", f"Rs {price/sqft:,.0f}")
            with col_c:
                st.metric("Price in Crores", f"Rs {price/10000000:.2f} Cr")
            
            # Comparison with city average
            city_data = df[df["City"] == city]
            city_avg = city_data["Price"].mean()
            diff = ((price - city_avg) / city_avg) * 100
            
            st.markdown("### Market Comparison")
            col_x, col_y = st.columns(2)
            with col_x:
                st.metric(f"{city} Average", f"Rs {city_avg/100000:.1f} L")
            with col_y:
                st.metric("Your Property", f"Rs {price/100000:.1f} L", f"{diff:+.1f}%")
            
        except Exception as e:
            st.error("Error: " + str(e))

# ============================================
# PAGE 3: EMI CALCULATOR
# ============================================
elif page == "EMI Calculator":
    st.header("Home Loan EMI Calculator")
    
    col1, col2 = st.columns(2)
    with col1:
        loan_amount = st.number_input("Loan Amount (Rs)", min_value=100000, value=5000000, step=100000)
        interest_rate = st.slider("Interest Rate (%)", 5.0, 15.0, 8.5, 0.1)
    with col2:
        tenure_years = st.slider("Tenure (Years)", 1, 30, 20)
    
    if st.button("Calculate EMI", use_container_width=True):
        monthly_rate = interest_rate / 12 / 100
        months = tenure_years * 12
        emi = (loan_amount * monthly_rate * (1 + monthly_rate)**months) / ((1 + monthly_rate)**months - 1)
        total_payment = emi * months
        total_interest = total_payment - loan_amount
        
        col_a, col_b, col_c = st.columns(3)
        with col_a:
            st.metric("Monthly EMI", f"Rs {emi:,.0f}")
        with col_b:
            st.metric("Total Payment", f"Rs {total_payment:,.0f}")
        with col_c:
            st.metric("Total Interest", f"Rs {total_interest:,.0f}")
        
        # Pie Chart
        fig = go.Figure(data=[go.Pie(
            labels=["Principal", "Interest"],
            values=[loan_amount, total_interest],
            hole=.4,
            marker_colors=["#667eea", "#764ba2"]
        )])
        fig.update_layout(title="Loan Breakdown")
        st.plotly_chart(fig, use_container_width=True)

# ============================================
# PAGE 4: BUY VS RENT
# ============================================
elif page == "Buy vs Rent":
    st.header("Buy vs Rent Calculator")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Buying")
        house_price = st.number_input("House Price (Rs)", min_value=1000000, value=8000000)
        down_payment = st.slider("Down Payment (%)", 10, 50, 20)
        loan_rate = st.slider("Loan Interest (%)", 5.0, 15.0, 8.5)
        loan_years = st.slider("Loan Tenure (Years)", 5, 30, 20)
    with col2:
        st.subheader("Renting")
        monthly_rent = st.number_input("Monthly Rent (Rs)", min_value=5000, value=25000)
        rent_hike = st.slider("Annual Rent Hike (%)", 0, 15, 7)
        stay_years = st.slider("Years of Stay", 1, 30, 10)
    
    if st.button("Compare Now", use_container_width=True):
        down_amt = house_price * down_payment / 100
        loan_amt = house_price - down_amt
        monthly_rate = loan_rate / 12 / 100
        months = loan_years * 12
        emi = (loan_amt * monthly_rate * (1 + monthly_rate)**months) / ((1 + monthly_rate)**months - 1)
        total_buy = down_amt + (emi * min(stay_years * 12, months))
        
        total_rent = 0
        current_rent = monthly_rent
        for year in range(stay_years):
            total_rent += current_rent * 12
            current_rent *= (1 + rent_hike/100)
        
        col_a, col_b = st.columns(2)
        with col_a:
            st.metric("Total Buying Cost", f"Rs {total_buy:,.0f}")
            st.metric("Monthly EMI", f"Rs {emi:,.0f}")
        with col_b:
            st.metric("Total Renting Cost", f"Rs {total_rent:,.0f}")
            st.metric("Down Payment", f"Rs {down_amt:,.0f}")
        
        if total_buy < total_rent:
            savings = total_rent - total_buy
            st.success(f"BUYING is better! You save Rs {savings:,.0f}")
        else:
            savings = total_buy - total_rent
            st.info(f"RENTING is better! You save Rs {savings:,.0f}")
        
        # Comparison chart
        fig = go.Figure(data=[
            go.Bar(name="Buying", x=["Cost"], y=[total_buy], marker_color="#667eea"),
            go.Bar(name="Renting", x=["Cost"], y=[total_rent], marker_color="#764ba2")
        ])
        fig.update_layout(title="Cost Comparison", yaxis_title="Amount (Rs)")
        st.plotly_chart(fig, use_container_width=True)

# ============================================
# PAGE 5: CITY COMPARISON
# ============================================
elif page == "City Comparison":
    st.header("Compare Cities")
    
    selected_cities = st.multiselect("Select Cities to Compare", 
                                       df["City"].unique().tolist(),
                                       default=df["City"].unique().tolist()[:3])
    
    if selected_cities:
        filtered_df = df[df["City"].isin(selected_cities)]
        
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Average Price")
            avg_price = filtered_df.groupby("City")["Price"].mean() / 100000
            fig = px.bar(x=avg_price.index, y=avg_price.values,
                        labels={"x": "City", "y": "Avg Price (Lakhs)"},
                        color=avg_price.values, color_continuous_scale="Bluered")
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.subheader("Price per Sqft")
            filtered_df["PPS"] = filtered_df["Price"] / filtered_df["Sqft"]
            pps = filtered_df.groupby("City")["PPS"].mean()
            fig = px.bar(x=pps.index, y=pps.values,
                        labels={"x": "City", "y": "Price per Sqft (Rs)"},
                        color=pps.values, color_continuous_scale="Viridis")
            st.plotly_chart(fig, use_container_width=True)
        
        # Detailed Table
        st.subheader("Detailed Statistics")
        stats = filtered_df.groupby("City").agg({
            "Price": ["mean", "median", "min", "max"],
            "Sqft": "mean"
        }).round(0)
        st.dataframe(stats, use_container_width=True)

# ============================================
# PAGE 6: MARKET INSIGHTS
# ============================================
elif page == "Market Insights":
    st.header("Market Insights")
    
    city_filter = st.selectbox("Select City for Analysis", df["City"].unique())
    city_df = df[df["City"] == city_filter]
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Avg Price", f"Rs {city_df['Price'].mean()/100000:.1f} L")
    with col2:
        st.metric("Properties", f"{len(city_df):,}")
    with col3:
        st.metric("Locations", city_df["Location"].nunique())
    
    # Top 10 Expensive Locations
    st.subheader(f"Top 10 Expensive Locations in {city_filter}")
    top_loc = city_df.groupby("Location")["Price"].mean().nlargest(10) / 100000
    fig = px.bar(x=top_loc.values, y=top_loc.index, orientation="h",
                 labels={"x": "Avg Price (Lakhs)", "y": "Location"},
                 color=top_loc.values, color_continuous_scale="Reds")
    st.plotly_chart(fig, use_container_width=True)
    
    # BHK Distribution
    st.subheader("BHK Distribution")
    bhk_counts = city_df[city_df["BHK"] <= 6]["BHK"].value_counts().sort_index()
    fig = px.pie(values=bhk_counts.values, names=[f"{i} BHK" for i in bhk_counts.index])
    st.plotly_chart(fig, use_container_width=True)

# ============================================
# PAGE 7: ABOUT
# ============================================
else:
    st.header("About This Project")
    
    st.markdown("""
    ## Smart Property Assistant - India
    
    An AI-powered web application for house price prediction across 6 major Indian cities.
    
    ### Features
    - **Price Predictor**: ML-based price predictions
    - **EMI Calculator**: Home loan calculations
    - **Buy vs Rent**: Financial comparison tool
    - **City Comparison**: Compare multiple cities
    - **Market Insights**: Location-wise analysis
    
    ### Cities Covered
    Bangalore, Mumbai, Delhi, Chennai, Hyderabad, Kolkata
    
    ### Technology Stack
    - **ML**: Scikit-learn, Random Forest
    - **Web**: Streamlit
    - **Visualization**: Plotly
    - **Data**: Pandas, NumPy
    
    ### Data Source
    Kaggle - Housing Prices in Metropolitan Areas of India
    
    ### Developer
    **Manish Kumar**
    """)

# Footer
st.markdown("---")
st.markdown("<center>Made with Streamlit | Smart Property Assistant</center>", unsafe_allow_html=True)
