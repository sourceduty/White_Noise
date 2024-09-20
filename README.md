![tv](https://github.com/sourceduty/White_Noise/assets/123030236/3c2a0ada-ec46-4a54-a565-e7d4aa300445)

> Generate custom white noises using Python.
#

This program is a graphical user interface (GUI) application for generating and saving different types of white noise audio files. It uses the `tkinter` library to create the GUI, and the `scipy.io.wavfile` and `numpy` libraries to generate and save the noise data. Users can select the noise type (Gaussian White Noise, Uniform White Noise, Pink Noise, or Brownian Noise), set the sample rate and duration, and then generate the corresponding audio file. The program provides suggestions based on the selected noise type and displays them in a text area. When the "Generate Noise" button is clicked, the selected parameters are used to generate the noise, which is then saved as a WAV file in an "output" folder.

The program includes several functions for generating specific types of noise. The `generate_white_noise` function generates the noise based on the user's selection and saves it to a WAV file. The `pink_noise` function creates pink noise using a cumulative sum of random numbers, while the `brown_noise` function generates Brownian noise using a cumulative sum with normalization. The `display_suggestions` function updates the GUI with specific tips based on the selected noise type. Additionally, a sample rate suggestion feature is available, providing information on different audio quality standards. The GUI elements are arranged using a grid layout, and the application runs an event loop to handle user interactions.

#
### Related Links

[Sound](https://github.com/sourceduty/Sound)

***
Copyright (C) 2023,  Sourceduty - All Rights Reserved.
