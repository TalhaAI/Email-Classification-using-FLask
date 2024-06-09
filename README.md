# Email Spam Classifier

## Overview

The Email Spam Classifier is a web application that allows users to input email content and determine whether it is spam or not using a machine learning model. The results of each classification are saved in a database and can be viewed in a history table. Additionally, an API endpoint is provided for integration with other applications.

## Features

- **Email Spam Classification**: Enter email content and classify it as spam or not spam.
- **History**: View all past classification results in a table format.
- **API**: Use an API endpoint to classify email content programmatically.
- **Database Storage**: Save classification results in an SQLite database.

## Setup and Installation

### Prerequisites

- Python 3.6+
- SQLite3

### Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/TalhaAI/Email-Classification-using-FLask
    cd Email-Spam-Classifier
    ```

2. **Create a virtual environment and activate it**:
    ```sh
    python -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required packages**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Set up the database**:
    ```sh
    python setup_database.py
    ```

### Running the Application

1. **Start the Flask application**:
    ```sh
    python app.py
    ```

2. **Open a web browser and go to**:
    ```
    http://localhost:8080
    ```

### Using the Application

1. **Email Classification**:
    - Enter the email content in the provided text area and click "Classify".
    - The result ("Spam" or "Not Spam") will be displayed on the page.

2. **View History**:
    - Click the "History" button to view all past classification results in a table format.

3. **API Endpoint**:
    - **Endpoint**: `/api/predict`
    - **Method**: POST
    - **Payload**: JSON object containing the email content.
        ```json
        {
            "content": "Your email content here"
        }
        ```
    - **Response**: JSON object containing the classification result.
        ```json
        {
            "prediction": "Spam" or "Not Spam",
            "email": "Your email content here"
        }
        ```

## Additional Features

### Gmail Integration

You can extend this project to integrate with Gmail, allowing users to classify their emails directly from their Gmail account.

1. **Enable Gmail API**:
    - Go to the [Google Cloud Console](https://console.cloud.google.com/).
    - Enable the Gmail API and create OAuth 2.0 credentials.
    - Download the `credentials.json` file and place it in the project directory.

2. **Authenticate and Connect to Gmail**:
    - Modify `email_utils.py` to include functions for authenticating with Gmail and fetching emails.

## Future Enhancements

- **User Authentication**: Secure the application by implementing user authentication.
- **Data Visualization**: Add charts and graphs to visualize the classification results.
- **Email Notifications**: Send notifications for classified spam or important emails.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or new features.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contact

For any inquiries or support, please contact:
- **Name**: Talha Anwar
- **Phone**: 0333-4567254
- **Email**: [talhaanwar116official@gmail.com](mailto:talhaanwar116official@gmail.com)
