Project 1: Passive Classification
Goal: Sort raw data into logical categories.
Steps to Run:
Open your Python script/notebook.
Define your Item Database (e.g., a list of movies or products with tags).
Run the Classification Cell.
Output: Observe the console as the system automatically organizes the items based on their intrinsic properties.
Project 2: Active Prediction
Goal: Align a "User State" with a specific database result.
Steps to Run:
Define a variable called user_preferences.
Run the Similarity Logic function.
Output: The system will print the single most relevant item that matches the user's input.
Project 3: Movie Recommendation Engine
Goal: Generate a ranked Top-N List using Vector Mapping.
Steps to Run:
Execute the cell containing the vectorize function.
Run the Input Block: A prompt will appear asking: "Enter genres you like (separated by commas):".
Type your genres (e.g., Action, Sci-Fi) and press Enter.
Output: The engine will display your "Top-3 Recommendations" with their corresponding Jaccard Similarity scores.
Project 4: Image Recognition (Mastery Phase)
Goal: Integrate a pre-trained model to classify real-world images.
Steps to Run:
Upload your image: Click the Folder Icon in the Colab sidebar and upload a .jpg or .png file.
Copy Path: Right-click the file and select "Copy Path".
Update Code: Paste the path into the local_path variable (e.g., local_path = '/content/dog.jpg').
Run the cell.

Output: An image will appear with a title showing the AI's Prediction and the Confidence Percentage.
