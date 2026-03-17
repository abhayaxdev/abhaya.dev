from fastapi.templating import Jinja2Templates



def get_templates():
    templates = Jinja2Templates(directory='templates')   
    return templates 