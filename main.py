
from anime_api import AnimeAPI
from anime_app import menu_principal

def main():
    api = AnimeAPI()
    menu_principal(api)

if __name__ == "__main__":
    main()