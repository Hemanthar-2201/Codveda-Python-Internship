import requests

def get_weather():
    print()
    print("\n---------------------- WEATHER INFORMATION ----------------------")
    
    print("\nAvailable cities: Bengaluru, Mumbai, Delhi, Chennai, Hyderabad")

    city = input("Enter city name: ").strip()

    if not city:
        print("City name cannot be empty.")
        return

    locations = {
        "bengaluru": (12.9716, 77.5946),
        "mumbai": (19.0760, 72.8777),
        "delhi": (28.6139, 77.2090),
        "chennai": (13.0827, 80.2707),
        "hyderabad": (17.3850, 78.4867)
    }

    city_key = city.lower()

    if city_key not in locations:
        print("City not available in this program.")
        print("Available cities:", ", ".join(locations.keys()))
        return

    latitude, longitude = locations[city_key]

    # API endpoint for Open-Meteo to get weather details
    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,relative_humidity_2m,wind_speed_10m",
        "timezone": "auto"
    }

    try:
        response = requests.get(url, params=params, timeout=10)

        if response.status_code != 200:
            print("Failed to fetch weather data.")
            print("Status code:", response.status_code)
            return

        data = response.json()

        if "current" not in data:
            print("Invalid response received from the weather API.")
            return

        current = data["current"]

        temperature = current.get("temperature_2m", "Unknown")
        humidity = current.get("relative_humidity_2m", "Unknown")
        wind_speed = current.get("wind_speed_10m", "Unknown")

        print()
        print("\n------------ Weather Details ------------")
       
        print("City:", city.title())
        print("Temperature:", temperature, "°C")
        print("Humidity:", humidity, "%")
        print("Wind Speed:", wind_speed, "km/h")
        print("________________________________________")

    except requests.exceptions.Timeout:
        print("The request took too long. Please try again.")

    except requests.exceptions.ConnectionError:
        print("Could not connect to the weather API.")
        print("Please check your internet connection.")

    except requests.exceptions.RequestException as error:
        print("An error occurred while contacting the API.")
        print("Error:", error)

    except ValueError:
        print("The API returned invalid JSON data.")


def get_crypto_price():
    print()   
    print("\n------ CRYPTOCURRENCY INFORMATION ------")
    

    crypto = input("Enter cryptocurrency (bitcoin/ethereum): ").strip().lower()

    crypto_ids = {
        "bitcoin": "btc-bitcoin",
        "ethereum": "eth-ethereum"
    }

    if crypto not in crypto_ids:
        print("Cryptocurrency not available.")
        print("Available options: bitcoin, ethereum")
        return

    coin_id = crypto_ids[crypto]

    #API endpoint for CoinPaprika to get cryptocurrency details
    url = f"https://api.coinpaprika.com/v1/tickers/{coin_id}"

    try:
        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            print("Failed to fetch cryptocurrency data.")
            print("Status code:", response.status_code)
            return

        data = response.json()

        if "quotes" not in data:
            print("Invalid response received from the cryptocurrency API.")
            return

        usd_data = data["quotes"].get("USD")

        if not usd_data:
            print("USD price information is not available.")
            return

        price = usd_data.get("price")
        change_24h = usd_data.get("percent_change_24h")

        print()
        print("\n-------- Cryptocurrency Details --------") 
    
        print("Name:", data.get("name", "Unknown"))
        print("Symbol:", data.get("symbol", "Unknown"))
        print("Price (USD):", price)
        print("24 Hour Change:", change_24h, "%")
        print("________________________________________")

    except requests.exceptions.Timeout:
        print("The request took too long. Please try again.")

    except requests.exceptions.ConnectionError:
        print("Could not connect to the cryptocurrency API.")
        print("Please check your internet connection.")

    except requests.exceptions.RequestException as error:
        print("An error occurred while contacting the API.")
        print("Error:", error)

    except ValueError:
        print("The API returned invalid JSON data.")


def search_books():
    print()
    print("\n--------------- BOOK SEARCH ---------------")
   

    book_name = input("Enter the name of a book: ").strip()

    if not book_name:
        print("Book name cannot be empty.")
        return

    url = "https://openlibrary.org/search.json"

    params = {
        "q": book_name,
        "limit": 5
    }

    try:
        response = requests.get(url, params=params, timeout=10)

        if response.status_code != 200:
            print("Failed to fetch book data.")
            print("Status code:", response.status_code)
            return

        data = response.json()

        if "docs" not in data:
            print("Invalid response received from the API.")
            return

        books = data["docs"]

        if not books:
            print("No books found for:", book_name)
            return

        print()
        print("\n------------- SEARCH RESULTS -------------")
       

        for index, book in enumerate(books, start=1):

            title = book.get("title", "Unknown")

            authors = book.get(
                "author_name",
                ["Unknown"]
            )

            year = book.get(
                "first_publish_year",
                "Unknown"
            )

            print(f"\nBook {index}")
            print("_____________________________")
            print("Title:", title)
            print("Author:", ", ".join(authors))
            print("First Published:", year)

    except requests.exceptions.Timeout:
        print("The request took too long. Please try again.")

    except requests.exceptions.ConnectionError:
        print("Could not connect to the book API.")
        print("Please check your internet connection.")

    except requests.exceptions.RequestException as error:
        print("An error occurred while contacting the API.")
        print("Error:", error)

    except ValueError:
        print("The API returned invalid JSON data.")


def main():

    while True:

        
        print("\n----------- API INFORMATION HUB ----------")
        
        print("1. Weather Information")
        print("2. Cryptocurrency Information")
        print("3. Book Search")
        print("4. Exit")
        print("___________________________________________")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            get_weather()

        elif choice == "2":
            get_crypto_price()

        elif choice == "3":
            search_books()

        elif choice == "4":
            print("\nThank you for using the API Information Hub.")
            print("Goodbye!")
            break

        else:
            print("\nInvalid choice. Please enter a number from 1 to 4.")


if __name__ == "__main__":
    main()
