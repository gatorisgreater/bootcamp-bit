from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

my_list=["spaced-repetition-capstone", "algorithms interview practice", "GoalzApp"]
pm_list = ["React Interview", "DSA Interview", "arm", "leg", "2/28 HW", "2/27 HW"]

spencer_list = ["react-trello", "HackerNewsAPI", "Thinkful Tube"]
cohort_list = ["", "Alex", "Anitha", "John", "Roberto", "Spencer", "Zach"]

@app.route("/")
@app.route("/home")
def home():
    my_img = "https://avatars1.githubusercontent.com/u/22352414?v=3&s=460"
    return render_template('child.html',
                           my_string="Your recent assignments:",
                           my_list=my_list,
                           my_img=my_img)

@app.route("/delete", methods=["GET"])
def delete_assignment_get():
    return render_template("delete_assignment.html", pm_list=pm_list)
    
@app.route("/delete", methods=["POST"])
def delete_assignment_delete():
    # print(request)
    
    # assignmentDeletion = request.form["title"]

    # pm_list.remove(assignmentDeletion)
    return redirect(url_for("theresa"))


@app.route("/add", methods=["GET"])
def add_assignment_get():
    return render_template("add_assignment.html", cohort_list=cohort_list)
    
@app.route("/add", methods=["POST"])
def add_assignment_post():
    assignmentEntry = request.form["title"]
    my_list.insert(0, assignmentEntry)
    spencer_list.insert(0, assignmentEntry)
    return redirect(url_for("home"))

# @app.route("/<name>")
# def cohortmate(name):
#     return render_template('child.html',
#                             my_string="You and {} have worked on:".format(name.title()),
#                             my_list=[0,1,2,3,4,5])

@app.route("/alex")
def alex():
    my_img = "https://avatars2.githubusercontent.com/u/22599303?v=3&s=400"
    my_list = ["hash maps", "hot or cold", "1 day react project", "Mocha/Chai", "blog app authentication" ]
    my_list_length = len(my_list)
    return render_template('child.html',
                            my_string="You and Alex have worked on %d assignments:" % my_list_length,
                            my_list=my_list,
                            my_img=my_img)
                          
@app.route("/anitha")
def anitha():
    my_img = "https://ca.slack-edge.com/T02D02A55-U2UR39L5D-gd92dfc29d9f-512"
    my_list = ["spaced-repetition-capstone","MongoDB","shopping list app"]
    my_list_length = len(my_list)
    return render_template('child.html',
                           my_string="You and Anitha have worked on %d assignments:" % my_list_length,
                           my_list=my_list,
                           my_img=my_img)

@app.route("/john")
def john():
    my_img = "https://avatars1.githubusercontent.com/u/22508470?v=3&s=400"
    my_list = ["spaced-repetition-capstone","Recursion", "Knex/SQL", "DOM Traversal and Manipulation"]
    my_list_length = len(my_list)
    return render_template('child.html',
                           my_string="You and John have worked on %d assignments:" % my_list_length,
                           my_list=my_list,
                           my_img=my_img)

@app.route("/roberto")
def roberto():
    my_img = "https://avatars0.githubusercontent.com/u/1451729?v=3&s=400"
    my_list = ["Search Algos", "Thinking in React", "Blog Authentication", "Blog-API", "In Your Own Words Challenge"]
    my_list_length = len(my_list)
    return render_template('child.html',
                           my_string="You and Roberto have worked on %d assignments:" % my_list_length,
                           my_list=my_list,
                           my_img=my_img)

@app.route("/spencer")
def spencer():
    my_img = "https://ca.slack-edge.com/T02D02A55-U2GKU5M0A-255c0ba93a2f-512"
    my_list_length = len(spencer_list)
    return render_template('child.html',
                           my_string="You and Spencer have worked on %d assignments:" % my_list_length,
                           my_list=spencer_list,
                           my_img=my_img)

@app.route("/zach")
def zach():
    my_img = "https://avatars0.githubusercontent.com/u/16063092?v=3&s=400"
    my_list = ["binary search trees", "React component testing", "mongoose inegration", "weather-challenge-app"]
    my_list_length = len(my_list)
    return render_template('child.html',
                           my_string="You and Zach have worked on %d assignments:" % my_list_length,
                           my_list=my_list,
                           my_img=my_img)

@app.route("/theresa")
def theresa():
    my_img = "https://ca.slack-edge.com/T02D02A55-U2GJFK36Y-e4a4483c1f77-512"
    my_list_length = len(pm_list)
    return render_template('child.html',
                           my_string="You have %d outstanding assignments for Theresa:" % my_list_length,
                           my_list=pm_list,
                           my_img=my_img)
                           

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)