from project import add_task, complete_task, list_tasks

def test_add_task(monkeypatch):
    tasks = []
    monkeypatch.setattr("builtins.input", lambda _: "Test Task")
    add_task(tasks)
    assert tasks == [{"task": "Test Task", "completed": False}]

def test_complete_task(monkeypatch):
    tasks = [{"task": "Sample Task", "completed": False}]
    monkeypatch.setattr("builtins.input", lambda _: "1")
    complete_task(tasks)
    assert tasks[0]["completed"] == True

def test_list_tasks(capsys):
    tasks = [{"task": "Sample Task", "completed": False}]
    list_tasks(tasks)
    captured = capsys.readouterr()
    assert "Sample Task" in captured.out
