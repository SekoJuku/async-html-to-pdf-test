import tempfile

import aiohttp
from pydantic import AnyUrl
from fastapi import HTTPException

async def download_file_to_tempfile(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status != 200:
                raise HTTPException(status_code=404, detail="Failed to download file")

            file_content = await response.read()

            with tempfile.NamedTemporaryFile(mode="wb", delete=False) as f:
                f.write(file_content)
                return f.name
