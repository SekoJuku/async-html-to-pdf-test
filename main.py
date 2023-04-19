import pdfkit
import aiohttp
import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse, StreamingResponse

from src import download_file_to_tempfile


app = FastAPI()


@app.get("/", include_in_schema=False)
async def docs_redirect():
    return RedirectResponse(url="/docs")

@app.get("/download/{url:path}")
async def download_file(url: str):
    extension = url.split(".")[-1]
    file_path = await download_file_to_tempfile(url)
    options = {
        'no-stop-slow-scripts': None,
        "encoding": "UTF-8"
    }
    pdfkit.from_file(file_path, f"{file_path}.pdf", options=options, configuration=pdfkit.configuration(wkhtmltopdf='/usr/bin/wkhtmltopdf'))
    return StreamingResponse(open(f'{file_path}.pdf', "rb"), media_type='application/pdf')
