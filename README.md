# SQL Query Generator with Explanation

This is a Streamlit application that generates SQL queries based on user prompts using Google's Generative AI (Gemini-1.5-pro). The application not only generates the SQL query but also provides the expected output and a simple explanation of the query.

## Features

- Generate SQL queries based on text input
- Provide expected output of the generated SQL query
- Explain the generated SQL query in simple terms
- Download the generated query, expected output, and explanation as a `.sql` file

## Installation

### Prerequisites

- Python 3.7 or higher
- Streamlit
- Google Generative AI Python client library (`google-generativeai`)

### Steps

1. **Clone the repository**:

    ```bash
    git clone https://github.com/sonagara-vashram/SQL_bot.git
    ```

2. **Install the required packages**:

    ```bash
    pip install -r requirements.txt
    ```

3. **Set up your Google API key**:

    ```bash
    export GOOGLE_API_KEY='your_google_api_key'
    ```

4. **Run the Streamlit app**:

    ```bash
    streamlit run app.py
    ```

## Usage

1. Enter your query prompt in the text area.
2. Click the "Generate SQL Query" button.
3. Wait for the SQL query, expected output, and explanation to be generated.
4. View the generated SQL query, expected output, and explanation on the web page.
5. Download the details as a `.sql` file if needed.
