mastermind
==========

# Screenshoot #

![mastermind](https://github.com/frosch03/mastermind/blob/master/mastermind.png)

# Downloading #

Just simply clone the git repository:

    git clone https://github.com/frosch03/mastermind.git


# Installing #

On the python side you must have

* python2.7
* cherrypy
* json

On the node side you should do something like:

    cd mastermind/client
    node install
    bower install
    grunt serve

# API #

## /new ##

Reset the server, or start a new game.


## /get ##

Return the current game state as json. The state contains:

* status: [running|end]
* ttl: [0-9]
* board: list of:

    * move: list of [1-6]
    * result: ( [0-4] , [0-4] )


## /move ##

Set a new combination. This POST request sends the request with it's
request-header. The result is an updated game state as json. The state
contains:

* status: [running|end]
* ttl: [0-9]
* board: list of:

    * move: list of [1-6]
    * result: ( [0-4] , [0-4] )
