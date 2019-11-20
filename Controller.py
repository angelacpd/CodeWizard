import web
from Models import RegisterModel, LoginModel

urls = (
    '/', 'Home',
    '/register', 'Register',
    '/login', 'Login',
    '/postregistration', 'PostRegistration',
    '/check-login', 'CheckLogin'
)

render = web.template.render("Views/Templates", base="MainLayout")
# render = web.template.render("Views/Templates")
app = web.application(urls, globals())


# Classes and Routes
class Home:
    def GET(self):
        # print("Hello, World!")
        # return
        # return render.MainLayout()
        return render.Home()
        # return "home"


class Register:
    def GET(self):
        return render.Register()


class Login:
    def GET(self):
        return render.Login()


class PostRegistration:
    def POST(self):
        data = web.input()
        reg_model = RegisterModel.RegisterModel()
        reg_model.insert_user(data)

        return data.username


class CheckLogin:
    def POST(self):
        data = web.input()
        login = LoginModel.LoginModel()
        isCorrect = login.check_user(data)
        if isCorrect:
            return isCorrect

        return "error"

if __name__ == "__main__":
    app.run()
