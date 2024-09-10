#liv.py
class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, titulo, function):
        self.commands[titulo] = function

    def run(self):
        while True:
            command = input("Enter a command: ")
            if command == "quit":
                print("Goodbye!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Invalid command. Try again.")


class livroCLI(SimpleCLI):
    def __init__(self, livro_model):
        super().__init__()
        self.livro_model = livro_model
        self.add_command("create", self.create_livro)
        self.add_command("read", self.read_livro)
        self.add_command("update", self.update_livro)
        self.add_command("delete", self.delete_livro)

    def create_livro(self):
        titulo = input("Enter the titulo: ")
        ano = int(input("Enter the ano: "))
        self.livro_model.create_livro(titulo, ano)

    def read_livro(self):
        id = input("Enter the id: ")
        livro = self.livro_model.read_livro_by_id(id)
        if livro:
            print(f"titulo: {livro['titulo']}")
            print(f"ano: {livro['ano']}")

    def update_livro(self):
        id = input("Enter the id: ")
        titulo = input("Enter the new titulo: ")
        ano = int(input("Enter the new ano: "))
        self.livro_model.update_livro(id, titulo, ano)

    def delete_livro(self):
        id = input("Enter the id: ")
        self.livro_model.delete_livro(id)
        
    def run(self):
        print("Welcome to the livro CLI!")
        print("Available commands: create, read, update, delete, quit")
        super().run()
        