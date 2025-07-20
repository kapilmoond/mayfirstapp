# Fyers Historical Data Simulator

This repository contains a simple example script for fetching historical 5-minute candle data for the NSE instrument **Reliance** using the Fyers API **v3**. It also demonstrates how to simulate playback of the candle data at an adjustable speed.

## Requirements

- Python 3.8+
- Fyers API credentials (client ID, redirect URI, and secret key)
- Dependencies listed in `requirements.txt` (includes `fyers-apiv3`)

Install dependencies with:

```bash
pip install -r requirements.txt
```

## Usage

1. Export your Fyers API credentials as environment variables:

```bash
export FYERS_CLIENT_ID="your_client_id"
export FYERS_REDIRECT_URI="https://your-redirect-uri"
export FYERS_SECRET_KEY="your_secret_key"
```

2. Run the simulation script. You will be prompted to log in and provide the authentication code from Fyers:

```bash
python simulate_reliance.py
```

The script fetches Reliance historical data between the hard-coded dates (`2022-01-01` to `2022-12-31`) and prints each candle at twice the normal speed (2x). Adjust the dates or speed in `simulate_reliance.py` as needed.

## Disclaimer

This example is for educational purposes only and demonstrates basic usage of the Fyers API. Ensure you comply with Fyers API terms and conditions when using their services.
