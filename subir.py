import os



import pinecone
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores.pinecone import Pinecone




def main():
    pinecone.init(api_key=os.getenv('PINECONE_API_KEY'), environment=os.getenv('PINECONE_ENVIRONMENT'))

    embeddings = OpenAIEmbeddings()
    text = <LoadTextFromFile>
    data = Pinecone.from_texts(texts=[text], embedding=embeddings, index_name= <YourIndexName>)


if __name__ == "__main__":
    main()