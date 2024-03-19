import io
import cv2
from fastapi import FastAPI, HTTPException, status
from fastapi.responses import StreamingResponse




app = FastAPI()

@app.get("/")
def root():
    return "در اینجا شما میتوانید درباره هریک از نمادهای هفت سین اطلاعاتی را به دست آورید . همچنین از هر نماد عکس های آن نیز وجود دارد"

@app.get("/sins")
def sins():
    return " سکه سنجد 🍎سیب   🍇 سرکه  سمنو 🧄سیر 🪻سنبل🪙" 

@app.get("/sins/{sin_name}")
def sininfo(sin_name : str):
    if sin_name == "سیب":
        return "سیب به عنوان نمادی از زیبایی، سلامتی و ثمرهٔ طبیعت است. شکل گرد سیب ممکن است همچنین نماد چرخهٔ زندگی و فصل‌های تغییرات باشد. "
    elif sin_name == "سنجد":
        return " در هفت‌سین، سنجد یکی از مواردی است که معمولاً به عنوان نمادی از شکوفایی، شادابی و زندگی جدید در ایران شناخته می‌شود"
    elif sin_name == "سرکه" : 
        return " استفاده از سرکه در هفت‌سین نمایانگر قدرت تحمل و توانایی برای تغییر و تحول در برابر موقعیت‌های تلخ و چالش‌های زندگی است. به عنوان یک نماد از شیرینی که میان تلخی‌ها وجود دارد، سرکه نشانه‌ای از امید به آینده و امید به بهبود و پیشرفت است."
    elif sin_name == "سکه" :
        return "  اضافه کردن سکه به هفت‌سین ممکن است به عنوان یک آرزو برای رونق اقتصادی و پیشرفت مالی در سال جدید تفسیر شود"
    elif sin_name == "سمنو" :
        return " سمنو به عنوان یک نماد از شروع دوره‌ی جدید، رونق و تازگی تفسیر می‌شود که با مفهوم نوروز و شروع سال جدید در جوامع ایرانی هماهنگی دارد"
    elif sin_name == "سنبل" :
        return " سنبل یکی از عناصر معمول است که به عنوان نمادی از بهار، تازگی، و شکوفایی استفاده می‌شود"
    elif sin_name == "سماق" : 
        return "در هفت‌سین، سماق نیز یکی از موارد معمول است که به عنوان نمادی از شادابی، نوآوری و رونق استفاده می‌شود."
    elif sin_name == "سیر" :
        return "سیر به عنوان نمادی از سلامتی و شفا، و همچنین به عنوان نمادی از مقاومت در برابر بیماری‌ها و سختی‌ها در فرهنگ‌های مختلف شناخته شده است. اضافه کردن سیر به هفت‌سین همچنین می‌تواند به عنوان نشانه‌ای از انرژی و توانایی برای مقابله با چالش‌های زندگی تفسیر شود "
    else:
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST,
                            detail = "لطفا فقط هفت سین را وارد کنید ")

@app.get("/pieces/{piece_name}/image")                
def sin_image(piece_name):
    if piece_name == "سیب":
        image = cv2.imread("images/sib.jpg")
        _, encoded_image = cv2.imencode(".png", image)
        return StreamingResponse(io.BytesIO(encoded_image.tobytes()), media_type = "image/jpg")
    elif piece_name == "سرکه":
        image = cv2.imread("images/serkeh.jpg")
        _, encoded_image = cv2.imencode(".png", image)
        return StreamingResponse(io.BytesIO(encoded_image.tobytes()), media_type = "image/jpg")
    
    elif piece_name == "سکه":
        image = cv2.imread("images/seke.jpg")
        _, encoded_image = cv2.imencode(".png", image)
        return StreamingResponse(io.BytesIO(encoded_image.tobytes()), media_type = "image/jpg")
    
    elif piece_name == "سیر":
        image = cv2.imread("images/sir.jpg")
        _, encoded_image = cv2.imencode(".png", image)
        return StreamingResponse(io.BytesIO(encoded_image.tobytes()), media_type = "image/jpg")
    
    elif piece_name == "سماق":
        image = cv2.imread("images/somagh.jpg")
        _, encoded_image = cv2.imencode(".png", image)
        return StreamingResponse(io.BytesIO(encoded_image.tobytes()), media_type = "image/jpg")
    
    elif piece_name == "سنبل":
        image = cv2.imread("images/sonbol.jpg")
        _, encoded_image = cv2.imencode(".png", image)
        return StreamingResponse(io.BytesIO(encoded_image.tobytes()), media_type = "image/jpg")
    
    else:
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST,
                            detail = "فقط هفت سین را وارد کنید")