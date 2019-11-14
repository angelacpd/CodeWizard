import web

urls = (
    '/', 'Home',
    '/register', 'Register',
    '/postregistration', 'PostRegistration'
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


class PostRegistration:
    def POST(self):
        data = web.input()
        return data.username

if __name__ == "__main__":
    app.run()
