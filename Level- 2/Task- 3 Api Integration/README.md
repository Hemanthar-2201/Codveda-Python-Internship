# API Integration - API Information Hub

## Description

This project is a menu-driven Python application that interacts with multiple external APIs using the `requests` library.

The application allows the user to:

* Get weather information for selected cities

* Check cryptocurrency information

* Search for books and view their details

The project demonstrates how Python can communicate with external APIs, send GET requests, process JSON responses, and display the retrieved information in a user-friendly format.

## Features

### 1. Weather Information

The weather option allows the user to select a city and retrieve:

* Temperature

* Humidity

* Wind speed

The application uses the Open-Meteo API to fetch the weather data.

Currently available cities:

* Bengaluru

* Mumbai

* Delhi

* Chennai

* Hyderabad

### 2. Cryptocurrency Information

The cryptocurrency option allows the user to check information about:

* Bitcoin

* Ethereum

The application displays:

* Cryptocurrency name

* Symbol

* Current price in USD

* 24-hour percentage change

### 3. Book Search

The book search option allows the user to search for a book by name.

The application displays up to 5 search results with:

* Book title

* Author

* First published year

## Technologies Used

* Python 3

* Requests library

* REST APIs

* JSON

* Command-Line Interface

## APIs Used

### Open-Meteo

Used to retrieve weather information.

### CoinPaprika

Used to retrieve cryptocurrency information.

### Open Library

Used to search for books and retrieve book details.

## Error Handling

The application handles common API and user input errors, including:

* Empty user input

* Invalid menu choices

* Unsupported cities

* Unsupported cryptocurrencies

* Failed API requests

* Connection errors

* Request timeouts

* Invalid JSON responses

* Missing data in API responses

## How to Run

### 1. Install Python

Make sure Python 3 is installed on your computer.

### 2. Install Requests

Open a terminal and run:

```
python -m pip install requests

```

If you are using Python 3.14 on Windows:

```
py -3.14 -m pip install requests

```

### 3. Run the Program

Navigate to the project folder and run:

```
python Api.py

```

Or, if you are using Python 3.14:

```
py -3.14 Api.py

```

## Example Menu

```
----------- API INFORMATION HUB ----------
1. Weather Information
2. Cryptocurrency Information
3. Book Search
4. Exit
___________________________________________
Enter your choice (1-4):

```

## What I Learned

Through this project, I learned how to:

* Use the requests library in Python

* Make GET requests to external APIs

* Send parameters with API requests

* Work with JSON data

* Check HTTP response status codes

* Extract required information from API responses

* Handle API and connection errors

* Create a menu-driven command-line application

* Work with multiple APIs in a single Python program

## Internship

This project was completed as part of my Python Development Internship at Codveda Technologies.