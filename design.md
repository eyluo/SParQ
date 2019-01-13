# Design Documentation
In this document, I attempt to map out the architecture for this application.
The code can be split into two main components:

## Client-side

## Server-side

### `main.py`
The crux of the operation. This file contains all of the server code, which 
does the computations and the work to modify the queue accordingly.

Although Spotify provides functionality that allows for the direct modification 
of a playlist, I think it's more effective to just maintain the state on the
server with a self-implemented PQueue and send information to Spotify piece by 
piece. I think it would also be helpful to add songs to a playlist as they get 
played, that way the ephemeral nature of the queue can be preserved in case the 
host wants to save songs.

### `pqueue.py`
A helper file that contains the PQueue implementation. The interface is used
primarily in `main.py`.