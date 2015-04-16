#!/usr/bin/python3
#-*- coding: utf-8 -*-


import os 
import re
import zipfile as zf


def properPATH(chemin):
    var = str(chemin)
    if var == "":
        return (False, False)
    if "..." in var:
        return (False, False)
    if var == "." or var == ".." or var == '/':
        return (str(var), False)
    if var[0] == '/':
        os.chdir('/')
        var = var[1:]
    slashes = var.count('/')
    if slashes:
        var = var.replace('//', '/')
        if var[-1] == "/":
            try:
                os.chdir(var)
                return (os.getcwd(), False)
            except:
                return (False, False)
        else:
            Liste = var.split('/')
            lastItem = Liste[-1]
            Liste.pop()
            for i in Liste:
                try:
                    os.chdir(str(i))
                except:
                    return (False, False)
            if lastItem in os.listdir():
                try:
                    os.chdir(str(lastItem))
                    return (os.getcwd(), False)
                except:
                    return (os.getcwd(), str(lastItem))
            else:
                return (os.getcwd(), False)
    else:
        try:
            os.chdir(var)
            return (os.getcwd(), False)
        except:
            if var in os.listdir():
                return (os.getcwd(), str(var))
            else:
                return (False, False)


def properPATH2file(chemin):
    var = str(chemin) 
    if var == "":
        return (False, False)
    if "..." in var:
        return (False, False)
    if var == "." or var == ".." or var == '/':
        return (str(var), False)
    if var[0] == '/':
        os.chdir('/')
        var = var[1:]
    slashes = var.count('/')
    if slashes:
        var = var.replace('//', '/')
        if var[-1] == "/":
            try:
                os.chdir(var)
                return (os.getcwd(), False)   
            except:
                return (False, False) 
        #
        else:
            Liste = var.split('/')
            lastItem = Liste[-1]
            #~ print(lastItem) #
            Liste.pop()
            #~ print(Liste) #
            for i in Liste:
                try:
                    os.chdir(str(i))
                except:
                    return (False, False)
            if lastItem in os.listdir():
                try:
                    os.chdir(str(lastItem))
                    #~ print("toto")
                    return (os.getcwd(), False) 
                except:
                    #~ print("tutu")
                    return (os.getcwd(), str(lastItem))  
            else:
                #~ print("titi")
                return (os.getcwd(), str(lastItem), False)   # changé par rapport à properPATH. On veut pouvoir créer un fichier, s'il n'existe pas.
    else:
        try:
            os.chdir(var)
            return (os.getcwd(), False)  
        except:
            if var in os.listdir():
                return (os.getcwd(), str(var))  
            else:
                return (False, False)


def unzipODT(fichierIn, fichierOut):
    ''' Tests nécessaires pour dézipper le ficheier d'entrée
    Retourne True si succès, False sinon.
    '''
    chemin1, fichier1 = properPATH(fichierIn)
    fichierIn = chemin1 + '/' + fichier1
    if not chemin1 or not fichier1:
        return False
    if not zf.is_zipfile(chemin1 + '/' + fichier1):
        print("Pas un zip.")
        return False
    myZip = zf.ZipFile(fichierIn)
    inZip = myZip.namelist()
    print("L'archive contient : ")
    for i in inZip:
        print(' -  ' + str(i))
    tmp = properPATH2file(fichierOut)
    if len(tmp) == 2:
        chemin2, fichier2 = tmp
    elif len(tmp) == 3:
        chemin2, fichier2, void = tmp
        #~ del void 
    print("akjhbvkjhjkahgfkjahgzfkjagjkf " + str(fichier2))
    if chemin2:
        fichierOut = chemin2 + '/' + fichier2
        fw = open(fichierOut, 'w')
        fr = myZip.open("content.xml", 'rU')
        data = fr.read()
        print(str(data[2:20])[2:], str(data[2:20])[-20:-1])
        #~ fw.write(str(data[2:-1])[2:-1])
        fw.write(str(data[2:-1])[2:-1].replace(r'\n', '\n').replace(r'\t', '\t').replace(r'><', '>\n<'))
        #~ fw.write(data)
    return True


fichier1 = '/tmp/maquetteODT.odt'
fichier2 = '/tmp/z/toto'
print(unzipODT(fichier1, fichier2))



































