import streamlit as st
from rapidfuzz import process, fuzz
import re

st.set_page_config(
    page_title="Dari Text Search System",
    page_icon="🔍",
    layout="centered"
)

st.title("Dari Text Search System")
st.write("A simple text search system using Fuzzy Matching and n-gram analysis.")

THRESHOLD = 80

def load_dataset(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()

    # Extract Dari/Persian words only
    words = re.findall(r'[\u0600-\u06FF]+', text)

    # Remove repeated words and sort them
    unique_words = sorted(set(words))
    return unique_words

def generate_bigrams(word):
    if len(word) < 2:
        return []
    return [word[i:i+2] for i in range(len(word)-1)]

words = load_dataset("final_dataset.txt")

query = st.text_input("Enter a Dari word:")

if st.button("Search"):
    query = query.strip()

    if query == "":
        st.warning("Please enter a word.")
    else:
        result = process.extractOne(query, words, scorer=fuzz.ratio)

        if result:
            matched_word, score, _ = result

            st.subheader("Search Result")
            st.write(f"Input word: {query}")

            if score >= THRESHOLD:
                st.success("Result found / Acceptable match")
                st.write(f"Closest matching word: {matched_word}")
                st.write(f"Similarity score: {score:.2f}%")

                input_bigrams = generate_bigrams(query)
                output_bigrams = generate_bigrams(matched_word)
                common_bigrams = set(input_bigrams).intersection(set(output_bigrams))

                st.subheader("n-gram Analysis")
                st.write(f"Input bigrams: {input_bigrams}")
                st.write(f"Matched word bigrams: {output_bigrams}")
                st.write(f"Common bigrams: {list(common_bigrams)}")
                st.write(f"Number of common bigrams: {len(common_bigrams)}")

                st.success("Evaluation: Correct / Acceptable")
            else:
                st.error("No suitable result found")
                st.write(f"Highest similarity score: {score:.2f}%")
                st.write("Evaluation: Not suitable")

                input_bigrams = generate_bigrams(query)
                output_bigrams = generate_bigrams(matched_word)
                common_bigrams = set(input_bigrams).intersection(set(output_bigrams))

                st.subheader("n-gram Analysis")
                st.write(f"Input bigrams: {input_bigrams}")
                st.write(f"Nearest but rejected word: {matched_word}")
                st.write(f"Rejected word bigrams: {output_bigrams}")
                st.write(f"Common bigrams: {list(common_bigrams)}")
                st.write(f"Number of common bigrams: {len(common_bigrams)}")