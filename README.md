# 🧙‍♂️ OpenCV Invisibility Cloak

A real-time computer vision project that uses color detection and image manipulation to create an "invisibility cloak" effect, inspired by Harry Potter. This project is built with Python and OpenCV.

---

### ✨ Features

- **Real-Time Performance**: Processes live webcam feed to apply the effect instantly.
- **HSV Color Space**: Uses the HSV color space for robust and reliable color detection under varying lighting conditions.
- **Advanced Masking**: Implements morphological closing (`MORPH_CLOSE`) to create a clean and consistent mask of the cloak.
- **Alpha Blending**: Employs Gaussian blurring on the mask edges to create a smooth, feathered blend between the foreground and background, eliminating jagged edges.

---

### 🎥 Demo

**(This is the most important part! Record a short video of your project working and convert it to a GIF. You can use a free online tool like ezgif.com. Place the GIF in your project folder and uncomment the line below.)**

---

### 🛠️ Technology Stack

- **Python 3.11.4**
- **OpenCV 4.7.0**
- **NumPy**

---
---

### 🚀 How to Run

1.  **Capture the Background:**
    - Stand in front of your webcam and make sure the "cloak" is not in the frame.
    - Run the background capture script. This will open your webcam feed.
    ```bash
    python bg_capture.py
    ```
    - Press **'q'** to capture the background. A `background.png` file will be saved.

2.  **Run the Main Application:**
    - Hold up your colored cloak.
    - Run the main script to see the invisibility effect.
    ```bash
    python invisibility_cloak.py
    ```
    - Press **'q'** to exit the application.

---

### 📜 License

This project is licensed under the MIT License. See the `LICENSE` file for details.
