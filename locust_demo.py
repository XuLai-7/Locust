# 定义任务  --- 取样器-发送 http 请求
# 定义任务集 --- 事务管理器
# 定义 locust 类 --- 线程组-线程数 用户类
from locust import TaskSet
from locust import HttpLocust


# 定义任务  --- 取样器-发送 http 请求
# 就是定义接口请求(l.client 相当于 request)
def login(l):
    l.client.post("/login", data={"username": "admin", "password": "123456"})


def index(l):
    l.client.get("/index")


def profile(l):
    l.client.get("/profile")


def logout(l):
    l.client.post("/logout")


# 定义任务集
class UserBehavior(TaskSet):
    # 类属性 tasks
    # 3 : 1 的比例关系
    tasks = {index: 3, profile: 1}

    def on_start(self):
        login(self)

    def on_stop(self):
        logout(self)


# 定义 locust 类 --- 线程组-线程数  用户类
# 执行 任务集
class WebsiteUser(HttpLocust):
    # 类属性, 绑定 任务集
    task_set = UserBehavior
    # 每个请求发送前的等待时间
    min_wait = 500
    max_wait = 1000
    # 会和任务-请求 中的 URL 拼接起来请求
    host = "http://bms-test.itheima.net/bms"
    # 用户数的分配权重
    # 一个用户类的权重无所谓
    # 都是它的
    weight = 10

# locustio 版本 0.12.2
# 运行 locust -f .\locust_demo.py
#  重新安装 gevent 包的版本 1.4.0
# 运行 locust -f .\locust_demo.py
# 浏览器输入 localhost:8089 设置虚拟用户数 和 每秒上升的用户数
# RPS: 每秒请求数  == QPS