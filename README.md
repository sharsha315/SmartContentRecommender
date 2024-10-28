# Smart Content Recommender 🎯

A vector search application using ChromaDB that recommends relevant articles and YouTube videos based on user queries. The system uses semantic search to find the most relevant content matches.

## Project Overview

The Smart Content Recommender is designed to help users find educational content across different platforms. It uses ChromaDB's vector database capabilities to perform similarity searches and provide accurate content recommendations.

### Key Features
- Semantic search using vector embeddings
- Dual content sources (articles and videos)
- Real-time performance metrics
- User-friendly interface
- Multi-category support

## Technical Implementation

### Core Components
1. ChromaDB for vector storage and similarity search
2. SentenceTransformer for generating embeddings
3. Gradio for the user interface
4. Data persistence for content management

### Technology Stack
- Backend: Python, ChromaDB
- Embeddings: SentenceTransformer
- Frontend: Gradio
- Data Management: Pandas, JSON

## Installation Guide

1. Clone the repository:
```bash
git clone https://github.com/yourusername/smart-content-recommender.git
cd smart-content-recommender
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # For Unix/Mac
.\venv\Scripts\activate   # For Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python src/app.py
```

## Usage Instructions

1. Access the web interface at http://localhost:7860
2. Enter your query in the search box
3. Click "Get Recommendations"
4. View recommended articles and videos with:
    - Title and author
    - Category
    - Direct links
    - Content preview

## Performance Metrics

### Vector Search Performance

- Average query time: ~0.1 seconds
- Content database size: 20+ entries

### System Optimization
- Efficient vector indexing
- Optimized content storage
- Fast retrieval system

## Demo Video
![Smart Content Recommender Demo](https://www.youtube.com/watch?v=YOUR_VIDEO_ID)

## Technical Highlights

1. ChromaDB Integration
    - Dual collections for different content types
    - Efficient vector similarity search
    - Metadata management
    - Vector Search Implementation

2.SentenceTransformer for text embeddings
    - Semantic similarity matching
    - Real-time query processing
    - Performance Optimizations

3. Efficient data loading
- Optimized search algorithms
- Quick response times

## Quick Demo Snapshot

![Demo GIF](images/bounty_cromadb_smartContentRecommender.png)
