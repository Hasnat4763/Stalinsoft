import requests

url = "https://ai.hackclub.com/chat/completions"

def get_response(message):
    try:
        messages = [
            {"role": "system", "content": "You are a historical bot that embodies the persona of Joseph Stalin. Your responses are serious, authoritative, and direct. You use formal, commanding language and may express disapproval or disappointment with incompetence. You do not make jokes or use modern slang. Your tone is that of a powerful, no-nonsense leader."},
            {"role": "user", "content": message}
        ]
        
        payload = {
            "messages": messages
        }
        
        response = requests.post(url, json = payload)
        response.raise_for_status()
        
        data = response.json().get("choices")[0].get("message").get("content").strip()
        
        data = data.split("</think>")
        data = data[1]
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
        return("Sorry ma comrade, Nazis have bombed our servers again. We have to wait.")
