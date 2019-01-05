import sys
import pprint
import spotipy
import spotipy.util as util

SCOPE = 'playlist-modify-public user-read-currently-playing'

def main():
    username = input('Enter username: ')

    token = util.prompt_for_user_token(username, SCOPE)

    if (token):
        sp = spotipy.Spotify(auth=token)
        currentTrack = sp.current_user_playing_track()
        if (currentTrack != None):
            print('Currently playing ', currentTrack['item']['name'])
        name = input('Playlist name: ')

        if (len(name) > 0):
            playlist = sp.user_playlist_create(user=username,
                                    name=name, 
                                    public=True)

        while (True):
            keyword = input('Give keyword: ')
            result = sp.search(q=keyword, limit=1)

            trackID = result['tracks']['items'][0]['id']
            
            # sp.user_playlist_add_tracks(username, playlist['id'], [trackID])

            pprint.pprint(sp.audio_analysis(trackID))

        print("Done!")
    else:
        print("Can't get token for", username)

if __name__ == '__main__':
    main()
