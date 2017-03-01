from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    my_img = "https://avatars1.githubusercontent.com/u/22352414?v=3&s=460"
    return render_template('child.html',
                           my_string="Your most recent projects",
                           my_list=[0],
                           my_img=my_img)

# @app.route("/<name>")
# def cohortmate(name):
#     return render_template('child.html',
#                             my_string="You and {} have worked on:".format(name.title()),
#                             my_list=[0,1,2,3,4,5])

@app.route("/alex")
def alex():
    my_img = "https://avatars2.githubusercontent.com/u/22599303?v=3&s=400"
    my_list = [0,1]
    my_list_length = len(my_list)
    return render_template('child.html',
                            my_string="You and Alex have worked on %d projects together:" % my_list_length,
                            my_list=my_list,
                            my_img=my_img)
                          
@app.route("/anitha")
def anitha():
    my_img = "https://ca.slack-edge.com/T02D02A55-U2UR39L5D-gd92dfc29d9f-512"
    my_list = [0,1,2]
    my_list_length = len(my_list)
    return render_template('child.html',
                           my_string="You and Anitha have worked on %d projects together:" % my_list_length,
                           my_list=my_list,
                           my_img=my_img)

@app.route("/john")
def john():
    my_img = "https://avatars1.githubusercontent.com/u/22508470?v=3&s=400"
    my_list = [0,1,2,3]
    my_list_length = len(my_list)
    return render_template('child.html',
                           my_string="You and John have worked on %d projects together:" % my_list_length,
                           my_list=my_list,
                           my_img=my_img)

@app.route("/roberto")
def roberto():
    my_img = "https://avatars0.githubusercontent.com/u/1451729?v=3&s=400"
    my_list = [0,1,2]
    my_list_length = len(my_list)
    return render_template('child.html',
                           my_string="You and Roberto have worked on %d projects together:" % my_list_length,
                           my_list=my_list,
                           my_img=my_img)

@app.route("/spencer")
def spencer():
    my_img = "https://ca.slack-edge.com/T02D02A55-U2GKU5M0A-255c0ba93a2f-512"
    my_list = [0,1]
    my_list_length = len(my_list)
    return render_template('child.html',
                           my_string="You and Spencer have worked on %d projects together:" % my_list_length,
                           my_list=my_list,
                           my_img=my_img)

@app.route("/zach")
def zach():
    my_img = "https://avatars0.githubusercontent.com/u/16063092?v=3&s=400"
    my_list = [0]
    my_list_length = len(my_list)
    return render_template('child.html',
                           my_string="You and Zach have worked on %d projects together:" % my_list_length,
                           my_list=my_list,
                           my_img=my_img)

@app.route("/theresa")
def theresa():
    my_img = "https://ca.slack-edge.com/T02D02A55-U2GJFK36Y-e4a4483c1f77-512"
    my_list = ["React Interview", "DSA Interview", "arm", "leg", "2/28 HW", "2/27 HW"]
    my_list_length = len(my_list)
    return render_template('child.html',
                           my_string="You have %d outstanding items for Theresa:" % my_list_length,
                           my_list=my_list,
                           my_img=my_img)
                           

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)