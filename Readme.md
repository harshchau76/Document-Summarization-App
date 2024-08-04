# Document Summarization App

## Overview
This project implements a web application that allows users to upload documents and receive summarized versions using a locally deployed Language Model (LLM). The backend is built with FastAPI, while the frontend is developed using React. Docker is used for local deployment of the entire application.

## Directory Structure
document-summarization-app/
├── backend/
│ ├── app/
│ │ ├── init.py
│ │ ├── main.py
│ │ ├── models.py
│ │ ├── routes.py
│ │ └── utils.py
│ ├── Dockerfile
│ └── requirements.txt
├── frontend/
│ ├── public/
│ │ └── index.html
│ ├── src/
│ │ ├── components/
│ │ │ ├── FileUpload.js
│ │ │ ├── Summarize.js
│ │ │ └── App.js
│ │ ├── App.css
│ │ └── index.js
│ ├── Dockerfile
│ └── package.json
├── docker/
│ └── docker-compose.yml
├── README.md
└── .gitignore


## Setup and Running the Application

### Prerequisites
- Docker
- Docker Compose

### Steps

1. **Clone the repository:**
    ```sh
    git clone <repository-url>
    cd document-summarization-app
    ```

2. **Build and run the Docker containers:**
    ```sh
    cd docker
    docker-compose up --build
    ```

3. **Access the application:**
    - Frontend: [http://localhost:3000](http://localhost:3000)
    - Backend: [http://localhost:8000/docs](http://localhost:8000/docs)

## Backend
The backend is built using FastAPI and is responsible for handling file uploads and summarizing documents using a locally deployed Language Model.

### Endpoints
- `POST /upload`: Handle file uploads (PDF, DOCX, TXT).
- `POST /summarize`: Process and summarize the document using a locally hosted LLM.

### Files
- **main.py**: Entry point for the FastAPI application.
- **models.py**: Defines data models used in the application.
- **routes.py**: Contains route definitions and their corresponding logic.
- **utils.py**: Utility functions for file handling and summarization logic.

## Frontend
The frontend is built using React and provides a user interface for uploading documents and displaying the summarized text.

### Components
- **FileUpload**: Component to handle file uploads.
- **Summarize**: Component to display the summarized text.

### Files
- **FileUpload.js**: Component for file upload functionality.
- **Summarize.js**: Component for displaying summarized text.
- **App.js**: Main application component.
- **App.css**: CSS file for styling the application.
- **index.js**: Entry point for the React application.

## Docker Setup
A Docker Compose file is provided to set up and run both the backend and frontend services locally.

### Files
- **docker-compose.yml**: Defines the Docker services for the backend and frontend.
- **backend/Dockerfile**: Dockerfile for building the backend service.
- **frontend/Dockerfile**: Dockerfile for building the frontend service.

## Challenges and Approach
- **File Handling**: Ensured proper handling and storage of uploaded files.
- **LLM Integration**: Integrated a pre-trained LLM for summarization.
- **Concurrency**: Ensured the backend can handle multiple concurrent requests.

## Bibliography
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [React Documentation](https://reactjs.org/)
- [Transformers Documentation](https://huggingface.co/transformers/)
