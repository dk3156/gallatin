"""
Creates a new playlist for the user matching the passed in mood. Tracks be randomly generated or
derived from the user's saved tracks library.
"""

# Load libraries
import numpy as np
import time
from spotipy_random import get_random


def classify_song(sp, trackURI, model):
    """Given a track URI, return the predicted mood of the song"""
    # track audio features [danceability, energy, valence]
    features = get_audio_features(sp, trackURI)
    if features == []:
        return None  # if audio features are available

    featuresArray = np.asarray([features], dtype=np.float32)
    predictions = model.predict(featuresArray)

    return predictions[0]


def get_user_mood_tracks(sp, mood: str, model, size: int):
    """Given a mood, return a list of songs matching the mood from the user's saved tracks"""

    playlist_songs = []
    offset = 0
    batch_size = 50
    while len(playlist_songs) < size:
        # get next batch of saved track from user
        saved_tracks = sp.current_user_saved_tracks(limit=batch_size, offset=offset)
        offset += batch_size

        if saved_tracks == None:  # if no more tracks
            break

        for track in saved_tracks["items"]:
            # trackURI
            trackURI = track.get("track", {}).get("uri", None)
            if trackURI is None:
                continue

            # classify songs
            predicted_mood = classify_song(sp, trackURI, model)
            if predicted_mood == mood:
                playlist_songs.append(trackURI)

    return playlist_songs


def get_random_mood_tracks(sp, mood: str, model, size: int):
    """Given a mood, return a list of random songs matching the mood"""
    playlistSongs = []
    while len(playlistSongs) < size:
        # random track
        track = get_random(spotify=sp, type="track")
        if track is None:
            continue

        # track uri
        trackURI = track.get("uri", None)
        if trackURI is None:
            continue

        # classify songs
        predicted_mood = classify_song(sp, trackURI, model)
        if predicted_mood == mood:
            playlistSongs.append(trackURI)

    return playlistSongs


def get_audio_features(sp, trackURI):
    """Given a track URI, return the audio features [danceability, energy, valence] of the track"""
    # space time between API calls
    # time.sleep(1)

    features = []
    audio_features = sp.audio_features(trackURI)[0]
    print(audio_features)
    if audio_features != None:
        features.append(audio_features["danceability"])
        features.append(audio_features["energy"])
        features.append(audio_features["valence"])
    return features


def create_playlist(sp, mood, user, tracks):
    """Creates a new playlist for the user given a list of track URIs"""
    # create new playlist for user
    userID = user["id"]
    playlist = sp.user_playlist_create(
        userID, name=f"Gallatin - {mood.capitalize()}", public=True
    )
    playlistID = playlist["id"]

    # add songs to playlist
    sp.user_playlist_add_tracks(userID, playlistID, tracks)


def main(sp, user, model, mood, size=15, mode="random"):
    match mode.lower():
        case "random":
            tracks = get_random_mood_tracks(sp, mood, model, size)
        case "user":
            tracks = get_user_mood_tracks(sp, mood, model, size)
        case _:
            tracks = get_random_mood_tracks(sp, mood, model, size)
    create_playlist(sp, mood, user, tracks)
