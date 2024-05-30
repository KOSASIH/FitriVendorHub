import os
from langchain import OpenAI, SQLDatabase
from langchain.chains import SQLDatabaseSequentialChain

os.environ['OPENAI_API_KEY'] = "****"

dburi = 'qlite:///db'
db = SQLDatabase.from_uri(dburi)

llm = OpenAI(temperature=0)
db_chain = SQLDatabaseSequentialChain(llm=llm, database=db, verbose=True)

def query_fn(input_text):
    response = db_chain.run(input_text)
    return response

iface = gr.Interface(
    fn=query_fn,
    inputs=gr.inputs.Textbox(label="Enter your query"),
    outputs=gr.outputs.Textbox(label="Query Result"),
    title="Chatbot"
)

iface.launch(share=False, server_port=8080)
