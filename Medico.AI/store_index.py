from src.helper import load_pdf_file, text_split, download_hugging_face_embeddings
from pinecone.grpc import PineconeGrpcClient as Pinecone
from pinecone import ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv
import os


load_dotenv()
PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY")
os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY

extracted_data= load_pdf_file(data='E:\\Diksha\\P\\Medico.AI\\Data')
text_chunks= text_split(extracted_data)
embeddings= download_hugging_face_embeddings()

pc = Pinecone(api_key="pcsk_5it82V_2mUxteDmFGC7tGkF8EYrJSccQzBURLAjKrFWekT3BTWLjrkVYxtQ7hfTPWBYZ1E")   # no need for environment= here

index_name = "medico-ai"

# First check if index exists
if not pc.has_index(index_name):
    pc.create_index(
        name=index_name,
        dimension=384,             
        metric="cosine",            
        spec=ServerlessSpec(        
            cloud="aws", 
            region="us-east-1"
        )
    )


docsearch= PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding=embeddings
)