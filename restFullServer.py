from flask import Flask,current_app,g,session,request,render_template,jsonify
app = Flask(__name__)


tasks = [
    {
        'id': 0,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 1,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

# get----read
@app.route('/api/v0.1/todos')
def readTodos():
    todoId = int(request.args.get('todoId','-1'))

    if todoId == -1:
        return jsonify(tasks)
    else:
        if 0<=todoId<len(tasks):
            return jsonify(tasks[todoId])
        else:
            return render_template('base-message.html',message="404 not found"),404
        
#post----create
@app.route('/api/v0.1/todos',methods=['POST'])
def createTodos():
    title = request.args.get('title','untitled')
    description = request.args.get('description','no description')

    todoId = len(tasks)

    tasks.append({'id':todoId,'title':title,'description':description})

    return jsonify(len(tasks)-1)

# put----update
@app.route('/api/v0.1/todos',methods=['PUT'])
def updateTodos():
    todoId = int(request.args.get('todoId','-1'))

    if todoId == -1:
        return 'error',404

    title = request.args.get('title',tasks[todoId]['title'])
    description = request.args.get('description',tasks[todoId]['description'])

    tasks[todoId] = {'id':todoId,'title':title,'description':description}

    return jsonify(tasks[todoId])

# delete----delete
@app.route('/api/v0.1/todos',methods=['DELETE'])
def deleteTodos():
    todoId = int(request.args.get('todoId','-1'))

    if todoId == -1:
        return 'error',404
    tmp = tasks.pop(todoId)

    return jsonify(tmp)


if __name__ == "__main__":
    app.run(debug=True,host="127.0.0.1",port=5000)
