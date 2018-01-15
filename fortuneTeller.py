from sanic import Sanic
from sanic.response import text

fortuneTeller = Sanic()


@fortuneTeller.route("/")
async def hello(request):
    return text("Hello {}".format(request.args["name"][0]))


if __name__ == "__main__":
    fortuneTeller.run(host="0.0.0.0", port=8000)