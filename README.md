# Instructions to use the gdelt interface and other things

This project looks at usage of poiter generators for generating random text based off news coverage about a particular subject 
The news coverage uses GDELT api to scrape the news articles that deal with some predetermined keywords with source country and language. 
The data is stored in a mongo database and then a LSTM based generator network would be trained on this text. 

# Installation 
To install I recommend using virtualenv to sandbox the installation.
To install virtualenv forllow this [link](https://virtualenv.pypa.io/en/stable/installation/)

Once Virtual env is stalled, create an environment by 
```shell 
virtualenv .env
```
Activate the environment by 
```shell
source .env/bin/activate
```

after creating environment, install dependencies for this project
```shell
pip install -r requirements.txt
```

These steps should set you up for running the project. 

# Mongo config

depending on where the mongo is being run, you will need to point the 
connector to that IP and port. 
Currently this is hardcoded, but will be configurable soon. 
