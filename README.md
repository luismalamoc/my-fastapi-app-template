
# My FastApi App Template

This is a FastAPI application structured with a focus on modularity, dependency injection, and scalability.

## Project Structure

```
app/
├── __init__.py
├── main.py
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── database.py
├── repositories/
│   ├── __init__.py
│   ├── user_repository.py
├── models/
│   ├── __init__.py
│   ├── user.py
├── mappers/
│   ├── __init__.py
│   ├── user_mapper.py
├── resources/
│   ├── __init__.py
│   ├── user_router.py
├── schemas/
│   ├── __init__.py
│   ├── user_schema.py
└── services/
    ├── __init__.py
    ├── user_service.py
```

## Getting Started

### Prerequisites

- Docker
- Python 3.11

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/yourrepository.git
   cd yourrepository
   ```

2. Build the Docker image:

   ```bash
   docker build -t my-fastapi-app-template .
   ```

3. Run the Docker container:

   ```bash
   docker run -d -p 8000:8000 my-fastapi-app-template
   ```
4. Run locally

    ```bash
    uvicorn app.main:app --reload
    ```

### Accessing the API

Once the container is running, you can access the API at:

```
http://localhost:8000
```

### Project Configuration

- **Environment Variables**:
  - `PYTHONDONTWRITEBYTECODE=1`: Prevents Python from writing `.pyc` files to disk.
  - `PYTHONUNBUFFERED=1`: Ensures that the Python output is not buffered.

- **Database Configuration**: Located in `config/settings.py`. Ensure you update the `database_url` to match your database settings.

### Application Context

The application uses an `AppContext` class to manage dependencies such as the database session, repositories, and services.

### Deployment

For production deployment, consider using Docker Compose, Kubernetes, or a cloud service provider that supports Docker containers.

## License

This project is licensed under the MIT License.
