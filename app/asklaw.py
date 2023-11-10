import streamlit as st
import query
import time
import asyncio

def validate_query(input_data):
    # Add your data validation logic here
    # For example, check if the input_data is not empty
    if not input_data:
        st.error("Input cannot be empty.")
        return False
    else:
        return True
st.title("AskLAW: An AI based research assistive tool")
st.text_input("What is your Question", key="query")
if st.button('Answer'):
    if validate_query(st.session_state.query):
        st.success("Query is valid. Performing search...")
        response, status = query.streamlit_query(st.session_state.query)
        r_dict = response.json()
        summary = r_dict['responseSet'][0]['summary'][0]['text']
        documents = r_dict['responseSet'][0]['document']
        results = r_dict['responseSet'][0]['response']
        st.write(f'SUMMARY:{summary}')
        for result in results:
            document_no = result['documentIndex']
            document = documents[document_no]
            st.write(f"## **Reference: {int(document_no)+1}**")
            st.write(result['text'], unsafe_allow_html=True)
            my_expander = st.expander(label='Expand me')

            with my_expander:
                title = document['metadata'][4].get('value', "")
                url = document['metadata'][1].get('value', '')
                court = document['metadata'][0].get('value', "")
                st.write(f'Title:{title}')
                st.write(f'Court:{court}')
                st.write(f'URL: {url}')


# latest_iteration = st.empty()
# bar = st.progress(0)

# async 
# for i in range(10):
#   # Update the progress bar with each iteration.
#   latest_iteration.text(f'Iteration {i+1}')
#   bar.progress(i + 1)
#   time.sleep(0.1)
