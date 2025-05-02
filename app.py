import streamlit as st

# Replace with your actual Amazon Associate Tag
PARTNER_TAG = "giftgenie0d-21"

def generate_link(query):
    q = query.replace(" ", "+")
    return f"https://www.amazon.de/s?k={q}&tag={PARTNER_TAG}"

def main():
    st.set_page_config(page_title="GiftGenie Simple", layout="centered")
    st.title("🎁 GiftGenie Simple - Gift Suggestions")
    st.write("Select your preferences and get gift ideas with Amazon links!")

    occasion = st.selectbox("What's the occasion?", ["Birthday", "Valentine's Day", "Christmas", "Anniversary", "Other"])
    recipient = st.text_input("Who is the gift for?", "e.g., Partner, Friend, Parent")
    budget = st.slider("Max budget (€)", 10, 500, 50)
    interests = st.text_input("Interests or hobbies (comma-separated)", "e.g., cooking, gaming")

    if st.button("Get Gift Links"):
        st.subheader("Here are some gift ideas:")
        terms = []
        for interest in interests.split(","):
            term = f"{occasion} {interest.strip()} gift for {recipient} under {budget} euro"
            terms.append(term)
        terms.append(f"{occasion} gift for {recipient} under {budget} euro")
        # Remove duplicates
        terms = list(dict.fromkeys(terms))
        for term in terms:
            link = generate_link(term)
            st.markdown(f"- [{term.title()}]({link})")

if __name__ == "__main__":
    main()