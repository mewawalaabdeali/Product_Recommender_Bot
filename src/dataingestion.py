from langchain_astradb import AstraDBVectorStore
from langchain_huggingface import HuggingFaceEndpointEmbeddings
from src.dataconverter import DataConverter
from src.config import Config

class DataIngestor:
    def __init__(self):
        self.embedding = HuggingFaceEndpointEmbeddings(model=Config.EMBEDDING_MODEL)
        self.vstore = AstraDBVectorStore(
            embedding=self.embedding,
            collection_name = "awsdb",
            api_endpoint=Config.ASTRA_DB_API_ENDPOINT,
            token = Config.ASTRA_DB_APPLICATION_TOKEN,
            namespace=Config.ASTRA_DB_KEYSPACE
        )


    def ingest(self, load_existing=True):
        if load_existing==True:
            return self.vstore
        
        docs = DataConverter("Data/amazon.csv").convert()

        self.vstore.add_documents(docs)
        return self.vstore
    
if __name__=="__main__":
    ingestor = DataIngestor()
    ingestor.ingest(load_existing=False)