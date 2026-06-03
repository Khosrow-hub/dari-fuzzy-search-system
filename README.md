# Dari Text Search System

A simple Dari text search system developed using Fuzzy Matching and Bigram (n-gram) analysis. The system is designed to identify and retrieve the closest matching Dari word even when the user enters an incomplete or misspelled query.

## Overview

This project provides an interactive search interface built with Streamlit. Users can enter a Dari word, and the system searches a text dataset to find the closest matching word using Fuzzy Matching techniques. The retrieved result is then analyzed using character-level Bigram analysis to examine structural similarity between the input and the matched word.

The system is intended as an educational and research prototype for studying typo-tolerant text retrieval in the Dari language.

## Features

* Interactive web interface using Streamlit
* Fuzzy Matching using RapidFuzz
* Character-level Bigram (n-gram) analysis
* Similarity score calculation
* Threshold-based result evaluation
* Detection of incomplete and misspelled words
* Automatic extraction of Dari words from a text dataset

## Technologies Used

* Python
* Streamlit
* RapidFuzz
* Regular Expressions (Regex)

## Project Structure

```text
dari-text-search-system/
│
├── app.py
├── final_dataset.txt
├── requirements.txt
└── README.md
```

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Khosrow-hub/dari-fuzzy-search-system.git
```

### 2. Navigate to the Project Folder

```bash
cd dari-text-search-system
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
streamlit run app.py
```

## How It Works

1. The dataset is loaded from a text file.
2. Dari words are extracted using regular expressions.
3. Duplicate words are removed automatically.
4. The user enters a search query.
5. RapidFuzz calculates similarity scores.
6. The closest matching word is retrieved.
7. Character-level Bigram analysis is performed.
8. Results are evaluated using a similarity threshold of 80%.
9. The system displays the matching result, similarity score, and Bigram analysis.

## Example

### Input Query

```text
دانسگا
```

### Retrieved Result

```text
دانشگاه
```

### Similarity Score

```text
85.71%
```

### Evaluation

```text
Accepted
```

## Contributors

This project was developed collaboratively by:

* Ahmad Ali Yaqin
* Abdulrahman Rahimi
* Khosrow Samadi

## Academic Purpose

This project was developed for academic and research purposes to demonstrate typo-tolerant Dari text retrieval using Fuzzy Matching and Bigram analysis techniques.

## License

This project is intended for educational and research use.
