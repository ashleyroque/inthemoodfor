import spotipy 
from spotipy.oauth2 import SpotifyOAuth

scope = "user-library-read"

sp = spotipy.Spotify(
    auth_manager=spotipy.SpotifyOAuth(
        client_id='551655100e814331881900d1974d10e9',
        client_secret='0e2831cd902643a6a9e0e35b14e96988',
        redirect_uri='http://localhost:8080',    
        scope=scope, 
        open_browser=False
    )
)

# Get the current user's top tracks
# Parameters: limit, offset, time_range
top_tracks = sp.current_user_top_tracks(limit=10, offset=0, time_range='short_term')

# Print out the top tracks
for idx, track in enumerate(top_tracks['items']): 
    print (f"{idx + 1}. {track['name']} by {', '.join([artist['name'] for artist in track['artists']])}")

# Get the current user's top artists
# Parameters: limit, offset, time_range
top_artists = sp.current_user_top_artists(limit=10, offset=0, time_range='short_term')

# Print out the top artists
for idx, artist in enumerate(top_artists['items']): 
    print (f"{idx + 1}. {artist['name']}")

# Analyze mood of top tracks and artists
def analyze_mood(data):
    # Perform sentiment analysis on tracks and artists
    # Determine the mood based on the analysis
    # Placeholder for mood
    mood = 'happy'  # Placeholder mood
    # Map mood to colors
    mood_color_map = {
        'happy': 'yellow',
        'sad': 'blue',
        'energetic': 'red',
        'calm': 'green'
        # Add more mood-color mappings as needed
    }
    # Return the mapped color
    return mood_color_map[mood]

# Analyze mood of top tracks and artists
track_mood = analyze_mood(top_tracks)
artist_mood = analyze_mood(top_artists)

# Output color based on mood
print(f"Aura result based on the tracks you listen to: {track_mood}")
print(f"Aura result based on the artists you listen to: {artist_mood}")







