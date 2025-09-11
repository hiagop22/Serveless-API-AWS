from src.drivers.rest.main import app

if __name__ == "__main__":
  import uvicorn
  uvicorn.run("run:app", host="127.0.0.1", port=8090, reload=True)