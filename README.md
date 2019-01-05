# SParQ: Spotify Party Queue

## Intro:

Imagine, if you will, that you're at a house party. You walk in, and to your
disgust, they _aren't_ playing the Yeehaw remix of "Wonderwall" by Oasis. You 
don't know who the host is; in fact, you don't know **anyone** there (except for
your friend Cyrus). If only there were a way to take musical matters into your 
own hands and turn this pedantic, poor playlist into the ultimate party queue.

Boy, do I have a solution for you. 

**Introducing SParQ: the Spotify Party Queue.** Powered by the beauty that is 
Spotify's Python API ([**Spotipy**](https://github.com/plamere/spotipy), check 
it out!), SParQ is designed to put the power of the queue in the hands of the people.

The current plan is to have a long-running process that lets users scan their 
Spotify code or something equivalent to figure out popular tracks that they've 
been listening to as well as give users the ability to select songs to put on 
wait, get the songs voted onto the queue, and then rearrange the queue by voting 
songs up or down.

The code right now is in very very early stages. As I'm getting used to Spotipy
and project-level coding for this personal project, I'm trying to use this as a
learning experience as well as something I could see myself using in the future.

## Installation:

After cloning the repo, run the following to install dependencies:

```
pip3 install --user -r requirements.txt
```

Spotipy hasn't been updated with pip3, so you're going to have to manually
install the newest version of Spotipy with:

```
pip3 install --user git+https://github.com/plamere/spotipy.git --upgrade
```

To run this code, simply `cd` into your working directory and run:

```
python3 main.py
```

## Features:

- Implemented a basic script that can generate a playlist and add songs to it 
for an authenticated user.
- Input loop that can control playback, give information, and reorder in a
hard-coded manner.

## To-do:

- Use what's been done so far to systematically generate playlists based off of 
user information.
- Set up sockets so other users can vote on songs.
- Create a buffer to add songs so they can get enter the queue after a set
amount of time/number of votes.
- Investigate audio analysis, maybe find a way to link this to beat detection in 
a room?
- Investigate ways to get user information and authentication. QR codes? 
Usernames?