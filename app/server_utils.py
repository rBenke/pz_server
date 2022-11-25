import requests as r

def get_user_embedding(user_id):
    #TODO: get embedding vector from model 
    message = "write code here"
    if message.status_code==200:
        print("text: ", message.text)
        return message.text
    else:
        print(message)
        return None

def get_SE_recommendation(embedding):
    #TODO: get search engine recommendation for given embedding
    message = "write code here"
    if message.status_code==200:
        print(message.text)
        return message.text
    else:
        print(message)
        return None

