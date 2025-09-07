import cv2
import numpy as np

def invisibility_cloak():
    """
    Creates a refined invisibility cloak effect using alpha blending for smooth edges.
    """
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    try:
        background = cv2.imread('background.png')
    except:
        print("Error: Could not read background.png.")
        return
        
    # Resize the background to match the webcam frame sizeSSSSSSSs
    ret, frame = cap.read()
    if not ret:
        print("Error: Can't read from webcam.")
        return
    background = cv2.resize(background, (frame.shape[1], frame.shape[0]))

    print("Starting Improved Invisibility Cloak. Press 'q' to exit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # --- Color Range for your Cloak (from your findings) ---
        lower_red1 = np.array([0, 78, 0])
        upper_red1 = np.array([10, 255, 255])
        mask1 = cv2.inRange(hsv, lower_red1, upper_red1)

        lower_red2 = np.array([140, 78, 0])
        upper_red2 = np.array([179, 255, 255])
        mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
        
        mask = mask1 + mask2

        # --- Step 1: Refine the Mask ---
        # Use Morphological Closing to fill holes in the mask for better consistency
        kernel = np.ones((5, 5), np.uint8)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel, iterations=2)

        # --- Step 2: Feather the Mask for Smooth Blending ---
        # Apply a Gaussian blur to the mask to create soft edges
        mask_blurred = cv2.GaussianBlur(mask, (15, 15), 0)
        
        # Normalize the blurred mask to be in the range 0.0 to 1.0
        mask_normalized = mask_blurred / 255.0
        
        # Resize mask_normalized to 3 channels to use it for blending
        mask_stacked = np.dstack([mask_normalized] * 3)

        # --- Step 3: Combine Images with Alpha Blending ---
        # Create the inverse of the mask
        mask_inv = 1.0 - mask_stacked

        # Blend the frame and the background
        # background * mask + frame * (1 - mask)
        foreground = frame.astype(float) * mask_inv
        cloak_area = background.astype(float) * mask_stacked
        
        final_output = cv2.add(foreground, cloak_area).astype(np.uint8)

        cv2.imshow("Invisibility Cloak (Improved)", final_output)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    invisibility_cloak()