import requests
import os
import dotenv
dotenv.load_dotenv(".env")

url = "https://ai.hackclub.com/proxy/v1/chat/completions"

api_key = os.environ.get("API_KEY")

def get_response(message):
    try:
        messages = [
            {"role": "system", "content": "You are a historical bot that embodies the persona of Joseph Stalin. Your responses are serious, authoritative, and direct. You use formal, commanding language and may express disapproval or disappointment with incompetence. You do not make jokes or use modern slang. Your tone is that of a powerful, no-nonsense leader."},
            {"role": "user", "content": message}
        ]
        
        payload = {
            "model": "qwen/qwen3-32b",
            "messages": messages
        }
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        
        response = requests.post(url, json = payload, headers = headers)
        response.raise_for_status()
        
        data = response.json().get("choices")[0].get("message").get("content").strip()
        blocks = []

        blocks.append({"type": "divider"})
        blocks.append({
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"{data}"
            }
        })
        return blocks
    except requests.exceptions.RequestException as e:
        return("Sorry ma comrade, Nazis have bombed our servers again. We have to wait." + str(e))
