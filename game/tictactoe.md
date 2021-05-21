# Earnest Research Software Engineer Exercise

![Tic Tac Toe logo](logo.png)

## Task
Design and implement a [tic-tac-toe](https://en.wikipedia.org/wiki/Tic-tac-toe) game.

Assume that players' moves are random and for that purpose use the provided [Random Service](#random-service).

**Important**: We are looking for a solution that follows Functional Programming principles (like avoiding mutation, isolating side-effects etc.).
Please aim for simplicity.

You can use any programming language of your choice. However ideally use a language that has good support for Functional Programming.

## Submission
We utilize Github and [pull requests](https://help.github.com/articles/creating-a-pull-request/) for collaborating on code. Create a new [branch](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging) for your submission.

You have 7 days from the time that you receive the take-home to submit. Please do not spend more than three or four hours (and ideally much less) on the project and feel free to submit your solution early if finished ahead of the 7-day deadline.

Please make sure to document how to run your exercise as well as any other information or consideration you think is relevant. When you are ready to submit, open a pull request against the master branch.

## Random Service
The [Random Service](https://github.com/brendanmaguire/random) can be run locally as a Docker container. It should be queried in order to determine the moves of the players in the game.

### Prerequisites
* [Docker Compose](https://docs.docker.com/compose/install/)

### Running
Bring up the Docker container:
```
docker-compose up
```

Query the API when the container is running:
```
curl 'http://localhost:5000/random/choice?value=1&value=2&value=3'
{"value":"3"}
```

View the Swagger Spec for the service:
```
curl http://localhost:5000/swagger.yaml
```
