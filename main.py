class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.blocks = []

class Directory:
    def __init__(self, name):
        self.name = name
        self.files = []
        self.subdirectories = []

class FileSystemSimulator:
    def __init__(self, block_size, memory_size):
        self.block_size = block_size
        self.memory_size = memory_size
        self.memory = [0] * (memory_size // block_size)
        self.root = Directory("root")

    def allocate_blocks(self, size):
        num_blocks = size // self.block_size
        if size % self.block_size != 0:
            num_blocks += 1

        allocated_blocks = []
        for i in range(len(self.memory)):
            if self.memory[i] == 0:
                allocated_blocks.append(i)
                if len(allocated_blocks) == num_blocks:
                    for block in allocated_blocks:
                        self.memory[block] = 1
                    return allocated_blocks

        return None  # Not enough contiguous blocks

    def deallocate_blocks(self, blocks):
        for block in blocks:
            self.memory[block] = 0

    def create_file(self, parent_directory, name, size):
        if any(file.name == name for file in parent_directory.files):
            print(f"Error: A file with the name '{name}' already exists in '{parent_directory.name}'.")
            return

        file_blocks = self.allocate_blocks(size)
        if file_blocks is not None:
            new_file = File(name, size)
            new_file.blocks = file_blocks
            parent_directory.files.append(new_file)
            print(f"File '{name}' created in '{parent_directory.name}'. Blocks: {file_blocks}")
        else:
            print(f"Not enough space to create file '{name}' in '{parent_directory.name}'")

    def delete_file(self, parent_directory, name):
        for file in parent_directory.files:
            if file.name == name:
                self.deallocate_blocks(file.blocks)
                parent_directory.files.remove(file)
                print(f"File '{name}' deleted from '{parent_directory.name}'.")
                return

        print(f"Error: File '{name}' not found in '{parent_directory.name}'.")

    def create_directory(self, parent_directory, name):
        if any(directory.name == name for directory in parent_directory.subdirectories):
            print(f"Error: A directory with the name '{name}' already exists in '{parent_directory.name}'.")
            return

        new_directory = Directory(name)
        parent_directory.subdirectories.append(new_directory)
        print(f"Directory '{name}' created in '{parent_directory.name}'")

    def delete_directory(self, parent_directory, name):
        for directory in parent_directory.subdirectories:
            if directory.name == name:
                if directory.files or directory.subdirectories:
                    print(f"Error: Directory '{name}' is not empty. Delete its contents first.")
                    return

                parent_directory.subdirectories.remove(directory)
                print(f"Directory '{name}' deleted from '{parent_directory.name}'.")
                return

        print(f"Error: Directory '{name}' not found in '{parent_directory.name}'.")

    def list_directory_contents(self, directory):
        print(f"Contents of directory '{directory.name}':")
        for subdirectory in directory.subdirectories:
            print(f" [D] {subdirectory.name}")
        for file in directory.files:
            print(f" [F] {file.name} - Size: {file.size} Blocks: {file.blocks}")

    def print_memory_status(self):
        used_blocks = sum(self.memory)
        free_blocks = len(self.memory) - used_blocks
        print(f"Memory Status: Used blocks: {used_blocks}, Free blocks: {free_blocks}")

# Exemplo de uso
if __name__ == "__main__":
    block_size = 4  # Tamanho do bloco em unidades arbitrarias
    memory_size = 16  # Tamanho da memória física em unidades arbitrarias

    fs_simulator = FileSystemSimulator(block_size, memory_size)

    root = fs_simulator.root
    fs_simulator.create_file(root, "file1.txt", 6)
    fs_simulator.create_file(root, "file2.txt", 4)
    fs_simulator.create_directory(root, "dir1")

    dir1 = root.subdirectories[0]
    fs_simulator.create_file(dir1, "file3.txt", 3)

    fs_simulator.list_directory_contents(root)
    fs_simulator.print_memory_status()
    
    fs_simulator.delete_file(root, "file2.txt")
    fs_simulator.list_directory_contents(root)
    fs_simulator.print_memory_status()
    
    fs_simulator.delete_directory(root, "dir1")
    fs_simulator.list_directory_contents(root)
    fs_simulator.print_memory_status()
