# Motorsport Software Tools (PyQt5)

A collection of lightweight Python GUI applications built using **PyQt5**, designed to simulate and calculate real-world Formula 1 engineering parameters.

## 1. F1 Strategy & Fuel Calculator
An engineering tool that calculates the minimum fuel mass required for a Grand Prix based on total race laps and average consumption per lap.
* **F1 Regulation Compliance:** Automatically accounts for the mandatory **1.0 kg FIA fuel sample** required at the end of the race.
* **Safety Margin Warning:** Triggers a system warning if the calculated fuel exceeds the official F1 tank limit (110 kg), simulating a scenario where strategic "lift-and-coast" is required.

## How to Run
1. Install requirements: `pip install PyQt5`
2. Run the apps: `python f1 fuel calculator.py`
