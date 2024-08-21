# Vertex Insight: Your Voice Matters

Welcome to the Vertex Insight repository! Before you can start using the app, please follow these instructions carefully.

## Prerequisites
- Make sure you have the latest version of Python installed on your system.
- (Optional) Create a virtual environment.

## Installation
1. Clone or download this repository to your local machine.
2. Open a terminal or command prompt and navigate to the project's root directory.

   ```shell
   cd path/to/Vertex Insight

3. Install the required libraries from the requirements.txt file using pip:

   ```shell
   pip install -r requirements.txt

### Database Setup
To set up the database for the app, run the following command:

    python create_database.py

### Dataset Setup
Open "Engine/candidate/" and copy the path for the file "combined.csv".
Then open dataset-to-database.py and change the value of dataset_path to the one you copied.

    dataset_path: str = # Enter path to combined.csv here

To copy the data from the dataset to the database, run the following command:

    python dataset-to-database.py

### Running the App

The next time you run the app you may simply use the command:

    python app.py

The app should now be accessible by visiting http://localhost:8080 in your web browser.

## License

[MIT](https://choosealicense.com/licenses/mit/)

