from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('child.html',
                           my_string="Your most recent projects",
                           my_list=[0])

# @app.route("/<name>")
# def cohortmate(name):
#     return render_template('child.html',
#                             my_string="You and {} have worked on:".format(name.title()),
#                             my_list=[0,1,2,3,4,5])

@app.route("/alex")
def alex():
    my_list = [0,1]
    my_list_length = len(my_list)
    return render_template('child.html',
                            my_string="You and Alex have worked on %d projects together:" % my_list_length,
                            my_list=my_list)
                          
@app.route("/anitha")
def anitha():
    my_list = [0,1,2]
    my_list_length = len(my_list)
    return render_template('child.html',
                           my_string="You and Anitha have worked on %d projects together:" % my_list_length,
                           my_list=my_list)

@app.route("/john")
def john():
    my_list = [0,1,2,3]
    my_list_length = len(my_list)
    return render_template('child.html',
                           my_string="You and John have worked on %d projects together:" % my_list_length,
                           my_list=my_list)

@app.route("/roberto")
def roberto():
    my_list = [0,1,2]
    my_list_length = len(my_list)
    return render_template('child.html',
                           my_string="You and Roberto have worked on %d projects together:" % my_list_length,
                           my_list=my_list)

@app.route("/spencer")
def spencer():
    my_list = [0,1]
    my_list_length = len(my_list)
    return render_template('child.html',
                           my_string="You and Spencer have worked on %d projects together:" % my_list_length,
                           my_list=my_list)

@app.route("/zach")
def zach():
    my_list = [0]
    my_list_length = len(my_list)
    return render_template('child.html',
                           my_string="You and Zach have worked on %d projects together:" % my_list_length,
                           my_list=my_list)
                           

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)