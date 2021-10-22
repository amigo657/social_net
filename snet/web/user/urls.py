from snet.urls.route import Controller
from snet.web.user import views as user


Controller.add("/create", user.Create, name = "create_user")