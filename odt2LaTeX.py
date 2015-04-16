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


def unzipODT(fichierIn):
    ''' Tests nécessaires pour dézipper le ficheier d'entrée
    Retourne True si succès, False sinon.
    '''
    chemin, fichier1 = properPATH(fichierIn)
    fichierIn = chemin + '/' + fichier1
    if not chemin or not fichier:
        return False
    if not zf.is_zipfile(chemin + '/' + fichier1):
        print("Pas un zip.")
        return False
    myZip = zf.ZipFile(fichierIn)
    inZip = myZip.namelist()
    print("L'archive contient : ")
    for i in inZip:
        print(' -  ' + str(i))
    return True


fichier = '/tmp/toto.zip'
print(unzipODT(fichier))












