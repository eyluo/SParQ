import sys
import pprint
import spotipy
import spotipy.util as util
from pqueue import PQueue

SCOPE = 'playlist-modify-public ' + \
        'user-read-currently-playing ' + \
        'user-modify-playback-state'

# given a Spotify object, username, and playlist name, looks for provided
# playlist or creates a new one with the specified name.
def fetchPlaylistID(sp, username, name):
    playlists = sp.current_user_playlists()
    for item in playlists['items']:
        if (item['name'] == name):
            return item['id']

    playlist = sp.user_playlist_create(user=username,
                                       name=name,
                                       public=True)

    pprint.pprint(sp.current_user_playlists())

    return playlist['id']

def main():
    # Step 1: get user and get access token from username
    username = input('Enter username: ')

    token = util.prompt_for_user_token(username, SCOPE)

    if (token):
        # Step 2: get playlist to modify
        sp = spotipy.Spotify(auth=token)

        name = input('Playlist name: ')

        if (name):
            playlistID = fetchPlaylistID(sp, username, name)

        pq = PQueue()

        # Step 3: in a perpetual loop, modify the playlist
        while (True):
            command = input('cmd: ')
            if (command == 'i'):
                keyword = input('Give keyword: ')
                result = sp.search(q=keyword, limit=1)

                trackID = result['tracks']['items'][0]['id']
                
                if (name): 
                    sp.user_playlist_add_tracks(username, playlistID, [trackID])

                out = open('audio-analysis.py', 'w')
                pprint.pprint(sp.audio_analysis(trackID), out)
            elif (command == 's'):
                sp.shuffle(True)
            elif (command == 'pa'):
                sp.pause_playback()
            elif (command == 'pl'):
                sp.start_playback()
            elif (command == 'n'):
                sp.next_track()
            elif (command == 'pr'):
                sp.previous_track()
            elif (command == 'c'):
                currentTrack = sp.current_user_playing_track()
                if (currentTrack != None):
                    print('Currently playing ', currentTrack['item']['name'])
            elif (command == 'r'):
                sp.user_playlist_reorder_tracks(username, playlistID, 3, 0)

        print("Done!")
    else:
        print("Can't get token for", username)

if __name__ == '__main__':
    main()
