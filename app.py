import streamlit as st
import google.generativeai as genai
from apikey import goggleapikey


genai.configure(api_key=goggleapikey)
model = genai.GenerativeModel(
  model_name="gemini-pro",
  )

def main():
    st.set_page_config(page_title="SQL Query Generator ",page_icon=":robot:")

    st.markdown(
        """
        <div style="text-align: center; ">
        <h1>SQL Query Generator 🤖 ⁉️ 👨🏻‍💻 </h1>

        <h3>I can generate SQL queries for you </h3>
        <h4>With explanation as well.</h4>
        <p>This tool helps you to generate sql queries based on the prompts you give. </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    text_input= st.text_area("Enter your prompt here in plain english:")
    
    
    submit=st.button("Generate SQL Query")

    if submit:
        with st.spinner("generating SQl Query..."):
            template="""
                Creating an SQL query snippet using the below text here:
                ```
                    {text_input}
                ```
            """

            formatted_template=template.format(text_input=text_input)
            response=model.generate_content(formatted_template)
            # st.write(formatted_template)
            sql_query=response.text
            # st.write(sql_query)


            expexted_output="""
                What would be the expected output for this sql query looks like after running it :
                ```
                {sql_query}
                ```
                Provide sampler tabel response with no explanation
                
            """

            expected_output_formatted=expexted_output.format(sql_query=sql_query)
            expected_output_response=model.generate_content(expected_output_formatted)
            # st.write(expected_output_response)
            expected_output_sql_query=expected_output_response.text
            # st.write(expected_output_sql_query)

            with st.container():
                st.success("SQL Querry Generated Successfully! Here's your query below: ") 
                st.code(sql_query,language="sql")
                st.success("Expected output of this SQL query looks like this: ")
                st.markdown(expected_output_sql_query)
        


        # response=model.generate_content(text_input)
        # print(response.text)
        # st.write(response.text)

main()