import json
import os

class DataManager:
    def __init__(self):
        self.data_dir = "data"
        self.articles_file = os.path.join(self.data_dir, "articles.json")
        self.videos_file = os.path.join(self.data_dir, "videos.json")
        
        # Create data directory if it doesn't exist
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)
        
    def save_content(self, articles_data, videos_data):
        # Save articles
        with open(self.articles_file, 'w') as f:
            json.dump(articles_data, f, indent=4)
            
        # Save videos
        with open(self.videos_file, 'w') as f:
            json.dump(videos_data, f, indent=4)
            
    def load_content(self):
        articles_data = {}
        videos_data = {}
        
        if os.path.exists(self.articles_file):
            with open(self.articles_file, 'r') as f:
                articles_data = json.load(f)
                
        if os.path.exists(self.videos_file):
            with open(self.videos_file, 'r') as f:
                videos_data = json.load(f)
                
        return articles_data, videos_data
