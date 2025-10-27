import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# --- 1. DEFINE CONSTANTS ---
# These are the calibrated values we found from your room temperature measurement.
SERIES_RESISTOR = 1000.0     # Ohms
THERMISTOR_NOMINAL = 175.5   # Ohms (our calibrated value)
B_COEFFICIENT = 3950.0       # K (a standard value)
T0_KELVIN = 298.15           # 25°C in Kelvin, the reference temperature

# --- 2. LOAD YOUR DATA ---
try:
    df = pd.read_csv('thermistor_data.csv')
except FileNotFoundError:
    print("Error: 'thermistor_data.csv' not found.")
    print("Please save your data from the Arduino Serial Monitor to that file.")
    exit()

# --- 3. CONVERT ADC TO KELVIN ---
# Step 3a: Convert ADC value (0-1023) to Resistance (Ohms)
df['Resistance_Ohm'] = SERIES_RESISTOR * (df['ADC_Value'] / (1023.0 - df['ADC_Value']))

# Step 3b: Convert Resistance to Temperature (Kelvin) using the Steinhart-Hart equation
inverse_temp = (1.0 / T0_KELVIN) + (1.0 / B_COEFFICIENT) * np.log(df['Resistance_Ohm'] / THERMISTOR_NOMINAL)
df['Temperature_K'] = 1.0 / inverse_temp

# --- 4. CREATE THE PLOT ---
plt.figure(figsize=(10, 6))
plt.plot(df['Time_s'], df['Temperature_K'], marker='.', linestyle='-')

# Add labels and a title that match the lab requirements
# **** THIS IS THE REVISED LINE ****
plt.title('Thermistor Temperature vs. Time')
plt.xlabel('Time (seconds)')
plt.ylabel('Temperature (Kelvin)')
plt.grid(True)
plt.tight_layout()

# Display the plot
plt.show()