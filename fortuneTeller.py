from sanic import Sanic
from sanic.response import text

fortuneTeller = Sanic()

# from cassandra.cluster import Cluster
# cluster = Cluster()
# session = cluster.connect('demo')

# session.execute("""
#
# insert into users (lastname, age, city, email, firstname) values ('Jones', 35, 'Austin', 'bob@example.com', 'Bob')
#
# """)

@fortuneTeller.route("/")
async def hello(request):
    # result = session.execute("select * from users where lastname='Jones' ")[0]
    # name = result.firstname
    # user = input("What is your name?\n")
    # hello = "Hellooooo"
    # return text()
    return text(list.html)
    #return text(result.firstname, result.age)

# def showMachineList()
#     return render_template('list.html')

if __name__ == "__main__":
    fortuneTeller.run(host="0.0.0.0", port=8000)