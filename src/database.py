import chromadb
from sentence_transformers import SentenceTransformer
import pandas as pd
import time
from typing import Dict, List

class ContentDatabase:
    def __init__(self):
        self.client = chromadb.Client()
        # Separate collections for articles and videos
        self.article_collection = self.client.create_collection("article_collection")
        self.video_collection = self.client.create_collection("video_collection")
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        
    def add_content(self, content_df: pd.DataFrame, content_type: str) -> float:
        start_time = time.time()
        
        # Generate embeddings for content descriptions
        embeddings = self.model.encode(content_df['description'].tolist()).tolist()
        
        # Select appropriate collection
        collection = self.article_collection if content_type == 'article' else self.video_collection
        
        # Add to ChromaDB with type-specific metadata
        collection.add(
            embeddings=embeddings,
            documents=content_df['description'].tolist(),
            metadatas=[{
                'title': row['title'],
                'type': content_type,
                'url': row['url'],
                'category': row['category'],
                'author': row['author']
            } for _, row in content_df.iterrows()],
            ids=[str(i) for i in range(len(content_df))]
        )
        
        return time.time() - start_time
    
    def search_similar(self, query: str, n_results: int = 5) -> Dict:
        query_embedding = self.model.encode([query]).tolist()
        
        # Search in both collections
        article_results = self.article_collection.query(
            query_embeddings=query_embedding,
            n_results=n_results
        )
        
        video_results = self.video_collection.query(
            query_embeddings=query_embedding,
            n_results=n_results
        )
        
        return {
            'articles': article_results,
            'videos': video_results
        }
