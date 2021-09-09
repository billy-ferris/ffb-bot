FROM python:latest

# Install app
ADD . /usr/src/ffb-bot
WORKDIR /usr/src/ffb-bot
RUN python3 setup.py install

# Launch app
CMD ["python3", "ffb_bot/ffb_bot.py"]