from email.mime import image
from src.exceptions import NoContentTypeError, FileIsNotAnImageError
from pydantic import BaseModel, ValidationError, field_validator
from fastapi import UploadFile


class TextQuery(BaseModel):
    text: str

class ImageQuery(BaseModel):
    image: UploadFile

    @field_validator('image', mode='after')
    @classmethod
    def is_image(cls, uploaded_file: UploadFile) -> UploadFile:
        if uploaded_file.content_type is None:
            raise NoContentTypeError(f"uploaded_File {uploaded_file.filename} is not an image")
        if not uploaded_file.content_type.startswith('image'):
            raise FileIsNotAnImageError(f"uploaded_File {uploaded_file.filename} is not an image")
        return uploaded_file


