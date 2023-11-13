from langchain.chat_models import ChatOpenAI
from langchain.agents import AgentType, initialize_agent
from langchain.tools import tool
import os
import pinecone
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores.pinecone import Pinecone


@tool("SayHello", return_direct=True)
def say_hello(name: str) -> str:
    """ Answer when someone says hello"""
    return f"Hello {name}! My name is Sainapsis"


def main():
    llm = ChatOpenAI(temperature=0)
    tools = [
        say_hello
    ]
    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent = AgentType.OPENAI_FUNCTIONS,
        verbose = True
    )
    print(agent.run("Hello! My name is David"))

    pinecone.init(api_key='4b6859ea-ff56-42a3-a9c2-034a2410e407', environment='gcp-starter')
    embeddings = OpenAIEmbeddings()
    text = open("economia.txt", "r")
    # print(text.read())
    pinecone.create_index("sainapsis", dimension=1536, metric="cosine")
    data = Pinecone.from_texts(texts=text.readlines(), embedding=embeddings, index_name='sainapsis')
    text = open("ingenieria-civil.txt", "r")
    data = Pinecone.from_texts(texts=text.readlines(), embedding=embeddings, index_name='sainapsis')
    text = open("ingenieria-sistemas.txt", "r")
    data = Pinecone.from_texts(texts=text.readlines(), embedding=embeddings, index_name='sainapsis')
    text = open("ingenieria-electrica.txt", "r")
    data = Pinecone.from_texts(texts=text.readlines(), embedding=embeddings, index_name='sainapsis')
    text = open("ingenieria-industrial.txt", "r")
    data = Pinecone.from_texts(texts=text.readlines(), embedding=embeddings, index_name='sainapsis')

main()

def buscar():
    pinecone.init(api_key='4b6859ea-ff56-42a3-a9c2-034a2410e407', environment='gcp-starter')
    embeddings = OpenAIEmbeddings()
    # if you already have an index, you can load it like this
    docsearch = Pinecone.from_existing_index("sainapsis", embeddings)
    query = "Cuantos años de acreditación tiene ingeniería de industrial?"
    docs = docsearch.similarity_search(query)
    print(docs)


