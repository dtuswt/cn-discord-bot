# Discord Bot

This is the actual discord bot for the system. This is the code that connects to Discord, and logs in to the servers.

## Development

To develop on the project, you shuld use a virtual environment, and Python 3.6. To set up the virtual environment, and install all the dependencies, simply run:

```bash
virtualenv -p python3.6 venv
source venv/bin/activate
pip install -r requirements.txt
```

When you have finished development, run:

```bash
deactivate
```

to deactivate the virtual environemnt.

**Note:** that this virtual environment differs from that in the [auth-api](https://github.com/dtuswt/cn-discord-bot/tree/master/auth-api).

## Running the Project

To run the project, you need a token for the bot. The token used to connect to the `DTU Compute` discord server is a secret, and will not be shared. If you want to try it out though, you can create your own bot at <https://discordapp.com/developers/applications/me>, get a token and use that. 

You need to create a file called `token.txt` and put it in this folder. The file should have the token inside, and **nothing more**.

To start the program, make you that you have activated the virtual environment (`source venv/bin/activate`). Then simply run:

```bash
python main.py
```

to execute start the bot, or go back a directory (to the root of the git repository) and run:

```bash
docker-compose up # or start if you have executed up once before
```

**Note:** that if you choose to use docker-compose, the entire project will be executed, and you don't need to be in the virtual environment, since the docker container takes care of that part.
