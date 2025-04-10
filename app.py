# CRUD com Flask
#Create, Read, Update, Delete = Cria, Ler, Atualizar e Deletar

from flask import Flask, request, jsonify
from models.task import Task

app = Flask(__name__)

tasks = []
task_id_control = 1

# Rota Create (CRIAR)
@app.route('/tasks', methods=['POST'])
def create_task():
    global task_id_control
    data = request.get_json()
    new_task = Task(id=task_id_control, title=data['title'], description=data.get("description", ""))
    task_id_control += 1
    tasks.append(new_task)
    return jsonify({"message": "Nova tarefa criada com sucesso"})

# Rota Read (LER)
@app.route('/tasks', methods=['GET'])
def get_tasks():
    task_list = [task.to_dict() for task in tasks]
    """nessa linha a variavel task_list recebe da interação
       for da lista tasks os itens da lista ja transformado 
       pelo metodo to_dict da class models, onde ele ja deixa
       os itens da lista no formato json
    """
    output = {
        "task": task_list,
        "total_tasks": len(task_list)
    }
    return jsonify(output)

# Rota Read de um iten especifico (LER)   
@app.route('/tasks/<int:id>', methods= ['GET'])
def get_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            return jsonify(t.to_dict())            
    if task == None:
            return jsonify({"message": "Não foi possível encontra a atividade"}), 404
    
# Rota Update (ATUALIZAR)    
@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t
            break
    if task == None:
        return jsonify({"message": "Não foi possível encontrar a atividade"}), 404
    
    # atualizando registro
    data = request.get_json()
    task.title = data['title']
    task.description = data['description']
    task.completed = data['completed']
    print(task)
    return jsonify({"message": "Tarefa atualizada com sucesso"})

# Rota Delete (DELETAR)
@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_desk(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t
            break

    if task == None:
        return jsonify({"message": "Não foi possível encontrar a atividade"}), 404
    
    tasks.remove(task)
    return jsonify({"message": "Tarefa deletada com seucesso"})


if __name__ == "__main__":
    app.run(debug= True)