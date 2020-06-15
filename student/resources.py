from student import repo

class StudentResource():
    def on_get(self, req, resp):
        resp.media = repo.getAll()
