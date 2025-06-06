import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Bill Calculator", layout="centered")

st.title("🧾 Bill Management System")

# Input for number of members
num_members = st.number_input("Enter number of members:", min_value=1, step=1)

# Input for bill amount and date range
bill_amount = st.number_input("Enter total bill amount (₹):", min_value=0.0, format="%.2f")
start_date = st.date_input("Start Date")
end_date = st.date_input("End Date")

# Calculate total days
total_days = (end_date - start_date).days + 1
st.write(f"📅 Total Days: {total_days}")

# Create member inputs dynamically
st.subheader("Enter Member Details:")
members = []
for i in range(num_members):
    col1, col2 = st.columns([2, 1])
    with col1:
        name = st.text_input(f"Member {i+1} Name", key=f"name_{i}")
    with col2:
        days_stayed = st.number_input(f"Days Stayed", min_value=0, key=f"days_{i}")
    members.append((name, days_stayed))

# Calculate button
if st.button("Calculate Bill"):
    if not all(name.strip() for name, _ in members):
        st.error("⚠️ All member names must be filled in.")
    elif total_days <= 0:
        st.error("⚠️ End date must be after start date.")
    elif bill_amount <= 0:
        st.error("⚠️ Please enter a valid bill amount.")
    else:
        total_stay_days = sum(days for _, days in members)
        if total_stay_days == 0:
            st.error("⚠️ Total stay days cannot be 0.")
        else:
            st.success("✅ Bill Calculated Successfully")
            st.markdown("---")
            st.subheader("📊 Bill Distribution:")
            st.write(f"**Total Bill:** ₹{bill_amount:.2f}")
            st.write(f"**Total Stay Days (All Members):** {total_stay_days}")
            st.markdown("### Member-wise Share")
            for name, days in members:
                share = round((days / total_stay_days) * bill_amount, 2)
                st.write(f"**{name}**: ₹{share:.2f} for {days} days")

