class Todo:
    def __init__(self,code_id:int, tittle: str, description: str):
        self.code_id: int = code_id
        self.tittle: str = tittle
        self.description: str = description
        self.completed: bool = False
        self.tags: list[str] = []

    def mark_completed(self):
        self.completed = True

    def add_tag(self, tag: str):
        if tag not in self.tags:
            self.tags.append(tag)

    def __str__(self) -> str:
        return f"{self.code_id} - {self.tittle}"


class TodoBook:
    def __init__(self):
        self.todos: dict[int, Todo] = {}

    def add_todo(self,tittle: str, descriptiom: str) -> int:
        code_id: int = len(self.todos) + 1
        todo: Todo = Todo(code_id, tittle, descriptiom)
        self.todos[code_id] = todo
        return  code_id

    def pending_todos(self) -> list[Todo]:
        return [todo for todo in self.todos.values() if not todo.completed]

    def completed_todos(self) -> list[Todo]:
        return [todo for todo in self.todos.values() if todo.completed]
        def tags_todo_count(self) -> dict[str, int]:
        result: dect[str, int] = {}
        for todo in self.todos.values():
            for tag in todo.tags:
                if tag not in result.keys():
                    result[tag] = 1
                else:
                    result[tag] += 1
        return result

