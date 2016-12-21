# Docker Image for Slack Files Delete

This image use a Python script developed by [@egermano](https://github.com/egermano). You can access the source [here](https://github.com/egermano/slack-files-delete).
It's usefull if you don't have python on your PC and loves Docker.

## Using

Before starting you need create a [Slack API Token](https://api.slack.com/web#authentication).

````bash
docker run -it --rm -e TOKEN=YouSlackAPIToken -e DAYS=30 gustajz/slack-cleanup
````