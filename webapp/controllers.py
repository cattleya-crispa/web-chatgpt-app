from fastapi import FastAPI
from starlette.templating import Jinja2Templates
from starlette.requests import Request
 
app = FastAPI(
    title='web-chatGPT-APP',
    description='chat gpt ga kotaeru web app',
    version='0.9 beta'
)
 

# new テンプレート関連の設定 (jinja2)
templates = Jinja2Templates(directory="templates")
jinja_env = templates.env  # Jinja2.Environment : filterやglobalの設定用


def index(request: Request):
    return templates.TemplateResponse('index.html',
                                      {'request': request}  )

def admin(request: Request):
    return templates.TemplateResponse('admin.html',
                                      {'request': request,
                                       'username': 'admin'})