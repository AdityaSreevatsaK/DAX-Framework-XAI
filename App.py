import streamlit as st

from DAX_Selector import dax_xai_selector  # Import logic from your existing file

st.title("🧠 DAX XAI Method Selector")
st.subheader("Domain-Aligned Explainability Tool")

# --- User Inputs ---
data_type = st.selectbox("Select your data type:", ["Tabular", "Text", "Image"])
has_legal_constraints = st.checkbox("Does your domain have strong legal/safety constraints?")

# Initialize all options as False
needs_token_level = False
needs_spatial_localization = False

# Dynamically show relevant secondary options
if data_type == "Text":
    needs_token_level = st.checkbox("Do you need token-level explanations?", key="token_checkbox")

elif data_type == "Image":
    needs_spatial_localization = st.checkbox("Do you need spatial localization of features?", key="spatial_checkbox")

elif data_type == "Tabular":
    st.info("No additional input needed for tabular data.")

# --- Display Recommendation ---
if st.button("Recommend XAI Methods"):
    methods = dax_xai_selector(
        data_type=data_type,
        has_legal_constraints=has_legal_constraints,
        needs_token_level=needs_token_level,
        needs_spatial_localization=needs_spatial_localization
    )

    st.success("✅ Recommended XAI methods for your context:")
    for method, score in methods:
        st.write(f"- {method} (Score: {score})")

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; font-size: 0.9em;'>"
    "Built with ❤️ for responsible AI by "
    "<a href='https://www.linkedin.com/in/adityasreevatsak/' target='_blank' "
    "style='text-decoration: underline; color: #A0C878; font-weight: 600;'>"
    "Aditya Sreevatsa K</a> &nbsp;|&nbsp; © 2025"
    "</div>",
    unsafe_allow_html=True
)
