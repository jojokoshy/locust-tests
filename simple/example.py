from locust import HttpLocust, TaskSet


def index(l):
    l.client.get("/publish")


class UserBehavior(TaskSet):
    tasks = [index]


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000
