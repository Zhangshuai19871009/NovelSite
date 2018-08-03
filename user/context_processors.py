from .forms import LoginForm

def login_modal_form(reqeust):
    return {'login_modal_form': LoginForm()}