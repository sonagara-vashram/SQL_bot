import streamlit as st
import google.generativeai as genai
import os

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
)

def main():
    st.set_page_config(page_title="Sql Query Generation", page_icon=":robot:")
    st.markdown(
        """
        <div style="text-align: center;">
            <h1> SQL Query Generator </h1>
            <h1> With Explaination as Well !!</h1>
            <p> This tool is generate sql query based on your prompt. </p>
        </div>
        """,
        unsafe_allow_html=True
    )
    text_input = st.text_area("Enter your query here : ") 
    
    submit = st.button('Generate SQL Query')
    if submit:
        with st.spinner('Generate SQL query...'):
            template="""
                Create a SQL query snippet using the below text:

                ```
                    {text_input}
                ```
                I just want SQL Query.
            
            """
            formatted_tempalte = template.format(text_input=text_input)
            response = model.generate_content(formatted_tempalte)
            sql_query = response.text
            
            sql_query = sql_query.strip().lstrip("```sql").rstrip("```")
    
            expected_output="""
                What would be the expected response of this sql query snippet:
                
                    ```
                        {sql_query}
                    ```
                Provide simple tabular response with no explaination.
            
            """
            expected_output_formatted = expected_output.format(sql_query=sql_query)
            eoutput = model.generate_content(expected_output_formatted)
            eoutput = eoutput.text
            
            explaination="""
                Explain This sql Query:
                
                    ```
                        {sql_query}
                    ```
              Please Provide with simplest of explaination.
            
            """
            
            # Combine all output into a single string for download
            downloadable_content = f"""
                ## SQL Query:
                ```sql
                {sql_query}
                ```

                ## Expected Output:
                {eoutput}

                ## Explanation:
                {explaination}
                """
            explaination_formatted = explaination.format(sql_query=sql_query)
            explaination = model.generate_content(explaination_formatted)
            explaination = explaination.text
            
            with st.container():
                st.success('SQL Query generated successfully! Here is your quesry Below:')
                st.code(sql_query, language='sql')

                st.success('Expected output : ')
                st.markdown(eoutput)
                
                st.success('Explaination : ')
                st.markdown(explaination)
                
                st.download_button(
                    label="Download All Details",
                    data=downloadable_content,
                    file_name="sql_query_details.sql",
                )
            
main()