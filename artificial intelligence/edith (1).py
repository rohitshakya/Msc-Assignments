#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
from chatterbot import ChatBot


# In[2]:


from chatterbot.trainers import ListTrainer


# In[3]:


bot = ChatBot('Rohit')


# In[4]:


from chatterbot.trainers import ListTrainer

trainer = ListTrainer(bot)

trainer.train([
    'hii',
    'hello',
    'How are you?',
    'I am good.',
    'Good to hear.',
    'Thank you',
    'You are welcome.',
    'I would like to book a flight.',
    'Sure sir!!',
])


# In[5]:


response = bot.get_response('I would like to book a flight.')

print(response)


# In[6]:


response = bot.get_response('How are You?')

print(response)


# In[7]:


response = bot.get_response('I would like to book a flight.')

print(response)


# In[8]:



convo = [
    'Hello',
    'Hi there!!',
    'what is your name?',
    'My name is Edith',
    'how are you?',
    'I am doing great these days',
    'Good to hear',
    'in which city  do you live?',
    'I live in Delhi',
    'in which language you talk?',
    'I mostly talk in English',
    'are you real?',
    'Yeah i am real my buddy.',
    'how old are you?',
    'I am 0.22',
    'where do you live?',
    'In your pc.',
    'how can you help me?',
    'I can help you in any situation by giving you valuable solutions.'
    'How are you? Are you doing ok?',
    'Kitne baar batau bhai,chahta kya h tu finally bolde',
    'What time is it?',





    
]


# In[ ]:


trainer.train(convo)


# In[ ]:


response = bot.get_response('In which city do you live ?')
print(response)


# In[ ]:



print("Hii how are you")
while True:
    query = input()
    if query == 'exit':
        break
    answer = bot.get_response(query)
    print("Edith:", answer)
     


# In[ ]:





# In[ ]:




