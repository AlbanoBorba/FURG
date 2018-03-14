#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import ceil
from bitmap import BitMap

class File:
    def __init__(self, name, index, size = 0):
        self.name = name
        self.size = size
        self.first_block = index
    def get_name(self):
        return self.name

    def get_block(self):
        return self.first_block

    def get_size(self):
        return self.size

class Directory:
    def __init__(self, name, obj):
        self.name = name
        self.parent = obj
        self.directories = []
        self.files = []

    def add_directory(self, obj):
        self.directories.append(obj)

    def add_file(self, obj):
        self.files.append(obj)

    def delete_directory(self, obj):
        self.directories.remove(obj)

    def delete_file(self, obj):
        self.files.remove(obj)

    def get_directories(self):
        return self.directories

    def get_files(self):
        return self.files

    def get_parent(self):
        return self.parent

    def get_name(self):
        return self.name

class FileSystem:
    def __init__(self, partition_size = 2048, block_size = 32):
        self.num_blocks = int(partition_size/block_size)
        self.block_size = block_size
        self.partition_size = partition_size
        self.partition = [0]*self.num_blocks
        self.bit_map = BitMap(block_size)
        self.root = Directory('root', None)
        self.actual_dir = self.root
        self.table = [" "]*self.num_blocks

    def findBlock(self, size):
        needed = ceil((1.0*size)/self.block_size)
        count = 0
        blocks = []
        for index, block in enumerate(self.partition):
            if block == 0:
                count += 1
                blocks.append(index)
                if count == needed:
                    return blocks
        return []

    def fillTable(self, block_list):
        for i in range(len(block_list)):
            if i != len(block_list) - 1:
                self.table[block_list[i]] = str(block_list[i+1])
            else:
                self.table[block_list[i]] = "-1"
    def showTable(self):
        for index, block in enumerate(self.table):
            print "| {0:>3} | {1:>3} |".format(index, block)

    def changeDir(self, target):
        if target == "..":
            if self.actual_dir != self.root:
                self.actual_dir = self.actual_dir.get_parent()
                return True
            else:
                print "Não existe diretório superior a este"
                return False
        else:
            directories = self.actual_dir.get_directories()
            for dir in directories:
                if dir.get_name() == target:
                    self.actual_dir = dir
                    return True
            print "Este não é um diretório válido"
            return False

    def makeDir(self, dir_name):
        directories = self.actual_dir.get_directories()
        for dir in directories:
            if dir.get_name() == dir_name:
                print "Diretório já existente"
                return False
        self.actual_dir.add_directory(Directory(dir_name, self.actual_dir))
        return True

    def listContent(self):
        directories = self.actual_dir.get_directories()
        files = self.actual_dir.get_files()
        for dir in directories:
            print "D", dir.get_name()
        for f in files:
            blocks = ceil((1.0*f.get_size())/self.block_size)
            print "A", f.get_name(), f.get_size(), int(blocks)
        return

    def makeFile(self, file_name, file_size):
        name, ext = file_name.split('.')
        if len(name) > 8:
            print "Nome do arquivo deve conter no máximo 8 caracteres"
            return False
        if len(ext) > 3:
            print "Nome da extensão deve conter no máximo 3 caracteres"
            return False
        files = self.actual_dir.get_files()
        for f in files:
            if f.get_name() == file_name:
                print "Arquivo já existente"
                return False
        blocks_used = self.findBlock(file_size)
        self.fillTable(blocks_used)
        if blocks_used:
            self.actual_dir.add_file(File(file_name, blocks_used[0], file_size))
            for index in blocks_used:
                self.partition[index] = min(file_size, self.block_size)
                file_size -= min(file_size, self.block_size)
            return True
        else:
            print "Não há espaço no disco"
            return False

    def deleteFile(self, file_name):
        files = self.actual_dir.get_files()
        for f in files:
            if f.get_name() == file_name:
                first = f.get_block()
                last = first + ceil((1.0*f.get_size())/self.block_size)
                for i in range(int(first), int(last)):
                    self.partition[i] = 0
                nx = int(self.table[first])
                self.table[first] = ' '
                while True:
                    if nx == -1:
                        break
                    tmp = int(self.table[nx])
                    self.table[nx] = ' '
                    nx = tmp
                self.actual_dir.delete_file(f)
                return True
        print "Este arquivo não existe"
        return False

    def get_path(self, now):
        if now == self.root:
            return "~"
        else:
            return self.get_path(now.get_parent()) + "/%s" % now.get_name()

    def showPartition(self):
        for block in self.partition:
            for i in range(self.block_size):
                if i < block:
                    print "+",
                else:
                    print "-",
            print ""

    def showDirectories(self, dir, identation = 0):
        directories = dir.get_directories()
        files = dir.get_files()
        if identation == 0:
            print dir.get_name()
        else:
            print " "*(identation-4) + "|-->" + dir.get_name()
        for f in files:
            print " "*identation + "|-->" + f.get_name()
        for d in directories:
            self.showDirectories(d, identation + 4)

    def saveCommands(self, history, log_name):
        f = open(log_name, "w")
        for cmd in history:
            f.write(cmd + "\n")

    def loadCommands(self, log_name):
        f = open(log_name + "_state", "r")
        self.actual_dir = self.root
        for line in f:
            cmd_list = line.split()
            if cmd_list[0] == "mkdir":
                self.makeDir(cmd_list[1])
            elif cmd_list[0] == "cd":
                self.changeDir(cmd_list[1])
            elif cmd_list[0] == "criar":
                self.makeFile(cmd_list[1], int(cmd_list[2]))
            elif cmd_list[0] == "excluir":
                self.deleteFile(cmd_list[1])

    def showHelp(self):
        print "O que você quer fazer?"
        print "Trocar de diretório: cd NOME_DIRETORIO"
        print "Voltar para o diretório anterior: cd .."
        print "Listar o conteúdo do diretório atual: ls"
        print "Criar um diretório: mkdir NOME_DIRETORIO"
        print "Criar um arquivo: criar NOME_ARQUIVO.EXT TAM_ARQUIVO"
        print "Excluir um arquivo: excluir NOME_ARQUIVO.EXT"
        print "Mostrar o mapa de bits: listamapa"
        print "Mostrar a árvore de diretórios: showtree"
        print "Salvar o estado da partição atual: save NOME_PARTIÇÃO"
        print "Carregar uma partição salva: load NOME_PARTIÇÃO"
        print "Sair do sistema de arquivos: quit"
    def interact(self):
        self.command_history = []
        #self.files_here = []
        command = ""
        while(command != "quit"):
            command = raw_input(self.get_path(self.actual_dir) + "$ >")
            cmd_list = command.split()
            if cmd_list[0] == "mkdir":
                if len(cmd_list) == 2:
                    if self.makeDir(cmd_list[1]):
                        self.command_history.append(command)
                else:
                    print "Informe o nome da pasta"
            elif cmd_list[0] == "cd":
                if len(cmd_list) == 2:
                    if self.changeDir(cmd_list[1]):
                        self.command_history.append(command)
                else:
                    print "Informe o nome da pasta"
            elif cmd_list[0] == "ls":
                self.listContent()
            elif cmd_list[0] == "criar":
                if len(cmd_list) == 3:
                    if self.makeFile(cmd_list[1], int(cmd_list[2])):
                        self.command_history.append(command)
                else:
                    print "Informe o nome do arquivo e seu tamanho"
            elif cmd_list[0] == "excluir":
                if len(cmd_list) == 2:
                    if self.deleteFile(cmd_list[1]):
                        self.command_history.append(command)
                else:
                    print "Informe o nome do arquivo"
            elif cmd_list[0] == "listamapa":
                self.showPartition()
                self.showTable()
            elif cmd_list[0] == "showtree":
                self.showDirectories(self.root)
            elif cmd_list[0] == "save":
                if len(cmd_list) == 2:
                    self.saveCommands(self.command_history, cmd_list[1])
                else:
                    print "Informe um nome para a gravação"
            elif cmd_list[0] == "load":
                if len(cmd_list) == 2:
                    self.loadCommands(cmd_list[1])
                else:
                    print "Informe o nome da gravação para ser carregada"
            elif cmd_list[0] == "help":
                self.showHelp()
            elif cmd_list[0] != "quit":
                print "Comando inválido. Digite help para ajuda"


FAT32 = FileSystem(2048, 32)
FAT32.interact()
