# LLM-based Automation Agent

This project implements an automation agent that accepts plain‑English tasks and executes a series of operations (tasks A1–A10) leveraging both file operations and external script calls. It provides two API endpoints:

- **POST /run?task=<task description>**: Parses and executes the given task.
- **GET /read?path=<file path>**: Returns the contents of a file (only within the `/data` directory).

## Setup

1. Clone the repository.
2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate   
   # Windows: venv\Scripts\activate
   pip install -r requirements.txt```
3. Run the API locally:
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```
4. Use Postman or curl to test the endpoints.
## Tasks Implemented
A1: Download and run datagen.py with the user email.

A2: Format `/data/format.md`.

A3: Count Wednesdays in `/data/dates.txt` and output the count. 

A4: Sort contacts in `/data/contacts.json`.

A5: Extract first lines from the 10 most recent log files in `/data/logs/`.

A6: Index Markdown files in `/data/docs/` by their first H1 title.

A7: Extract sender’s email from `/data/email.txt`.

A8: Extract credit card number from `/data/credit-card.png`.

A9: Find the most similar pair of comments in `/data/comments.txt` .

A10: Query `/data/ticket-sales.db` for total "Gold" ticket sales.

## Deployment
A Dockerfile is provided. Build and run the Docker image as described in the Dockerfile.

## License
This project is licensed under the MIT License.








