from math import radians, cos, sin, asin, sqrt
import string
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer

def adv_preprocessing(text):
    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text)
    text = [w for w in word_tokens if not w in stop_words]
    text = [lemmatizer.lemmatize(word) for word in text]
    text = ' '.join(text)
    return text

def preprocessing(text, advanced=True):
    for punc in string.punctuation:
        text = text.replace(punc, '')
    lower = text.lower()
    text = ''.join(word for word in lower if not word.isdigit())
    if advanced:
        text = adv_preprocessing(text)
    return text


def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 6371  # Radius of earth in kilometers. Use 3956 for miles
    return c * r




if __name__ == "__main__":
    # Le Wagon location
    lat1, lon1 = 48.865070, 2.380009
    #Insert your coordinates from google maps here
    x = 40.459
    y = 2.1098
    lat2, lon2 = x, y
    distance = haversine(lon1, lat1, lon2, lat2)
    print(distance)
