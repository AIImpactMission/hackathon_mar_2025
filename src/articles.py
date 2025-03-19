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

def create_keywords_tags_fuzzy(
    article_text: str,
    keywords: Dict[str, List[str]],
    threshold: float = 0.2,
    fuzzy_threshold: float = 0.7,
    max_length_diff: int = 3,
    min_word_length: int = 3,
) -> str:
    """
    Assigns a tag to the article_text based on keyword hits using fuzzy matching
    and basic optimization.

    :param article_text: The article text to analyze.
    :param keywords: A dictionary of the form {tag: [keyword1, keyword2, ...]}.
    :param threshold: The minimum fraction of matched keywords required to assign a tag.
    :param fuzzy_threshold: The similarity threshold (0.0 to 1.0) for considering a keyword "matched".
    :param max_length_diff: The maximum allowed difference in word lengths before skipping comparison.
    :return: The tag with the highest fraction of matched keywords or 'other'.
    """
    text_words = re.findall(r"\w+", article_text.lower())
    unique_words = set(text_words)
    unique_words = [word for word in unique_words if len(word) >= min_word_length]

    best_tag = "other"
    best_fraction = 0.0

    for tag, kw_list in keywords.items():
        if not kw_list:
            continue

        matched_count = 0

        for kw in kw_list:
            
            kw_lower = kw.lower()
            found_match = False

            for word in unique_words:
                # a) Quick length-based pruning
                if abs(len(word) - len(kw_lower)) > max_length_diff:
                    continue

                # b) Calculate similarity
                similarity = SequenceMatcher(None, word, kw_lower).ratio()
                if similarity >= fuzzy_threshold:
                    found_match = True
                    break

            if found_match:
                matched_count += 1

        fraction_matched = matched_count / len(kw_list)

        if fraction_matched > best_fraction:
            best_fraction = fraction_matched
            best_tag = tag

    if best_fraction < threshold:
        return "other"

    return best_tag
    
def keywords_dict():
    """
    Create a dictionary of keywords for each tag.
    :return: A dictionary of keywords for each tag.
    """
    keywords_dict = {
        "Financial Crises": [
            "Wirtschaftszusammenbruch",
            "Bankenzusammenbruch",
            "Staatsverschuldung",
            "Kreditklemme",
            "Rettungspaket",
            "Markteinbruch",
            "Rezession",
            "Finanzielle Instabilität",
            "Immobilienblase",
            "Börsencrash"
        ],
        "Sustainability": [
            "Erneuerbare Energien",
            "Umweltverantwortung",
            "CO2-Fußabdruck",
            "Grüne Initiativen",
            "Anpassung an den Klimawandel",
            "Kreislaufwirtschaft",
            "Ressourcenschonung",
            "Umweltfreundlich",
            "Nachhaltige Entwicklung",
            "Emissionsreduktion"
        ],
        "Fake News": [
            "Fehlinformation",
            "Desinformation",
            "Faktencheck",
            "Virale Falschmeldungen",
            "Propaganda",
            "Clickbait",
            "Medienmanipulation",
            "Falsche Narrative",
            "Verschwörungstheorien",
            "Erfundene Geschichten"
        ],
        "AI": [
            "Maschinelles Lernen",
            "Deep Learning",
            "Algorithmische Intelligenz",
            "Sprachverarbeitung",
            "Chatbot",
            "Robotik",
            "Künstliche Intelligenz",
            "Predictive Analytics",
            "Computer Vision",
            "Datenbasierte Erkenntnisse"
        ],
        "Digitalization": [
            "Digitale Transformation",
            "E-Governance",
            "Automatisierung",
            "Cloud Computing",
            "Online-Plattformen",
            "Virtuelle Dienstleistungen",
            "Cybersicherheit",
            "Blockchain",
            "Internet der Dinge",
            "Fernarbeit"
        ],
        "Local Journalism": [
            "Berichterstattung aus der Gemeinde",
            "Regionale Nachrichten",
            "Hyperlokale Berichterstattung",
            "Nachbarschaftsgeschichten",
            "Basisnahe Medien",
            "Lokale Presse",
            "Kommunale Neuigkeiten",
            "Bürgerjournalismus",
            "Stadtredaktion",
            "Berichterstattung im öffentlichen Interesse"
        ],
        "COVID": [
            "Pandemie",
            "Coronavirus",
            "Abstand halten",
            "Lockdown",
            "Impfkampagne",
            "Gesundheitskrise",
            "Quarantäne",
            "Kontaktverfolgung",
            "Virenausbruch",
            "COVID-19"
        ],
        "Demographics": [
            "Bevölkerungstrends",
            "Volkszählungsdaten",
            "Altersverteilung",
            "Migrationsmuster",
            "Sozioökonomische Faktoren",
            "Urbanisierung",
            "Bevölkerungswachstum",
            "Generationswechsel",
            "Haushaltszusammensetzung",
            "Demografische Analyse"
        ],
        "Innovation": [
            "Durchbrüche",
            "Unternehmertum",
            "Forschung und Entwicklung",
            "Spitzentechnologie",
            "Produkterfindung",
            "Disruptive Ideen",
            "Innovative Lösungen",
            "Prototyping",
            "Risikokapital",
            "Kreatives Denken"
        ]
    }
    return keywords_dict