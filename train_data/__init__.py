import os
from dotenv import load_dotenv
import glob
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.text_splitter import TokenTextSplitter
from langchain.chat_models import ChatOpenAI
from langchain.chains import ChatVectorDBChain
from langchain.document_loaders import DirectoryLoader
from langchain.docstore.document import Document
from typing import List
import jieba as jb


load_dotenv()
if not os.path.exists('./db'):
    os.mkdir('./db')

openai_api_key = os.getenv("OPENAI_API_KEY")


def init_cut_file() -> None:
    # You can use any path you want
    file_list = glob.glob('./data/*')
    for file_path in file_list:
        if file_path.endswith("txt") or file_path.endswith("md"):
            with open(file_path, "r", encoding='utf-8') as f:
                data = f.read()
        else:
            data = ''

        cut_data = " ".join([w for w in list(jb.cut(data))])
        file_name_with_ext = os.path.basename(file_path)
        file_name = os.path.splitext(file_name_with_ext)[0]
        cut_file = f"./db/cut_{file_name}.txt"
        with open(cut_file, 'w') as f:
            f.write(cut_data)
            f.close()


def load_cut_file() -> List[Document]:
    loader = DirectoryLoader('./db', glob='**/*.txt')
    docs = loader.load()
    text_splitter = TokenTextSplitter(chunk_size=1000, chunk_overlap=0)
    return text_splitter.split_documents(docs)


def get_chroma_db(doc_texts: List[Document]) -> Chroma:
    embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
    vectordb = Chroma.from_documents(
        doc_texts, embeddings, persist_directory="./db")
    return vectordb


def vector_chain():
    has_init = os.path.exists('./checkpoint')

    if not has_init:
        init_cut_file()

    dom = load_cut_file()
    vectordb = get_chroma_db(dom)
    if not has_init:
        vectordb.persist()
        with open('./checkpoint', 'w') as f:
            f.write('1')
            f.close()

    return ChatVectorDBChain.from_llm(ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo"),
                                      vectordb, return_source_documents=True)


chain = vector_chain()


def fetch_result(question):
    chat_history = []
    result = chain({"question": question, "chat_history": chat_history})
    return result["answer"]
