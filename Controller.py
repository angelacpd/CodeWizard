import web
from Models import RegisterModel, LoginModel, Posts

web.config.debug = False

urls = (
    '/', 'Home',
    '/register', 'Register',
    '/login', 'Login',
    '/logout', 'Logout',
    '/postregistration', 'PostRegistration',
    '/check-login', 'CheckLogin',
    '/post-activity', 'PostActivity',
    '/profile/(.*)/info', 'UserInfo',
    '/settings', 'UserSettings',
    'update-settings', 'UpdateSettings',
    '/profile/(.*)', 'UserProfile'
)

app = web.application(urls, globals())
session = web.session.Session(app, web.session.DiskStore("sessions"), initializer={"user": None})
session_data = session._initializer

render = web.template.render("Views/Templates", base="MainLayout", globals={"session": session_data,
                                                                            "current_user": session_data["user"]})
# render = web.template.render("Views/Templates", base="MainLayout")

# Classes and Routes
class Home:
    def GET(self):


        post_model = Posts.Posts()
        posts = post_model.get_all_posts()

        # print("Hello, World!")
        # return
        # return render.MainLayout()
        return render.Home(posts)
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
            session_data["user"] = isCorrect
            return isCorrect

        return "error"


class PostActivity:
    def POST(self):
        data = web.input()
        data.username = session_data['user']['username']

        post_model = Posts.Posts()
        post_model.insert_post(data)
        return "success"


class UserProfile:
    def GET(self, user):
        login = LoginModel.LoginModel()
        user_info = login.get_profile(user)

        post_model = Posts.Posts()
        posts = post_model.get_user_posts(user)
        return render.Profile(posts, user_info)


class UserInfo:
    def GET(self, user):

        login = LoginModel.LoginModel()
        user_info = login.get_profile(user)

        return render.Info(user_info)


class UserSettings:
    def GET(self):

        return render.Settings()


class UpdateSettings:
    def POST(self):
        data = web.input()
        data.username = session_data["user"]["username"]

        settings_model = LoginModel.LoginModel()
        if settings_model.update_info(data):
            return "success"
        else:
            return "A fatal error has occurred."

class Logout:
    def GET(self):
        session['user'] = None
        session_data['user'] = None

        session.kill()
        return "success"

if __name__ == "__main__":
    app.run()
