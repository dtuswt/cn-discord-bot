# Auth API (Flask)

This is the backend REST API for the system. It fetches data from DTU Inside and saves user information to a redis database.

## User Security

To make requests to DTU Inside's open API, a study number and a hashed password is required. 
When authorizing with DTU Inside, username and password is needed (i.e. username: `s123456`, password: `mySecurePassword1`).
Then, DTU's authorization service will return some sort of token (i.e. `123456A1-A012-3B34-12AB-A12BC34D3FG7`). 
That token will be saved in the redis database along with the username (`s123456`) and the discord ID (i.e. `JohnDoe#1234`).

As of now (2018-08-28), I don't really know if that token will expire. If it will, I'm afraid that the actual password need to be saved, which rises a few security concers. 
For now though, I'll try only saving the token.

## Development

To develop on the project, you shuld use a virtual environment, and Python 3.6. To set up the virtual environment, and install all the dependencies, simply run:

```bash
virtualenv -p python3.6 venv-api
source venv/bin/activate
pip install -r requirements.txt
```

When you have finished development, run:

```bash
deactivate
```

to deactivate the virtual environemnt.

**Note:** that this virtual environment differs from that in the [discord-bot](https://github.com/dtuswt/cn-discord-bot/tree/master/discord-bot).

## Running the Project

Easiest way is to go back a directory and run:

```bash
docker-compose up # or start if you have executed up once before
```

That will start up the entire project, not that you will probably get an error in the [discord-bot](https://github.com/dtuswt/cn-discord-bot/tree/master/discord-bot), though this will also startup a redis database, which is needed for the API to work.

The docker container will automatically take care of the virtual environment and install all the needed dependencies.
