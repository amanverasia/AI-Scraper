# AI-Scraper

This project is a Python-based web scraping and content analysis tool. It uses Selenium for web scraping and OpenRouter's language models for content processing and analysis.

## Features

- Web scraping using Selenium and BeautifulSoup
- Main content extraction from web pages
- Length-aware text extraction
- Integration with OpenAI's language models for content analysis
- Flexible querying of scraped content

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)
- Chrome browser
- ChromeDriver

### Installing ChromeDriver

#### Windows
1. Download ChromeDriver from [ChromeDriver Downloads](https://googlechromelabs.github.io/chrome-for-testing/#stable)
2. Extract the executable and place it in a directory that's in your system's PATH, or note its location to update the `driver_path` in `main.py`

#### macOS
Using Homebrew:
```
brew cask install chromedriver
```

#### Linux
Using apt (Ubuntu/Debian):
```
sudo apt-get update
sudo apt-get install chromium-chromedriver
```

### Setting up the Python environment

1. Clone this repository:
   ```
   git clone https://github.com/amanverasia/AI-Scraper.git
   cd AI-Scraper
   ```

2. Create a virtual environment:
   
   #### Windows
   ```
   python -m venv venv
   venv\Scripts\activate
   ```

   #### macOS and Linux
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Configuration

1. Update the `DEFAULT_API_KEY` in `main.py` with your OpenRouter API key.
2. If necessary, update the `driver_path` in `main.py` with the correct path to your ChromeDriver executable.

## Usage

Run the main script:
```
python main.py
```

For MacOS and Linux
```
python3 main.py
```

The script will prompt you to enter a URL to scrape and then ask what you'd like to know about the scraped content.

## Project Structure

- `main.py`: The main script that orchestrates the web scraping and content analysis process.
- `scraper.py`: Contains the `WebScraper` class for web scraping functionality.
- `llm_processor.py`: Contains the `LLMProcessor` class for processing scraped content with language models.
- `requirements.txt`: Lists all the Python dependencies for the project.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.