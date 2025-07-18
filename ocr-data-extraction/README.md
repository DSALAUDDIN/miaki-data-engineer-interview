# OCR Data Extraction API

This project provides a FastAPI-based web service for extracting structured data from documents, such as PCC and university certificates. The API is containerized using Docker for easy deployment.

## Features
- Health check endpoint
- File upload endpoints for PCC and university certificates
- Placeholder extraction logic (ready for extension)

## Getting Started

### Prerequisites
- Docker
- Python 3.9 (if running locally)

### Build and Run with Docker
1. Build the Docker image:
   ```sh
   docker build -t ocr-data-extraction-api .
   ```
2. Run the Docker container:
   ```sh
   docker run -d -p 8000:8000 --name ocr-data-extraction-container ocr-data-extraction-api
   ```
3. Access the API:
   - Health check: [http://localhost:8000/](http://localhost:8000/)
   - Docs: [http://localhost:8000/docs](http://localhost:8000/docs)

### Local Development
1. Install dependencies:
   ```sh
   pip install -r requirements.txt
   pip install python-multipart
   ```
2. Run the API:
   ```sh
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

## API Endpoints
- `GET /` - Health check
- `POST /extract/pcc` - Upload PCC document
- `POST /extract/university` - Upload university certificate

## License
MIT

