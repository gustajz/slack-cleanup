# Docker Image for Slack Files Delete

This image use a Python script developed by [@technmsg](https://gist.github.com/technmsg/76c8120425df71a7058e986cca5e4b3f) with little modifications. It's usefull if you don't have python on your PC and loves Docker.

## Using

Before starting you need create a [Legacy Token](https://api.slack.com/custom-integrations/legacy-tokens).

```bash

$ docker run -it --rm gustajz/slack-cleanup -h
usage: slack_delete.py [-h] -t TOKEN [-d DAYS] [-c COUNT]

optional arguments:
  -h, --help            show this help message and exit
  -t TOKEN, --token TOKEN
                        Specifies the OAuth token used for authentication,
                        created at (https://api.slack.com/custom-
                        integrations/legacy-tokens)
  -d DAYS, --days DAYS  Delete files older than x days (optional)
  -c COUNT, --count COUNT
                        Max amount of files to delete at once (optional)
```

```bash
$ docker run -it --rm gustajz/slack-cleanup --token YouSlackAPIToken --days 20
```