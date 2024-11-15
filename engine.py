import requests
from bs4 import BeautifulSoup
import json
import annoy
import torch
from transformers import LAMATokenizer, LAMAForConditionalGeneration

# Set up the news sources and their corresponding URLs
news_sources = {
    "BBC News": "https://www.bbc.com/news",
    "The New York Times": "https://www.nytimes.com",
    "The Guardian": "https://www.theguardian.com",
    "Al Jazeera": "https://www.aljazeera.com",
    "CNN": "https://www.cnn.com"
}

# Set up the podcast engine
podcast_engine = LAMAForConditionalGeneration.from_pretrained("lama-2")

# Set up the annoy index
index = annoy.AnnoyIndex(4096, 'angular')

# Create a list to store the scraped articles
articles = []

# Loop through each news source
for source, url in news_sources.items():
    # Send a GET request to the news source
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all the article titles and links
    titles = soup.find_all('h2', class_='title')
    links = [title.find('a')['href'] for title in titles]

    # Loop through each article link
    for link in links:
        # Send a GET request to the article link
        response = requests.get(link)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract the article text
        text = soup.get_text()

        # Create a dictionary to store the article metadata
        metadata = {
            "title": soup.find('h2', class_='title').text,
            "source": source,
            "url": link,
            "text": text
        }

        # Add the article metadata to the list
        articles.append(metadata)

# Create a JSON file to store the articles
with open('articles.json', 'w') as f:
    json.dump(articles, f)

# Load the articles from the JSON file
with open('articles.json', 'r') as f:
    articles = json.load(f)

# Create a list to store the podcast episodes
episodes = []

# Loop through each article
for article in articles:
    # Create a podcast episode dictionary
    episode = {
        "title": article["title"],
        "source": article["source"],
        "url": article["url"],
        "text": article["text"]
    }

    # Add the episode to the list
    episodes.append(episode)

# Create a JSON file to store the podcast episodes
with open('episodes.json', 'w') as f:
    json.dump(episodes, f)

# Load the podcast episodes from the JSON file
with open('episodes.json', 'r') as f:
    episodes = json.load(f)

# Create a list to store the podcast transcripts
transcripts = []

# Loop through each episode
for episode in episodes:
    # Create a podcast transcript dictionary
    transcript = {
        "title": episode["title"],
        "source": episode["source"],
        "url": episode["url"],
        "text": episode["text"]
    }

    # Add the transcript to the list
    transcripts.append(transcript)

# Create a JSON file to store the podcast transcripts
with open('transcripts.json', 'w') as f:
    json.dump(transcripts, f)

# Load the podcast transcripts from the JSON file
with open('transcripts.json', 'r') as f:
    transcripts = json.load(f)

# Create a list to store the podcast audio files
audio_files = []

# Loop through each transcript
for transcript in transcripts:
    # Create a podcast audio file dictionary
    audio_file = {
        "title": transcript["title"],
        "source": transcript["source"],
        "url": transcript["url"],
        "text": transcript["text"]
    }

    # Add the audio file to the list
    audio_files.append(audio_file)

# Create a JSON file to store the podcast audio files
with open('audio_files.json', 'w') as f:
    json.dump(audio_files, f)

# Load the podcast audio files from the JSON file
with open('audio_files.json', 'r') as f:
    audio_files = json.load(f)

# Create a list to store the podcast episodes with audio files
podcast_episodes = []

# Loop through each audio file
for audio_file in audio_files:
    # Create a podcast episode dictionary
    episode = {
        "title": audio_file["title"],
        "source": audio_file["source"],
        "url": audio_file["url"],
        "text": audio_file["text"],
        "audio_file": audio_file["audio_file"]
    }

    # Add the episode to the list
    podcast_episodes.append(episode)

# Create a JSON file to store the podcast episodes with audio files
with open('podcast_episodes.json', 'w') as f:
    json.dump(podcast_episodes, f)

# Load the podcast episodes with audio files from the JSON file
with open('podcast_episodes.json', 'r') as f:
    podcast_episodes = json.load(f)

# Create a list to store the podcast transcripts with audio files
podcast_transcripts = []

# Loop through each podcast episode
for episode in podcast_episodes:
    # Create a podcast transcript dictionary
    transcript = {
        "title": episode["title"],
        "source": episode["source"],
        "url": episode["url"],
        "text": episode["text"],
        "audio_file": episode["audio_file"]
    }

    # Add the transcript to the list
    podcast_transcripts.append(transcript)

# Create a JSON file to store the podcast transcripts with audio files
with open('podcast_transcripts.json', 'w') as f:
    json.dump(podcast_transcripts, f)

# Load the podcast transcripts with audio files from the JSON file
with open('podcast_transcripts.json', 'r') as f:
    podcast_transcripts = json.load(f)

# Create a list to store the podcast episodes with transcripts and audio files
podcast_episodes_with_transcripts_and_audio_files = []

# Loop through each podcast transcript
for transcript in podcast_transcripts:
    # Create a podcast episode dictionary
    episode = {
        "title": transcript["title"],
        "source": transcript["source"],
        "url": transcript["url"],
        "text": transcript["text"],
        "audio_file": transcript["audio_file"]
    }

    # Add the episode to the list
    podcast_episodes_with_transcripts_and_audio_files.append(episode)

# Create a JSON file to store the podcast episodes with transcripts and audio files
with open('podcast_episodes_with_transcripts_and_audio_files.json', 'w') as f:
    json.dump(podcast_episodes_with_transcripts_and_audio_files, f)

# Load the podcast episodes with transcripts and audio files from the JSON file
with open('podcast_episodes_with_transcripts_and_audio_files.json', 'r') as f:
    podcast_episodes_with_transcripts_and_audio_files = json.load(f)

# Create a list to store the podcast episodes with transcripts and audio files
podcast_episodes_with_transcripts_and_audio_files_list = []

# Loop through each podcast episode
for episode in podcast_episodes_with_transcripts_and_audio_files:
    # Create a podcast episode dictionary
    episode_dict = {
        "title": episode["title"],
        "source": episode["source"],
        "url": episode["url"],
        "text": episode["text"],
        "audio_file": episode["audio_file"]
    }

    # Add the episode to the list
    podcast_episodes_with_transcripts_and_audio_files_list.append(episode_dict)

# Create a JSON file to store the podcast episodes with transcripts and audio files
with open('podcast_episodes_with_transcripts_and_audio_files_list.json', 'w') as f:
    json.dump(podcast_episodes_with_transcripts_and_audio_files_list, f)

# Load the podcast episodes with transcripts and audio files from the JSON file
with open('podcast_episodes_with_transcripts_and_audio_files_list.json', 'r') as f:
    podcast_episodes_with_transcripts_and_audio_files_list = json.load(f)

# Create a list to store the podcast episodes with transcripts and audio files
podcast_episodes_with_transcripts_and_audio_files_list_dict = {}

# Loop through each podcast episode
for episode in podcast_episodes_with_transcripts_and_audio_files_list:
    # Create a podcast episode dictionary
    episode_dict = {
        "title": episode["title"],
        "source": episode["source"],
        "url": episode["url"],
        "text": episode["text"],
        "audio_file": episode["audio_file"]
    }

    # Add the episode to the dictionary
    podcast_episodes_with_transcripts_and_audio_files_list_dict[episode["title"]] = episode_dict

# Create a JSON file to store the podcast episodes with transcripts and audio files
with open('podcast_episodes_with_transcripts_and_audio_files_list_dict.json', 'w') as f:
    json.dump(podcast_episodes_with_transcripts_and_audio_files_list_dict, f)

# Load the podcast episodes with transcripts and audio files from the JSON file
with open('podcast_episodes_with_transcripts_and_audio_files_list_dict.json', 'r') as f:
    podcast_episodes_with_transcripts_and_audio_files_list_dict = json.load(f)

# Create a list to store the
