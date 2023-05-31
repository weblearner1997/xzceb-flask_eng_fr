import os
from dotenv import load_dotenv
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import json

# Load environment variables
load_dotenv()

# Get API key and URL from environment variables
apikey = os.environ['apikey']
url = os.environ['url']

# Set up IBM Watson Language Translator
authenticator = IAMAuthenticator(apikey)
translator = LanguageTranslatorV3(
    version="2018-05-01",
    authenticator=authenticator
)
translator.set_service_url(url)


def english_to_french(english_text):
    """
    Translate English text to French.
    """
    if english_text is None:
        return None

    translation = translator.translate(
        text=english_text,
        source="en",
        target="fr"
    )
    french_text = json.loads(json.dumps(translation.get_result()))['translations'][0]['translation']
    return french_text


def french_to_english(french_text):
    """
    Translate French text to English.
    """
    if french_text is None:
        return None

    translation = translator.translate(
        text=french_text,
        source="fr",
        target="en"
    )
    english_text = json.loads(json.dumps(translation.get_result()))['translations'][0]['translation']
    return english_text
