import gradio as gr
import pandas as pd
from database import ContentDatabase
import time

# Sample content data
sample_articles = {
    'title': [
        'Getting Started with Python',
        'Machine Learning Basics',
        'Web Development 101'
    ],
    'description': [
        'Comprehensive guide to Python programming fundamentals...',
        'Introduction to machine learning concepts and applications...',
        'Complete overview of modern web development...'
    ],
    'category': ['Programming', 'Machine Learning', 'Web Development'],
    'author': ['John Doe', 'Jane Smith', 'Mike Johnson'],
    'url': [
        'https://blog.example.com/python-guide',
        'https://blog.example.com/ml-basics',
        'https://blog.example.com/web-dev-101'
    ]
}

sample_videos = {
    'title': [
        'Python Programming for Beginners',
        'Machine Learning Crash Course',
        'Web Dev Tutorial'
    ],
    'description': [
        'Complete Python tutorial for beginners with hands-on examples...',
        'Comprehensive machine learning course covering key concepts...',
        'Step-by-step guide to building modern websites...'
    ],
    'category': ['Programming', 'Machine Learning', 'Web Development'],
    'author': ['TechChannel', 'AI Academy', 'WebDev Pro'],
    'url': [
        'https://youtube.com/watch?v=123',
        'https://youtube.com/watch?v=456',
        'https://youtube.com/watch?v=789'
    ]
}

# Initialize database
db = ContentDatabase()
articles_df = pd.DataFrame(sample_articles)
videos_df = pd.DataFrame(sample_videos)

# Add content to database
article_ingestion_time = db.add_content(articles_df, 'article')
video_ingestion_time = db.add_content(videos_df, 'video')

def format_content(result: dict, content_type: str) -> str:
    formatted = []
    for i in range(len(result['documents'][0])):
        metadata = result['metadatas'][0][i]
        formatted.append(f"""
        📌 {metadata['title']}
        👤 Author: {metadata['author']}
        🏷️ Category: {metadata['category']}
        🔗 Link: {metadata['url']}
        📝 Preview: {result['documents'][0][i][:200]}...
        """)
    return "\n".join(formatted)

def search_content(query: str) -> tuple:
    if not query.strip():
        return "Please enter a query", "", ""
    
    start_time = time.time()
    results = db.search_similar(query)
    query_time = time.time() - start_time
    
    articles_formatted = "📚 ARTICLES:\n" + format_content(results['articles'], 'article')
    videos_formatted = "\n\n🎥 VIDEOS:\n" + format_content(results['videos'], 'video')
    
    performance = f"Query Time: {query_time:.4f} seconds"
    return articles_formatted, videos_formatted, performance

# Create Gradio interface
with gr.Blocks(theme=gr.themes.Soft()) as interface:
    gr.Markdown("# 🎯 Smart Content Recommender")
    gr.Markdown(f"""
    System Initialization Times:
    - Articles: {article_ingestion_time:.4f} seconds
    - Videos: {video_ingestion_time:.4f} seconds
    """)
    
    with gr.Row():
        with gr.Column():
            query_input = gr.Textbox(
                placeholder="What would you like to learn about?",
                label="Search Query"
            )
            search_button = gr.Button("🔍 Get Recommendations", variant="primary")
        
        with gr.Column():
            articles_output = gr.Textbox(
                label="📚 Recommended Articles",
                lines=10
            )
            videos_output = gr.Textbox(
                label="🎥 Recommended Videos",
                lines=10
            )
            performance_output = gr.Textbox(
                label="⚡ Performance Metrics"
            )
    
    search_button.click(
        fn=search_content,
        inputs=query_input,
        outputs=[articles_output, videos_output, performance_output]
    )

interface.launch()
