# Emailer Assistant

## Overview

Emailer Assistant is a comprehensive solution designed to automate the process of scheduling meetings and managing emails. It leverages Google's Gmail and Calendar APIs to fetch, read, and send emails, as well as to schedule meetings based on free time slots. The project is built using Python for backend logic and JavaScript for the web server and database connectivity.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

### Python Modules

- **Calendar API**: Initializes Google Calendar API and fetches free time slots.
- **Gmail API**: Initializes Gmail API, reads emails, and sends replies.
- **Meet Scheduler**: Schedules meetings based on free time and replies.
- **Responser**: Generates responses for scheduling meetings.
- **Services**: Sets up Google services for Gmail and Calendar.
- **Testing**: Tests fetching free time from Google Calendar.

### JavaScript Modules

- **DB**: Connects to MongoDB database.
- **Server**: Sets up the Express server.
- **Routes**: Defines routes for the web application.
- **User Model**: Defines the User schema for MongoDB.

## Prerequisites

- Python 3.x
- Node.js
- MongoDB
- Google API credentials

## Installation

1. **Clone the Repository**

    ```bash
    git clone https://github.com/shadowaxe99/emailer-assistant.git
    ```

2. **Navigate to the Directory**

    ```bash
    cd emailer-assistant
    ```

3. **Install Python Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Install Node Dependencies**

    ```bash
    npm install
    ```

5. **Set up Google API Credentials**

    - Place your `credentials.json` for Google API in the root directory.

6. **Start the Server**

    ```bash
    npm start
    ```

## Usage

- Run the Python scripts for various functionalities like email reading, meeting scheduling, etc.
- Use the web interface for managing emails and calendar events.

## Contributing

Contributions are welcome! Please read the [contributing guidelines](CONTRIBUTING.md) to get started.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE.md) file for details.

---

For more information, please refer to the [documentation](docs/).

Feel free to raise issues or submit pull requests. Happy coding!
