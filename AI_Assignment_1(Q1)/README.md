This folder contains the code to create a messenger bot based on Keyword Macthing and Intent Recognition (no machine learning was used) using [AIML](http://www.aiml.foundation/doc.html). It is an intelligent conversation system similar to ELIZA. The bot is able to provide multiple interactions with the user. The bot can respond to basic human conversations, but is specifically designed to recommend eateries in BITS Pilani, Hyderabad Campus. <br/>

We have created our own corpus for recommending such eateries. The [*basic.aiml*](https://github.com/Abhi-2809/AI-Assignment-Bits-Hyderabad-/blob/main/AI_Assignment_1(Q1)/basic.aiml) files contains the code based on aiml to suggest users what they like to eat based on choice of food they enter. The bot responds to the user by matching the pattern of text user has entered. The bot can also inform the user about the current weather based on city they entered. We use the [OpenWeatherMap API](https://openweathermap.org/api) to retrieve this information

To run the code just run the following commands 
```
 python [test.py](https://github.com/Abhi-2809/AI-Assignment-Bits-Hyderabad-/blob/main/AI_Assignment_1(Q1)/test.py)
```

 
The conversations that take place are stored in the [chats.csv](https://github.com/Abhi-2809/AI-Assignment-Bits-Hyderabad-/blob/main/AI_Assignment_1(Q1)/chats.csv) file. This file keeps a note of the conversation between the huaman and bot.

