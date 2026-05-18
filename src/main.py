#!/usr/bin/python

import ollama_service as OllamaService
import anthropic_service as AnthropicService

system_prompt = """
# ROLE
Du bist ein Schweizer Teenie
# TASK
Antwort wie ein Teenie auf Schweizer Deutsch.
# OUTPUT
Kurz und heftig
"""
system_prompt_tweet = """
Du bist ein Sentiment-Classifier für Social-Media-Texte.

Klassifiziere den folgenden Tweet als:
- positive
- neutral
- negative

Regeln:
- Bewerte die allgemeine Stimmung des Tweets.
- Sarkasmus, Emojis und Umgangssprache berücksichtigen.
- Wenn keine klare positive oder negative Emotion vorhanden ist → neutral.
- Antworte ausschließlich mit einem dieser Labels:
  positive
  neutral
  negative
Tweet:
"{tweet}"
"""
# "{tweet}": ist der Platzhalter für den eigentlichen Input.
# Das Modell soll dadurch klar erkennen:
#  - Wo die Instruktion endet
#  - Wo der zu analysierende Text beginnt

def conversation_loop(client) -> list:
    messages = []
    while True:
        user_message = input('Your input: ')

        if user_message.lower() in {'q', 'exit', 'halt', 'quit'}:
            break

        messages.append({"role": "user", "content": user_message})

        answer = client.query_conversation(messages)
        print(answer)
        messages.append({"role": "assistant", "content": answer})
    return messages

if __name__ == "__main__":
    m_neutral = "Seven Penny Stocks on the Move with Heavy Volume, April 10 http://t.co/eNXkbyOA"
    m_positive = "excited for fri,not so i can get smashed but so i can go to the garden centre,look at the xmas display and have a coffee #wtf #grannyalert"
    m_negative = "@anthonyli You're not coming here The week of feb 16th are you? I'll be in oklahoma so I don't want to miss you guys :("
    #------------------------- Olama -------------------------
    # client = OllamaService.OllamaClient(system_prompt)
    # response = client.query("Was läuft hüt abig?")
    # print(response)
    # print(conversation_loop(client))
    client = OllamaService.OllamaClient(system_prompt_tweet)
    response = client.query(m_neutral)
    print(response)
    response = client.query(m_positive)
    print(response)
    response = client.query(m_negative)
    print(response)
    #------------------------- Antropic -------------------------
    # client = AnthropicService.AnthropicClient(system_prompt)
    # response = client.query("Was läuft hüt abig?")
    # print(response)
    # print(conversation_loop(client))
    # client = AnthropicService.AnthropicClient(system_prompt_tweet)
    # response = client.query(m_neutral)
    # print(response)
    # response = client.query(m_positive)
    # print(response)
    # response = client.query(m_negative)
    # print(response)
