import csv

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

        pass
    def __str__(self):
        return f"{self.title} by {self.artist}"

class Playlist:
    pass
  
class Favorites:
    def __init__(self):
        self.favorite_songs = []

    def add_to_favorites(self, song):
        self.favorite_songs.append(song)
        print(f"{song} added to favorites.")

    def remove_from_favorites(self, song):
        if song in self.favorite_songs:
            self.favorite_songs.remove(song)
            print(f"{song} removed from favorites.")
        else:
            print(f"{song} is not in favorites.")



class MusicApp:
    def __init__(self):
        self.users = []
        self.current_user = None
        self.songs_data = []
        self.playlist = Playlist()

    def read_users_data(self):
        try:
            with open('users.csv', 'r') as users_file:
                reader = csv.reader(users_file)
                for row in reader:
                    username, password = row
                    self.users.append(User(username, password))

        except FileNotFoundError:
            print("File not found!")

    def write_users_data(self):
        try:
            with open('users.csv', 'w') as users_file:
                writer = csv.writer(users_file)
                for user in self.users:
                    writer.writerow([user.username, user.password])

        except IOError:
            print("Error writing to file!")

    def register(self):
        username = input("Enter a username: ")
        password = input("Enter a password: ")

        self.users.append(User(username, password))
        self.write_users_data()

    def login(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        for user in self.users:
            if user.username == username and user.password == password:
                self.current_user = user
                print(f"Logged in as {user.username}")
                return

        print("Invalid credentials.")

    def read_data(self):
        

        def display_songs(self):
            for song in self.songs_data:
                print(song)

        def search_songs(self, keyword):
            results = [song for song in self.songs_data if keyword.lower() in song.title.lower()]
            if results:
                for result in results:
                    print(result)
            else:
                print(f"No results found for '{keyword}'.")

        
        def display_favorites(self):
            pass  

    def add_song(self):
        self.tittle 
        pass  
    

    def create_playlist(self):
        pass  

    def play_song(self):
        print("Playing song...")

    def pause_song(self):
        print("Pausing song...")

    def stop_song(self):
        print("Stopping song...")

    def reshuffle_playlist(self):
        print("Reshuffling playlist...")

    def repeat_song(self):
        print("Repeating song...")

    def equalizer(self):
        print("Adjusting Equalizer...")

    def main_menu(self):
        if not self.current_user:
            print("\nPlease login or register.")
            print("1. Register")
            print("2. Login")
            print("3. Exit")
            print("Note: The application supports all types of music formats.")
            return False
        else:
            print(f"\nWelcome, {self.current_user.username}!")
            print("1. Display Songs")
            print("2. Add Song")
            print("3. Create Playlist")
            print("4. Favorite")
            print("5. Search song")
            print("6. Exit")
            print("7. Play")
            print("8. Pause")
            print("9. Stop")
            print("10. Reshuffle Playlist")
            print("11. Repeat")
            print("12. EQ")
            print("13. Logout")
            print("Note: The application supports all types of music formats.")
            return True

    def main(self):
        self.read_users_data()
        self.read_data()

        while True:
            logged_in = self.main_menu()

            if not logged_in:
                choice = input("Enter your choice: ")
                if choice == '1':
                    self.register()
                elif choice == '2':
                    self.login()
                elif choice == '3':
                    print("Exiting...")
                    break
                else:
                    print("Invalid choice!")
            else:
                choice = input("Enter your choice: ")
                if choice == '1':
                    self.display_songs()
                elif choice == '2':
                    self.add_song()
                elif choice == '3':
                    self.create_playlist()
                elif choice == '4':
                    self.current_user = None
                    print("Logged out.")
                elif choice == '5':
                    print("Exiting...")
                    break
                elif choice == '6':
                    self.play_song()
                elif choice == '7':
                    self.pause_song()
                elif choice == '8':
                    self.stop_song()
                elif choice == '9':
                    self.reshuffle_playlist()
                elif choice == '10':
                    self.repeat_song()
                elif choice == '11':
                    self.equalizer()
                elif choice == '12':
                    self.favorite()
                elif choice == '13':
                    self.search_songs()
                    
                
                else:
                    print("Invalid choice!")

if __name__ == "__main__":
    music_app = MusicApp()
    music_app.main()
