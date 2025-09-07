import cv2
import numpy as np

def nothing(x):
    """A dummy callback function for the trackbars."""
    pass

def find_hsv_range():
    """
    Initializes a webcam feed and creates a window with trackbars to find
    the optimal HSV range for color detection.
    """
    # Initialize the webcam
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    # Create a window to hold the trackbars
    cv2.namedWindow("Trackbars")
    cv2.resizeWindow("Trackbars", 600, 300)

    # Create trackbars for Hue, Saturation, and Value
    # Hue has a range of 0-179 in OpenCV
    cv2.createTrackbar("Hue Min", "Trackbars", 0, 179, nothing)
    cv2.createTrackbar("Hue Max", "Trackbars", 179, 179, nothing)
    # Saturation and Value have a range of 0-255
    cv2.createTrackbar("Sat Min", "Trackbars", 0, 255, nothing)
    cv2.createTrackbar("Sat Max", "Trackbars", 255, 255, nothing)
    cv2.createTrackbar("Val Min", "Trackbars", 0, 255, nothing)
    cv2.createTrackbar("Val Max", "Trackbars", 255, 255, nothing)

    print("Adjust the sliders to isolate the cloak color. Press 'q' to exit.")

    while True:
        # Read a frame from the webcam
        ret, frame = cap.read()
        if not ret:
            break

        # Convert the frame to HSV color space
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Get the current positions of the trackbars
        h_min = cv2.getTrackbarPos("Hue Min", "Trackbars")
        h_max = cv2.getTrackbarPos("Hue Max", "Trackbars")
        s_min = cv2.getTrackbarPos("Sat Min", "Trackbars")
        s_max = cv2.getTrackbarPos("Sat Max", "Trackbars")
        v_min = cv2.getTrackbarPos("Val Min", "Trackbars")
        v_max = cv2.getTrackbarPos("Val Max", "Trackbars")

        # Create the lower and upper HSV range arrays
        lower_range = np.array([h_min, s_min, v_min])
        upper_range = np.array([h_max, s_max, v_max])

        # Create a mask using the specified HSV range
        mask = cv2.inRange(hsv, lower_range, upper_range)

        # Create a result image by applying the mask to the original frame
        result = cv2.bitwise_and(frame, frame, mask=mask)

        # Display the original, mask, and result frames
        cv2.imshow("Original Frame", frame)
        cv2.imshow("Mask (Cloak should be white)", mask)
        cv2.imshow("Result (Isolated Color)", result)

        # Exit loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            # Print the final values before exiting
            print("\nFinal HSV Values:")
            print(f"Lower Range: np.array([{h_min}, {s_min}, {v_min}])")
            print(f"Upper Range: np.array([{h_max}, {s_max}, {v_max}])")
            break

    # Clean up
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    find_hsv_range()