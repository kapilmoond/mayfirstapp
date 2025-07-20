#!/usr/bin/env python3
"""Fetch and simulate Reliance 5-minute historical data using Fyers API v3."""

import os
import time
import pandas as pd
from fyers_apiv3.fyersModel import FyersModel, SessionModel


def get_fyers(client_id: str, redirect_uri: str, secret_key: str) -> FyersModel:
    """Authenticate and return a FyersModel instance."""
    session = SessionModel(
        client_id=client_id,
        secret_key=secret_key,
        redirect_uri=redirect_uri,
        response_type="code",
        grant_type="authorization_code",
    )
    print("Open the URL below in your browser to log in and authorize:")
    print(session.generate_authcode())
    auth_code = input("Enter the auth code from the redirect URL: ")
    session.set_token(auth_code)
    token_response = session.generate_token()
    access_token = token_response["access_token"]
    return FyersModel(client_id=client_id, token=access_token)


def fetch_history(fyers: FyersModel, start: str, end: str) -> pd.DataFrame:
    """Retrieve 5-minute historical data for Reliance."""
    response = fyers.history(
        data={
            "symbol": "NSE:RELIANCE-EQ",
            "resolution": "5",
            "date_format": "1",
            "range_from": start,
            "range_to": end,
            "cont_flag": "1",
        }
    )
    if response.get("s") != "ok":
        raise RuntimeError(f"API error: {response}")
    df = pd.DataFrame(
        response["candles"],
        columns=["timestamp", "open", "high", "low", "close", "volume"],
    )
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="s")
    return df


def simulate(df: pd.DataFrame, speed: float = 1.0) -> None:
    """Print each row of data at the given speed."""
    delay = 5.0 / speed
    for _, row in df.iterrows():
        print(row.to_dict())
        time.sleep(delay)


def main() -> None:
    client_id = os.getenv("FYERS_CLIENT_ID")
    redirect_uri = os.getenv("FYERS_REDIRECT_URI")
    secret_key = os.getenv("FYERS_SECRET_KEY")
    if not all([client_id, redirect_uri, secret_key]):
        raise SystemExit(
            "Set FYERS_CLIENT_ID, FYERS_REDIRECT_URI, and FYERS_SECRET_KEY environment variables"
        )

    fyers = get_fyers(client_id, redirect_uri, secret_key)
    df = fetch_history(fyers, start="2022-01-01", end="2022-12-31")
    simulate(df, speed=2.0)  # 2x real time


if __name__ == "__main__":
    main()
