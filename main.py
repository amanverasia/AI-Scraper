import os
from scraper import WebScraper
from llm_processor import LLMProcessor
import sys
import warnings
import urllib3

warnings.filterwarnings("ignore")
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)  # Suppress InsecureRequestWarning

# Default configuration
DEFAULT_SCRAPE_URL = input("Enter the URL: ")
DEFAULT_API_KEY = ""  # Replace with your actual API key
DEFAULT_MODEL = "meta-llama/llama-3.1-8b-instruct"
DEFAULT_API_BASE_URL = "https://openrouter.ai/api/v1"  # Default OpenAI API base URL

def get_user_prompt():
    print("\nWhat would you like to know about the scraped content?")
    return input("Your question: ").strip()

def main():
    # Allow overriding defaults with environment variables
    scrape_url = os.environ.get("SCRAPE_URL", DEFAULT_SCRAPE_URL)
    api_key = os.environ.get("OPENAI_API_KEY", DEFAULT_API_KEY)
    model = os.environ.get("OPENAI_MODEL", DEFAULT_MODEL)
    api_base_url = os.environ.get("OPENAI_API_BASE_URL", DEFAULT_API_BASE_URL)

    # Initialize the WebScraper
    driver_path = "chromedriver.exe"  # Update this with your chromedriver path
    scraper = WebScraper(driver_path)

    # Initialize the LLMProcessor with OpenAI
    llm_processor = LLMProcessor(api_key=api_key, base_url=api_base_url, model_name=model)

    try:
        # Scrape the website
        print(f"Scraping URL: {scrape_url}")
        scraped_data = scraper.scrape_website(scrape_url)

        # Get user query
        user_query = get_user_prompt()

        # Process the content with LLM
        result = llm_processor.process_content(scraped_data, user_query)

        print("\nLLM Response:")
        print(result)

    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        sys.exit(1)

    finally:
        # Close the WebDriver
        scraper.close()

if __name__ == "__main__":
    main()