# DTU Inside Discord Bot

This bot can access DTU Inside and retrieve information such as upcomming assignments etc. It will also be able to list what is on the menu in the cantines etc.

## General Structure

The project is split up in three parts:

- [auth-api](https://github.com/dtuswt/cn-discord-bot/tree/master/auth-api) (The backend which stores user information - Python Flask)
- [discord-bot](https://github.com/dtuswt/cn-discord-bot/tree/master/discord-bot) (The actual bot - Python)
- web (Frontend, not created yet - React)

## Running Project

Docker is used to run the project. That makes deployment really easy. To run the project, make sure that Docker is installed on your system.

### Install Docker

Docker (<https://www.docker.com/>) is a simply way of running containers. Installation is easy:

- [Docker for Mac](https://docs.docker.com/docker-for-mac/install)
- [Docker for Windows](https://docs.docker.com/docker-for-windows/install/)

**Mac Tip:** If you are using MacOS and have [homebrew](https://brew.sh/) installed, simply run:

```bash
brew cask install docker
```

### Start the Project

When Docker is installed, simply open a terminal (or cmd/powershell), navigate to the project, and execute:

```bash
docker-compose up
```

If you have executed that command before, use

```bash
docker-compose start
```

to start the project, and

```bash
docker-compose stop
```

to stop the project.

The command will start the python api, discord bot and a redis database.

**Important:** You will probably get an error with the discord bot. Read the readme.md in [discord-bot](https://github.com/dtuswt/cn-discord-bot/tree/master/discord-bot) to see how to run the bot.

## License

The project is licensed under the [MIT License](https://github.com/dtuswt/cn-discord-bot/tree/master/LICENSE).
