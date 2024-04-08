# NASA Astronomy Picture of the Day (APOD) Streamlit App

This Streamlit app fetches and displays the Astronomy Picture of the Day (APOD) from NASA's API. It showcases the image, its title, and an explanation provided by NASA.

## Description

The app utilizes the NASA API to dynamically fetch the APOD data and display it on a Streamlit interface. Users can explore different astronomical images and learn about them directly from NASA.

## Features

- Fetches the latest Astronomy Picture of the Day from NASA's API.
- Displays the image along with its title and explanation.

## How to Run

1. Clone this repository.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Obtain an API key from NASA's API [here](https://api.nasa.gov/).
4. Replace the `api_key` variable in the script with your API key.
5. Run the Streamlit app with `streamlit run app.py`.
6. Access the app in your web browser at `http://localhost:8501`.

## Prerequisites

- Python 3.7 or above
- Streamlit
- Requests

## Credits

- [Streamlit](https://streamlit.io/)
- [NASA API](https://api.nasa.gov/)
- [Requests](https://docs.python-requests.org/)
