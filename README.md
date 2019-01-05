# SParQ: Spotify Party Queue

A Spotify party playlist.

The current plan is to have a long-running process that lets users scan their 
Spotify code or something equivalent to figure out popular tracks that they've 
been listening to as well as give users the ability to influence songs by voting 
them up or down the party queue.

Currently just a concept. At the moment, not immediately feasible... try to
imagine everyone bringing their laptops to a party. Portability will be a focus
once a proof-of-concept has been done.

## Done:

- Implemented a basic script that can generate a playlist and add songs to it 
for an authenticated user.
- Input loop that can control playback, give information, and reorder in a
hard-coded manner.

## To-do:

- Set up sockets so other users can vote on songs.
- Create a buffer to add songs so they can get voted onto the queue after a set
amount of time.
- Use what's been done so far to systematically generate playlists based off of 
user information.
- Investigate audio analysis, maybe find a way to link this to beat detection in 
a room?
- Investigate ways to get user information. QR codes? Usernames?
- Like a million other things.