
# print("Collected News Data:")
# for key, value in all_news.items():
#     print(f"{key}: {value['title']} by {'---- '.join(value['author'])} on {'---- '.join(value['published'])}")
#     print("Content:", ' '.join(value['content'][:2]), "...")  # Print first two paragraphs of content
#     print("--------------------------------------------------------------------")
from .collect_news import all_news
import ollama
import time
import pandas as pd

client = ollama.Client()
# tinyllama:latest fast less precise
# mistral:instruct medium precise
# phi3:latest slow more precise
news={}
num=0
for key, value in all_news.items():
    start_time=time.time()
    model="tinyllama:latest"
    prompt = "Summarize the following news article:  under 100 word end it with WAAH ASHUTOSH WAAAH\n\n"
    prompt += f"Content: {value['content']}\n\n"
    prompt += "Summary:\n"

    response = client.generate(
        model=model,
        prompt=prompt,
        # max_tokens=100,  Limits the length of the output.
        # temperature=0.1, Controls randomness (higher = more creative).
        # top_p=0.9 Nucleus sampling (limits output to top 90% probability mass).
        # top_p=1.0,Full randomness (can choose any word).
        # top_p=0.5: Very focused, less creative.
    )
    print("Time taken: ", time.time()-start_time)
    dic={
        'news_id': value['news_id'],
        'title': value['title'],
        'author': value['author'],
        'published': value['published'],
        'content': value['content'],
        'summary': response.response,
        'link': value['link']
    }
    news[str(num)]=dic
    num+=1
    # print("Response from model:")
    # print(response.response)

print("done with api ai")
for key, value in news.items():
    print(f"{key}: {value['title']} by {'---- '.join(value['author'])} on {'---- '.join(value['published'])}")
    print("Content:", ' '.join(value['content'][:2]), "...")  # Print first two paragraphs of content
    print("Summary:", value['summary'])
    print("--------------------------------------------------------------------")
    print("Link:", value['link'])