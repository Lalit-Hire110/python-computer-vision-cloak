import cv2

def capture_background():
    """
    Captures a single frame from the webcam and saves it as 'background.png'.
    The script will display the webcam feed. Press 'q' to capture the frame and exit.
    """
    # Initialize the webcam
    cap = cv2.VideoCapture(0)  # The argument 0 refers to the default webcam

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    print("Press 'q' to capture the background image.")

    while True:
        # Read a new frame from the webcam
        ret, frame = cap.read()

        if not ret:
            print("Error: Could not read frame.")
            break

        # Display the frame in a window
        cv2.imshow("Webcam Feed - Press 'q' to capture background", frame)

        # Check for user input to capture the frame
        if cv2.waitKey(1) & 0xFF == ord('q'):
            # Save the captured frame as 'background.png'
            cv2.imwrite("background.png", frame)
            print("Background image saved as 'background.png'.")
            break

    # Release the webcam and close all windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    capture_background()

# This is some information, File path in which i am doing this project is this: C:\Users\Lalit Hire\OneDrive\Desktop\invi_cloak> 
# My python version is 3.11.4 and opencv version is 4.7.0, Virtual environment is named invi
# File I used to capture image is named bg_capture.py
# main script is named invisibility_cloak.py