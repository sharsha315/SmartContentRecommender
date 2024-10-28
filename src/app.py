import gradio as gr
import pandas as pd
from database import ContentDatabase
from data_manager import DataManager
import time

# Initialize data manager
data_manager = DataManager()

# Sample content data
sample_articles = {
    'title': [
        'Python 101: A Beginners Guide to Python Programming',
        'Learning Python Pandas Library: A Comprehensive Guide with Code Examples',
        'Python Programming Basics: Statements, Comments, and Data Types',
        'Machine Learning Tutorials for Beginners completely Free',
        'The Fundamental Mathematics of Machine Learning',
        'Artificial Intelligence - An Overview',
        'What is AI? Artificial Intelligence explained',
        'Web Development for Beginners: A new Learning Path on Microsoft Learn',
        'Web Development Guide For Absolute Beginners',
        'Learn Full-Stack Web Development with React and GraphQL by Building a Sticky Note App - Part one'
    ],
    'description': [
        'Comprehensive guide to Python programming fundamentals including data types, functions, and OOP concepts',
        'Python Pandas library is a powerful tool for data manipulation and analysis.',
        'Master Python Programming Basics: Learn About Statements, Comments, Variables, and Data Types in Python.',
        'In this article I came up with Best YouTube Tutorials and Website for starting your Journey with Machine Learning',
        'A Deep Dive into Vector Norms, Linear Algebra, Calculus',
        'Artificial Intelligence - An Overview',
        'A guide to artificial intelligence in the enterprise',
        'Web Development for Beginners: A new Learning Path on Microsoft Learn',
        'Web Development Guide For Absolute Beginners',
        'Learn Full-Stack Web Development with React and GraphQL by Building a Sticky Note App - Part one'
    ],
    'category': ['Programming', 'Programming', 'Programming', 'Machine Learning', 'Machine Learning', 'Artificial Intelligence', 'Artificial Intelligence', 'Web Development', 'Web Development', 'Web Development'],
    'author': ['DM Codinius', 'Python Programming', 'Arnav Singh', 'Mr.Shah', 'Joseph Robinson, Ph.D', 'Attaullah Shafiq', 'Lev Craig', 'Chris Noring', 'Bhavesh Goyal', 'Temitope'],
    'url': [
        'https://dev.to/codinius/python-101-a-beginners-guide-to-python-programming-1b95',
        'https://medium.com/@LearnPythonProgramming/learning-python-pandas-library-a-comprehensive-guide-with-code-examples-dfec8e0b7d68',
        'https://pythonfornoobs.hashnode.dev/python-basics',
        'https://dev.to/shahstavan/machine-learning-tutorials-completely-free-4927',
        'https://medium.com/towards-artificial-intelligence/the-fundamental-mathematics-of-machine-learning-39c2418d19c6',
        'https://dev.to/attaullahshafiq10/artificial-intelligence-an-overview-4ma3',
        'https://www.techtarget.com/searchenterpriseai/definition/AI-Artificial-Intelligence',
        'https://dev.to/azure/web-dev-for-beginners-on-learn-4fpk',
        'https://dev.to/dsc_ciet/web-development-guide-for-absolute-beginners-235f',
        'https://dev.to/kingdavid/learn-full-stack-web-development-with-react-and-graphql-by-building-a-sticky-note-app-part-one-4kck'
    ]
}

sample_videos = {
    'title': [
        'Python for Beginners - Learn Python in 1 Hour',
        'Python for Beginners - Full Course Programming Tutorial',
        'Python As Fast as Possible - Learn Python in ~75 Minutes',
        '12 Beginner Python Projects - Coding Course',
        'Machine Learning for Everybody - Full Course',
        'Complete Machine Learning In 6 Hours | Krish Naik',
        'Harvard CS50s Artificial Intelligence with Python - Full University Course',
        'Generative AI Full Course - Gemini Pro, OpenAI, Llama, Langchain, Pinecone, Vector Databases & More',
        'Full Course Web Development [22 Hours] | Learn Full Stack Web Development From Scratch',
        'HTML & CSS Full Course | Web Development for Beginners',
        'Full Stack Web Development for Beginners (Full Course on HTML, CSS, JavaScript, Node.js, MongoDB)'
    ],
    'description': [
        'Complete Python tutorial for beginners with hands-on examples and practical projects',
        'Learn the Python programming language in this full course for beginners! You will learn the fundamentals of Python and code two Python programs line-by-line.',
        'This python tutorial aims to teach you python as fast as possible. This python speed course will cover all the fundamentals of python and give you a quick overview of all of the main python features.',
        'Improve your Python skills by following along with 12 different Python project tutorials.',
        'Learn Machine Learning in a way that is accessible to absolute beginners. You will learn the basics of Machine Learning and how to use TensorFlow to implement many different concepts.',
        'Complete Machine Learning Algorithms for Data Science',
        'This course from Harvard University explores the concepts and algorithms at the foundation of modern artificial intelligence',
        'Learn about generative models and different frameworks, investigating the production of text and visual material produced by artificial intelligence.',
        'This is full Stack Web Development Course for Absolute Beginners.',
        'In this video I teach you everything you need to know about web development with HTML & CSS so that you can start building your own amazing, modern and responsive websites today!',
        'Learn full-stack web development in this full course for beginners.'        
    ],
    'category': ['Programming', 'Programming', 'Programming', 'Python Projects', 'Machine Learning', 'Machine Learning', 'Artificial Intelligence', 'Generative AI', 'Web Development', 'Web Development', 'Web Development'],
    'author': ['Programming with Mosh', 'freeCodeCamp.org', 'Tech With Tim', 'freeCodeCamp.org', 'freeCodeCamp.org', 'Krish Naik', 'freeCodeCamp.org', 'freeCodeCamp.org', 'Mehul - Codedamn', 'Smoljames', 'freeCodeCamp.org'],
    'url': [
        'https://youtu.be/kqtD5dpn9C8?si=DSvCfl6dRml5jHYb',
        'https://youtu.be/eWRfhZUzrAc?si=ODLH6a-h4n3GN8kE',
        'https://youtu.be/VchuKL44s6E?si=W5TS9QUCx4hMwjLp',
        'https://youtu.be/8ext9G7xspg?si=LakI-0bwJf-Gh69i',
        'https://youtu.be/i_LwzRVP7bg?si=xdo-1pp_m7Uv-x8o',
        'https://youtu.be/JxgmHe2NyeY?si=I1RnC75RLlksC3x3',
        'https://youtu.be/5NgNicANyqM?si=ZnFcOzfgQ0cmaq1t',
        'https://youtu.be/mEsleV16qdo?si=nhJXrxAHz-lz2eFS',
        'https://youtu.be/ZxKM3DCV2kE?si=sFSNn9z5ZQOr9sVf',
        'https://youtu.be/Eb3lOiukwAQ?si=nuUA3NrXMvG-QwJr',
        'https://youtu.be/nu_pCVPKzTk?si=X3YM8fUdcW2w3_g6'        
    ]
}

# Save sample data
data_manager.save_content(sample_articles, sample_videos)

# Load data
loaded_articles, loaded_videos = data_manager.load_content()

# Initialize database
db = ContentDatabase()
articles_df = pd.DataFrame(loaded_articles)
videos_df = pd.DataFrame(loaded_videos)

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
        {'=' * 50}
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
    
    performance = f"""
    ⚡ Performance Metrics:
    - Query Time: {query_time:.4f} seconds
    - Results Found: {len(results['articles']['documents'][0])} articles, {len(results['videos']['documents'][0])} videos
    """
    return articles_formatted, videos_formatted, performance

# Create Gradio interface
with gr.Blocks(theme=gr.themes.Soft()) as interface:
    gr.Markdown("# 🎯 Smart Content Recommender")
    gr.Markdown(f"""
    ### System Information
    - Articles Database Size: {len(articles_df)} entries
    - Videos Database Size: {len(videos_df)} entries
    - Articles Ingestion Time: {article_ingestion_time:.4f} seconds
    - Videos Ingestion Time: {video_ingestion_time:.4f} seconds
    """)
    
    with gr.Row():
        with gr.Column(scale=1):
            query_input = gr.Textbox(
                placeholder="What would you like to learn about?",
                label="🔍 Search Query",
                lines=2
            )
            search_button = gr.Button("🚀 Get Recommendations", variant="primary")
            
            gr.Markdown("""
            ### 💡 Example Queries:
            - "Python programming basics"
            - "Machine learning for beginners"
            - "Web development tutorials"
            - "Data science projects"
            - "AI applications"
            """)
        
        with gr.Column(scale=2):
            articles_output = gr.Textbox(
                label="📚 Recommended Articles",
                lines=10
            )
            videos_output = gr.Textbox(
                label="🎥 Recommended Videos",
                lines=10
            )
            performance_output = gr.Textbox(
                label="📊 Performance Metrics"
            )
    
    search_button.click(
        fn=search_content,
        inputs=query_input,
        outputs=[articles_output, videos_output, performance_output]
    )

if __name__ == "__main__":
    interface.launch()
