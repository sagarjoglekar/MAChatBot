#Instructions to use the gdelt interface and other things

This project looks at usage of poiter generators for generating random text based off news coverage about a particular subject 
The news coverage uses GDELT api to scrape the news articles that deal with some predetermined keywords with source country and language. 
The data is stored in a mongo database and then a LSTM based generator network would be trained on this text. 

#Installation 
To install I recommend using virtualenv to sandbox the installation.
To install virtualenv forllow this [link](https://virtualenv.pypa.io/en/stable/installation/)

Once Virtual env is stalled, create an environment by 
```shell 
virtualenv .env
```
