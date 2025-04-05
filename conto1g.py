import requests
import streamlit as st

st.title("Gold Price Checker 💰")

api_key = "5c1e67f4f4d16f411fc46eb60cce18fd"
url = f"https://api.metalpriceapi.com/v1/latest?api_key={api_key}&base=USD&currencies=XAU"

response = requests.get(url)
data = response.json()

if response.status_code == 200 and "rates" in data and "XAU" in data["rates"]:
    price_per_ounce = 1 / data["rates"]["XAU"]
    price_per_gram_24k = price_per_ounce / 31.1035
    price_per_gram_18k = price_per_gram_24k * 0.75

    st.success(f"24K Gold (1g): ${price_per_gram_24k:.2f}")
    st.success(f"18K Gold (1g): ${price_per_gram_18k:.2f}")
else:
    st.error("Failed to retrieve gold price.")
