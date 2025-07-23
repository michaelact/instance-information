import logging
import requests
from fastapi import FastAPI, Response
from fastapi.responses import Response as FastAPIResponse
import uvicorn

app = FastAPI()

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
logger = logging.getLogger(__name__)

def get_public_ip():
    """
    Fetch public information from https://ifconfig.me (currently public IP).
    This function can be extended in the future for more info.
    """
    try:
        response = requests.get('https://ifconfig.me', timeout=5)
        response.raise_for_status()
        public_ip = response.text.strip()
        logger.info(f'Fetched public IP: {public_ip}')
        return public_ip
    except requests.RequestException as e:
        logger.error(f'Error fetching public IP: {e}')
        return None

@app.get("/")
def root():
    get_public_ip()
    return FastAPIResponse(status_code=200)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080)
