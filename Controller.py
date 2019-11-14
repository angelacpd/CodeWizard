import web

urls = (
    '/', 'home',
    '/register', 'register'
)

render = web.template.render("Views/Templates", base="MainLayout")
# render = web.template.render("Views/Templates")
app = web.application(urls, globals())


# Classes and Routes
class home:
    def GET(self):
        # print("Hello, World!")
        # return
        # return render.MainLayout()
        return render.Home()
        # return "home"


class register:
    def GET(self):
        return render.Register()

if __name__ == "__main__":
    app.run()
