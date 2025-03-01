# Flask DateTime API

A simple Flask application that provides current date and time through different API endpoints.

## Endpoints

- `/` - Returns current date and time in UTC (format: YYYY-MM-DD HH:MM:SS)
- `/date` - Returns current date in UTC (format: YYYY-MM-DD)
- `/time` - Returns current time in UTC (format: HH:MM:SS)

## Prerequisites

- Docker installed on your system


## Running the Application

### 1. Build the Docker Image
```bash
docker build -t flask-datetime .
```
### 2. Run the Container

```bash
docker run -p 5000:5000 flask-datetime
```

### 3. Access the API

After running the container, you can access the endpoints at:

- http://localhost:5000/
- http://localhost:5000/date
- http://localhost:5000/time


## Examples

Using curl:

```bash
# Get full datetime
curl http://localhost:5000/

# Get date only
curl http://localhost:5000/date

# Get time only
curl http://localhost:5000/time
```

## Note

- All times are returned in UTC timezone
- The application runs in debug mode inside the container
- The container exposes port 5000 internally




