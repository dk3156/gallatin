# '''
# This is the main file for the application. This application will
# create playlists for specific moods for a certain user using their own music.
# The user can either manually input their mood or the program will use a facial
# recognition API to detect the mood of the user by taking a picture of them
# after they have provided the program with all user scopes required. The program
# uses machine learning on a training set created using Last.fm tags and features
# about the songs obtained through Spotify to create the playlist for the user to
# try and classify the user's music into specific moods. 

# In order to run the application, you must supply your unique user ID as the
# second argument in the terminal. Example:python spotify.py userID 
# This file defines the user scopes and prompts a user for their token 
# in order to access their data. The program will run until the user manually
# quits the program using 1. 
# '''
# #Load libraries
# import sys
# import json
# import spotipy
# import spotipy.util as util
# import os
# import getMood
# import createPlaylist
# import getTrainingData
# import learnSongs

# CLIENT_ID = 'ce931c51bc334b5288daa5e5ba897d5a'
# CLIENT_SECRET = '26fb987dce6d4294ae77d5da59ab2a73'

# # id: 563f890f0bc540309c44d40e35a0a462
# # secret: 343030b9e9d0440b80bebb96647485af

# def get_token(username):
#     token = ""
#     scopes = ("user-read-recently-played"
# 			" user-top-read"
# 			" user-library-modify"
# 			" user-library-read"
# 			" user-read-private"
# 			" playlist-read-private"
# 			" playlist-modify-public"
# 			" playlist-modify-private"
# 			" user-read-email"
# 			" user-read-private"
# 			" user-read-playback-state"
# 			" user-modify-playback-state"
# 			" user-read-currently-playing"
# 			" app-remote-control"
# 			" streaming"
# 			" user-follow-read"
# 			" user-follow-modify")
#     try:
#         token = util.prompt_for_user_token(username,scopes,
# 									client_id=CLIENT_ID,
# 									client_secret=CLIENT_SECRET,
# 									redirect_uri='http://google.com/')
#     except:
#         os.remove(".cache-{}".format(username))
#         token = util.prompt_for_user_token(username,scopes,
# 									client_id=CLIENT_ID,
# 									client_secret=CLIENT_SECRET,
# 									redirect_uri='http://google.com/')
        
#     return token
   
# def generate_song(token, usermood):
#     if token != "":
#         sp = spotipy.Spotify(auth=token)
#         user = sp.current_user()
#         if usermood != '':
#             mood = usermood
#         else:
#             mood = getMood.getMood()
#         model = learnSongs.main()
#         createPlaylist.main(sp, user, model, mood)
#         return True
#     else:
#         return False