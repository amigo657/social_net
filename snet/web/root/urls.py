from snet.urls.route import Controller

API_URL = "/api/v1"


Controller.include(API_URL + "/user", "snet.web.user.urls")