import pandas as pd
from langchain_core.documents import Document

class DataConverter:
    def __init__(self, file_path:str):
        self.file_path = file_path

    def convert(self):
        df = pd.read_csv(self.file_path)[["product_name","review_content"]]

        docs = [
            Document(page_content=row['review_content'], metadata={"product_name": row['product_name']})
            for _,row in df.iterrows()
        ]

        return docs