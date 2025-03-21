import re
from difflib import SequenceMatcher
from typing import Dict, List

def process_raw_article(article):
    """
    Process the raw article data and extract the relevant information.
    :param article: The raw article dict from JSON.
    :return: A dict containing the key fields.
    """
    result = {}
    result["id"] = article["uuid"]
    result["published_at"] = article["first_published_at"]

    content = article["content"]
    result["author"] = content["autor"]
    result["title"] = content["titel"]

    # Extract category
    try:
        category = content["category"]["name"]
    except:
        category = ""
    result["category"] = category

    # Extract section
    try:
        section = content["category"]["content"]["parent"]
    except:
        section = ""
    result["section"] = section

    # Extract the text from the article
    article_text = ""
    for block in content["inhalt"]["content"]:
        if block["type"] == "paragraph":    
            for part in block["content"]:
                if part.get("type") == "text":
                    text = part.get("text", "")
                    article_text += text
                    article_text += "\n"

    result["text"] = article_text
    return result

def create_static_metadata(article, filename):
    """
    Create a static metadata dict for the article.
    :param article: The article dict.
    :param filename: The filename of the article.
    :return: A dict with the metadata.
    """
    article_metadata = {
        "id": article["id"],
        "title": article["title"],
        "author": article["author"],
        "published_at": article["published_at"],
        "words_count": len(article["text"].split(" ")),
        "filename": filename,
        "category": article["category"],
        "section": article["section"],
    }
    return article_metadata