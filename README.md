# Simulador de Sistema de Arquivos em Python
Este é um simulador simples de sistema de arquivos implementado em Python. O código representa um modelo básico que permite a criação, exclusão e listagem de arquivos e diretórios, além de simular a alocação de blocos de memória.

## Classes Principais
### File
Representa um arquivo no sistema de arquivos.

### Directory
Representa um diretório no sistema de arquivos.

### FileSystemSimulator
Simula o sistema de arquivos, incluindo a alocação de blocos de memória.

## Métodos Principais
 - allocate_blocks: Aloca blocos de memória para um arquivo.
 - deallocate_blocks: Desaloca blocos de memória previamente alocados.
 - create_file: Cria um novo arquivo em um diretório especificado.
 - delete_file: Exclui um arquivo de um diretório.
 - create_directory: Cria um novo diretório em um diretório pai.
 - delete_directory: Exclui um diretório de um diretório pai.
 - list_directory_contents: Lista o conteúdo de um diretório.
 - print_memory_status: Imprime o status da memória, indicando blocos usados e livres.

### Exemplo de Uso
```python
  if __name__ == "__main__":
    block_size = 4  # Tamanho do bloco em unidades arbitrárias
    memory_size = 16  # Tamanho da memória física em unidades arbitrárias

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
```
Este exemplo demonstra a utilização das principais funcionalidades do simulador, incluindo a criação e exclusão de arquivos/diretórios, listagem de conteúdo e exibição do status da memória.
