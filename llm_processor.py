from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import json

class LLMProcessor:
    def __init__(self, api_key, base_url, model_name):
        self.llm = ChatOpenAI(
            openai_api_key=api_key,
            model_name=model_name,
            base_url=base_url
        )

    def create_prompt_template(self):
        template = """You are an AI assistant tasked with analyzing web content. You have been provided with the following information scraped from a webpage:

URL: {url}
Title: {title}
Meta Description: {meta_description}

Main Content:
{text_content}

Links:
{links}

Images:
{images}

Structured Data:
{structured_data}

Based on this information, please respond to the following query:
{query}

Instructions:
1. Analyze the provided information carefully.
2. Focus on addressing the specific query using the most relevant parts of the scraped data.
3. If the query asks for a summary, provide a concise yet informative summary of the main content.
4. If the query is about specific details, use the structured data or other relevant sections to provide accurate information.
5. If the query is not directly answerable from the given information, provide the most relevant information available and state any limitations.

Your response:
"""
        return ChatPromptTemplate.from_template(template)

    def format_scraped_data(self, data):
        formatted_links = "\n".join([f"- {link['text']}: {link['href']}" for link in data['links'][:5]])
        formatted_images = "\n".join([f"- {img['alt']} ({img['src']})" for img in data['images'][:5]])
        
        structured_data_str = "No structured data available"
        if data['structured_data']:
            try:
                # Attempt to parse and pretty-print the first structured data item
                parsed_data = json.loads(data['structured_data'][0])
                structured_data_str = json.dumps(parsed_data, indent=2)
            except json.JSONDecodeError:
                structured_data_str = "Structured data present but not valid JSON"

        return {
            "url": data['url'],
            "title": data['title'],
            "meta_description": data['meta_description'],
            "text_content": data['text_content'],
            "links": formatted_links,
            "images": formatted_images,
            "structured_data": structured_data_str
        }

    def process_content(self, scraped_data, query):
        prompt_template = self.create_prompt_template()
        chain = prompt_template | self.llm | StrOutputParser()
        
        formatted_data = self.format_scraped_data(scraped_data)
        formatted_data['query'] = query

        result = chain.invoke(formatted_data)
        return result.strip()