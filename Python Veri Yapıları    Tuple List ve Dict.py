# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 16:33:40 2022

@author: merve
"""
#Sırasıyla 10'dan 20'ye kadar olan (20 dahil) tamsayıları içeren, ardından alfabenin "abcdefghijklmnopqrstuvwxyz" harflerini içeren bir "list" verisi
liste = list(range(10,21)) + list("abcdefghijklmnopqrstuvwxyz") 
print(liste)
print(len(liste)) #listenin uzunluğu
liste.remove('k') #listeden 'k' harfini çıkarılması ve ardından listenin yazdırılması
print(liste)
liste.append('a') #listeye sırasıyla 'a' karakterinin, 3 rakamınbın, 'a' karakterinin ve 58 sayısının eklenmesi
liste.append(3)
liste.append('a')
liste.append(58)
print(liste.count('a')) #listedeki 'a' karakterinin tekrarlanma sayısını bulunması ve ardından ekrana yazdırılması
del liste[17:27]
print(liste)