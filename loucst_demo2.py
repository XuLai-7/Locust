from locust import TaskSet, HttpLocust


# 定义任务
def login(l):
    l.client.post("/login", data={"username": "admin", "password": "123456"})


def index(l):
    l.client.get("/index")


def profile(l):
    l.client.get("/profile")


def logout(l):
    l.client.post("/logout")


class UserBehavier(TaskSet):
    tasks = {index: 3, profile: 1}

    def on_start(self):
        login(self)

    def on_stop(self):
        logout(self)


class WebsitUser(HttpLocust):
    task_set = UserBehavier
    min_wait = 500
    max_wait = 1000
    host = "http://bms-test.itheima.net/bms"
    weight = 10
