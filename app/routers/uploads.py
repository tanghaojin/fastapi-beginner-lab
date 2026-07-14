from typing import Annotated

from fastapi import APIRouter, Depends, File, UploadFile

from ..auth import get_current_user

router = APIRouter(prefix="/uploads", tags=["uploads"])


@router.post("", summary="上传单个文件")
async def upload_file(
    file: Annotated[UploadFile, File(description="要上传的文件")],
    current_user=Depends(get_current_user),
):
    return {
        "filename": file.filename,
        "content_type": file.content_type,
    }
