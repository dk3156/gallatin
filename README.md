# Gallatin

## Setup

### Requirements

* Python 3.10 or higher
* Spotify account and developer app with client id and secret
  * Alternatively, you can use the included sample credentials and account information

### Installation

1. Clone the repository
2. Install the prerequisites with `pip install -r requirements.txt`
3. Run the command `python gallatin.py USERID` where `USERID` is the Spotify user id of the user you want to generate a playlist for
   1. The user ID for the test account is `31zmbimflej3gpsj3yxpwpm4qeyy`
4. The new playlist will be generated in the user's Spotify account

## Test User

username: carosa8039@syinxun.com
password: carosa8039
userid:   31zmbimflej3gpsj3yxpwpm4qeyy

## Supported emotions

* happy
  * Sunny, up to 25C
  * Partly cloudy, any temp
  * Cloudy, 5-25C
* relaxed
* sad
  * Below 5C
* angry
  * Heavy rain
  * Thunder
  * Light/


## Weather

* Temperature
* Raining
* Cloud coverage
* Thunder
* Snow


Your choice: angry
[{'danceability': 0.727, 'energy': 0.834, 'key': 2, 'loudness': -5.851, 'mode': 1, 'speechiness': 0.0496, 'acousticness': 0.165, 'instrumentalness': 0, 'liveness': 0.105, 'valence': 0.816, 'tempo': 131.7, 'type': 'audio_features', 'id': '5RsUlxLto4NZbhJpqJbHfN', 'uri': 'spotify:track:5RsUlxLto4NZbhJpqJbHfN', 'track_href': 'https://api.spotify.com/v1/tracks/5RsUlxLto4NZbhJpqJbHfN', 'analysis_url': 'https://api.spotify.com/v1/audio-analysis/5RsUlxLto4NZbhJpqJbHfN', 'duration_ms': 194120, 'time_signature': 4}]

  SUNNY = 113
  PARTLY_CLOUDY = 116
  CLOUDY = 119
  VERY_CLOUDY = 122
  FOG = 143
  LIGHT_SHOWERS = 176
  LIGHT_SLEET_SHOWERS = 179
  LIGHT_SLEET = 182
  THUNDERY_SHOWERS = 200
  LIGHT_SNOW = 227
  HEAVY_SNOW = 230
  LIGHT_RAIN = 266
  HEAVY_SHOWERS = 299
  HEAVY_RAIN = 302
  LIGHT_SNOW_SHOWERS = 323
  HEAVY_SNOW_SHOWERS = 335
  THUNDERY_HEAVY_RAIN = 389
  THUNDERY_SNOW_SHOWERS = 392
