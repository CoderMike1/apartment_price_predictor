# -*- coding: utf-8 -*-
import joblib
import pandas as pd

def predict_price(district_id, rooms, furnitured, meters):
    rf_model = joblib.load("rf_model.pkl")
    new_ap = pd.DataFrame(
        {
            "district_encoded":[int(district_id)],
            "numberOfRooms":[int(rooms)],
            "meters":[meters],
            "furniture":[int(furnitured)]
        }
    )

    estimated_price = int(rf_model.predict(new_ap)[0])
    formatted_estimated_price = f"{estimated_price:,}".replace(",", " ")

    return formatted_estimated_price