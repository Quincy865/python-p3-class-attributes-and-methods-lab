class Song:
    count = 0 
    genres = [] 
    artists = []
    genre_count = {} 
    artist_count = {}  
    
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        """Increments the song count when a new song is created."""
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        """Adds genre to the list of genres only if it's not already present."""
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        """Adds artist to the list of artists only if it's not already present."""
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        """Increments the count for a genre in the genre_count dictionary."""
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        """Increments the count for an artist in the artist_count dictionary."""
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1



ninety_nine_problems = Song("99 Problems", "Jay-Z", "Rap")
song2 = Song("Run This Town", "Jay-Z", "Rap")
song3 = Song("Bohemian Rhapsody", "Queen", "Rock")
song4 = Song("Country Roads", "John Denver", "Country")
song5 = Song("I Will Survive", "Gloria Gaynor", "Disco")


print(Song.count)  
print(Song.genres)  
print(Song.artists) 

