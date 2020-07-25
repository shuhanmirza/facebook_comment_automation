# facebook_comment_automation
Your friend just offered to do something silly for commenting in thousands in their post? look no further! You are in the right repo xD 

## overview
It's a simple selenium automation implementation. It logs in your account and then goes to your friends timeline and finds the latest post and starts commenting.

## Prerequisites
- You will need have Python3
- Setup virtualenv and install selenium
```console
your_pc$ virtualenv -p /usr/bin/python3 venv
```
```console
your_pc$ source venv/bin/activate
```
```console
(venv)your_pc$ pip install -r requirements.txt
```
- Have firefox installed
- I used geckodriver for linux. If you run windows, install geckodriver for windows.
- Rename env_sample.json to env.json and configure it with your username,password and target's username

## Running
You will need to add PATH for geckodriver
```console
(venv)your_pc$ export PATH=$PATH:.
```
```console
(venv)your_pc$ python main.py
```

## Process Steps of the bot
- goes to facebook.com
- logs in to your account
- goes to targets's timeline
- selects latest post
- starts commenting random letters
