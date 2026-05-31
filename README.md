# Motorsport Software Tools (PyQt5)

A collection of lightweight Python GUI applications built using **PyQt5**, designed to simulate and calculate real-world Formula 1 engineering parameters.

## 1. F1 Strategy & Fuel Calculator
An engineering tool that calculates the minimum fuel mass required for a Grand Prix based on total race laps and average consumption per lap.
* **F1 Regulation Compliance:** Automatically accounts for the mandatory **1.0 kg FIA fuel sample** required at the end of the race.
* **Safety Margin Warning:** Triggers a system warning if the calculated fuel exceeds the official F1 tank limit (110 kg), simulating a scenario where strategic "lift-and-coast" is required.

## 2. F1 Launch Reaction Tester
A high-precision visual simulation of the official FIA start-light sequence used to test player reflexes.
* **Randomized Asynchronous Delay:** Uses `QTimer` to turn on the 5 red lights sequentially at stable 800ms intervals, followed by a completely randomized delay (1–3 seconds) before "lights out" to prevent predictable patterns.
* **False Start Detection:** Features an automated anti-cheat system that instantly triggers a penalty warning if the player hits the spacebar before the lights officially go out.
* **Vector-Based Rendering:** Utilizes PyQt5's native `QPainter` to render all visual components and start lights programmatically without relying on external image files.

## How to Run
1. Install requirements: `pip install PyQt5`
2. Run the apps: `python f1 fuel calculator.py`
