import random
import string
import string

from fastapi import APIRouter, Depends
from fastapi.responses import RedirectResponse

from models import URL
from schemas import  URLRequest, URLResponse
from database import get_db
from sqlalchemy.orm import Session



from fastapi import HTTPException





router = APIRouter(
    prefix="/url",
    tags=["URL Shortener"]
)

def generate_short_code(length:int=6):
    return "".join(random.choices(string.ascii_letters + string.digits,k=length))

@router.post("/shorten",response_model=URLResponse)
def create_short_url(request:URLRequest,db:Session=Depends(get_db)):
    original_url = str(request.original_url)

    existing = db.query(URL).filter(URL.original_url==original_url).first()
    if existing:
        return{
            "original_url":existing.original_url,
            "short_code":existing.short_code,
            "short_url":f"http://localhost:8000/{existing.short_code}"
        }
     

    short_code = generate_short_code()
    while db.query(URL).filter(URL.short_code == short_code).first():
        short_code = generate_short_code()

    new_url = URL(original_url =original_url,short_code=short_code)
    db.add(new_url)
    db.commit()
    db.refresh(new_url)

    return{
            "original_url":new_url.original_url,
            "short_code":new_url.short_code,
            "short_url":f"http://localhost:8000/{new_url.short_code}"
        }


@router.get("/all",response_model=list[URLResponse])
def get_all_urls(db:Session=Depends(get_db)):
    urls = db.query(URL).all()
    result=[]
    for url in urls:
        result.append({
            "original_url":url.original_url,
            "short_code":url.short_code,
            "short_url":f"http://localhost:8000/{url.short_code}"
        })
    return result

@router.get("/{short_code}")
def redirect_to_original(short_code:str,db:Session=Depends(get_db)):
    url = db.query(URL).filter(URL.short_code==short_code).first()
    if url:
        return RedirectResponse(url.original_url)
    else:
        raise HTTPException(status_code=404,detail="Short URL not found")

      
@router.delete("/delete/{short_code}")
def delete_short_url(short_code: str, db: Session = Depends(get_db)):
    url = db.query(URL).filter(URL.short_code == short_code).first()

    if not url:
        raise HTTPException(
            status_code=404,
            detail="Short URL not found"
        )

    db.delete(url)
    db.commit()

    return {
        "message": "Short URL deleted successfully"
    }