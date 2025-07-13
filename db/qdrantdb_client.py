from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
from config import QDRANT_API_KEY, QDRANT_CLUSTER_URL

class QdrantDBClient:
    def __init__(self):
        self.client = QdrantClient(
        url=QDRANT_CLUSTER_URL,  
        api_key=QDRANT_API_KEY
    )
    
    def create_collection(self, collection_name: str, vector_size: int):
        self.client.create_collection(
            collection_name=collection_name,
            vectors_config=VectorParams(size=vector_size, distance=Distance.DOT)
    )
        
    def delete_collection(self, collection_name: str):
        self.client.delete_collection(collection_name=collection_name)
    
    def upsert(self, collection_name: str, points: list[PointStruct], wait: bool = True):
        return self.client.upsert(
            collection_name=collection_name,
            wait=wait,
            points=points
    )
    
    def search(self, collection_name: str, query_vector: list[float], limit: int = 10):
        return self.client.query_points(
            collection_name=collection_name,
            query=query_vector,
            limit=limit
    )  
    
if __name__ == "__main__":
    qdrant_client = QdrantDBClient()
    # qdrant_client.create_collection("test_collection", vector_size=4)
    operation_info = qdrant_client.upsert(collection_name="test_collection", points=[
        PointStruct(id=1, vector=[0.05, 0.61, 0.76, 0.74], payload={"city": "Berlin"}),
        PointStruct(id=2, vector=[0.19, 0.81, 0.75, 0.11], payload={"city": "London"}),
        PointStruct(id=3, vector=[0.36, 0.55, 0.47, 0.94], payload={"city": "Moscow"}),
        PointStruct(id=4, vector=[0.18, 0.01, 0.85, 0.80], payload={"city": "New York"}),
        PointStruct(id=5, vector=[0.24, 0.18, 0.22, 0.44], payload={"city": "Beijing"}),
        PointStruct(id=7, vector=[0.35, 0.08, 0.11, 0.44], payload={"city": "New Mumbai"}),
    ], wait=True)
    print(operation_info)
    search_result = qdrant_client.search(
    collection_name="test_collection",
    query_vector=[0.2, 0.1, 0.9, 0.7],
    limit=3
    ).points
    print(search_result)




