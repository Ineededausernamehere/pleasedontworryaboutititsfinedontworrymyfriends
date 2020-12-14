from mitmproxy import http
from mitmproxy import ctx
base = []
url = []

compURL = ['https:', 'canvas.instructure.com', 'api', 'v1', 'courses', '2433119', 'quizzes', '6433069', 'submissions', '30655698', 'events']
compareBase = ['canvas', 'instructure', 'com']


class CanvasKill:
    def load(self, loader):
        loader.add_option(
            "canvas_kill", bool, False,
            """
            It modifies Instructure's Canvas packets that log when
            one leaves quiz pages
            """
        )

    def request(self, flow: http.HTTPFlow) -> None:
        ctx.log("Loaded")
        currentURL = str(flow.request.pretty_url)
        currentURL.split('/')
        if url[4] == compURL[3] and url[3] == compURL[2] and url[11] == compURL[10] and len(url) == 12:
            flow.kill()
