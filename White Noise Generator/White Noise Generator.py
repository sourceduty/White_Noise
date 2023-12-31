# White Noise Generator
# Generate custom white noises using Python.
# Copyright (C) 2023, Sourceduty - All Rights Reserved.

import tkinter as tk
from tkinter import ttk
import numpy as np
from scipy.io import wavfile
import os
import random

# Function to generate and save white noise
def generate_white_noise():
    sample_rate = int(sample_rate_entry.get())
    duration = float(duration_entry.get())
    noise_type = noise_type_combo.get()
    
    # Generate white noise
    if noise_type == "Gaussian White Noise":
        noise = np.random.normal(0, 1, int(sample_rate * duration))
    elif noise_type == "Uniform White Noise":
        noise = np.random.uniform(-1, 1, int(sample_rate * duration))
    elif noise_type == "Pink Noise":
        noise = pink_noise(sample_rate, int(sample_rate * duration))
    elif noise_type == "Brownian Noise":
        noise = brown_noise(sample_rate, int(sample_rate * duration))
    
    output_folder = "output"
    os.makedirs(output_folder, exist_ok=True)
    output_filename = os.path.join(output_folder, f"{noise_type.replace(' ', '_').lower()}_noise.wav")
    
    # Save the white noise as a WAV file
    wavfile.write(output_filename, sample_rate, noise)

    result_label.config(text=f"Saved {noise_type} to {output_filename}")

# Function to generate pink noise
def pink_noise(sample_rate, duration):
    pink = np.random.randn(duration)
    pink = np.cumsum(pink)
    pink -= np.mean(pink)
    pink /= np.max(np.abs(pink))
    return pink

# Function to generate brown noise
def brown_noise(sample_rate, duration):
    brown = np.random.randn(duration).cumsum()
    brown -= brown.min()
    brown /= brown.max()
    brown = (brown - 0.5) * 2.0
    return brown

# Function to display noise suggestions
def display_suggestions(event=None):
    selected_noise = noise_type_combo.get()
    suggestions = get_suggestions(selected_noise)
    suggestions_text.config(state='normal')
    suggestions_text.delete('1.0', tk.END)
    suggestions_text.insert(tk.END, suggestions)
    suggestions_text.config(state='disabled')

# Function to populate sample rate suggestions
def populate_sample_rate_suggestions():
    sample_rate_suggestions = "Sample Rate Suggestions:\n"
    sample_rate_suggestions += "44100 Hz - CD quality audio\n"
    sample_rate_suggestions += "48000 Hz - DVD quality audio\n"
    sample_rate_suggestions += "96000 Hz - High-quality audio\n"
    sample_rate_suggestions += "192000 Hz - Studio-quality audio\n"
    suggestions_text.config(state='normal')
    suggestions_text.insert(tk.END, sample_rate_suggestions)
    suggestions_text.config(state='disabled')

# Function to get suggestions based on selected noise type
def get_suggestions(noise_type):
    suggestions = ""
    if noise_type == "Gaussian White Noise":
        suggestions = "Try using a different mean and standard deviation for the Gaussian distribution."
    elif noise_type == "Uniform White Noise":
        suggestions = "Experiment with different amplitude ranges for the uniform distribution."
    elif noise_type == "Pink Noise":
        suggestions = "Adjust the filter parameters for pink noise generation."
    elif noise_type == "Brownian Noise":
        suggestions = "Explore different algorithms for generating Brownian noise."
    
    return suggestions

# Create the main GUI window
window = tk.Tk()
window.title("Noise Generator")

# Set background color to black and text color to white
window.configure(bg='black')

# Padding and spacing for elements
padding = 10
spacing = 5

# Sample Rate
sample_rate_label = ttk.Label(window, text="Sample Rate (Hz):", background='black', foreground='white')
sample_rate_label.grid(row=0, column=0, padx=padding, pady=padding)
sample_rate_entry = ttk.Entry(window, foreground='black')
sample_rate_entry.grid(row=0, column=1, padx=padding, pady=padding)
sample_rate_entry.insert(0, "44100")

# Duration
duration_label = ttk.Label(window, text="Duration (s):", background='black', foreground='white')
duration_label.grid(row=1, column=0, padx=padding, pady=padding)
duration_entry = ttk.Entry(window, foreground='black')
duration_entry.grid(row=1, column=1, padx=padding, pady=padding)
duration_entry.insert(0, "5")

# Noise Type
noise_type_label = ttk.Label(window, text="Noise Type:", background='black', foreground='white')
noise_type_label.grid(row=2, column=0, padx=padding, pady=padding)
noise_type_values = ["Gaussian White Noise", "Uniform White Noise", "Pink Noise", "Brownian Noise"]
noise_type_combo = ttk.Combobox(window, values=noise_type_values, foreground='black')
noise_type_combo.grid(row=2, column=1, padx=padding, pady=padding)
noise_type_combo.set(noise_type_values[0])
noise_type_combo.bind("<<ComboboxSelected>>", display_suggestions)

# Suggestions Text
suggestions_text = tk.Text(window, wrap=tk.WORD, height=5, width=40, background='white', foreground='black', state='disabled')
suggestions_text.grid(row=3, columnspan=2, padx=padding, pady=padding)

# Populate sample rate suggestions when the application starts
populate_sample_rate_suggestions()

# Generate Button
generate_button = ttk.Button(window, text="Generate Noise", command=generate_white_noise)
generate_button.grid(row=4, columnspan=2, padx=padding, pady=padding)

# Result Label
result_label = ttk.Label(window, text="", background='black', foreground='white')
result_label.grid(row=5, columnspan=2, padx=padding, pady=padding)

window.mainloop()
