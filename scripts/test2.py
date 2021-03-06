#!/usr/bin/env python

"""
Ce script cherche a tester les nouvelles fn de la classe GeneCluster

Usage : ./test2.py

"""

__auteur__ = "Jean-Simon Brouard"
__date__ = "2019-09-26"

# Importation de modules standards
import sys
import os
from pathlib import Path
#from Bio.Graphics import GenomeDiagram
from Bio import SeqIO
from Bio.SeqFeature import SeqFeature, FeatureLocation
from io import StringIO
from collections import OrderedDict
#import pandas as pd
import numpy
import re
import csv
import glob

# Importation des modules locaux
from foreign_code import prepare_color_dict
from foreign_code import digest_features
from foreign_code import get_coord_gene
from geneCluster import geneCluster
from dock import dock

# Programme principal

if __name__ == "__main__":




	# Initialisons quelques gene clusters

	

	# a0
	a0 = geneCluster("a0")
	geneList = ['A', 'B', 'C']
	strandList = ['+','+','+']
	a0.load(geneList, strandList)
	print('a0: ' + a0.name + '\t' + a0.read())


	# copy the object a0 and rename it
	a1 = a0
	a1.name = 'a1_a_copy_of_a0'
	print('a1: ' + a1.name + '\t' + a1.read())

	# r1
	#r1 = geneCluster("r1")
	#geneList = ['C', 'B', 'A']
	#strandList = ['-','-','-']
	#r1.load(geneList, strandList)

	r1 = a0.reverse()
	r1.name =('inverted_a0') 
	print('r1: ' + r1.name + '\t' + r1.read())




	# u0
	u0 = geneCluster("u0")
	geneList = ['C', '?', 'A']
	strandList = ['-','-','-']
	u0.load(geneList, strandList)
	print('read method: ' + u0.name + '\t' + u0.read())
	print('pretty_read method: ' + u0.name + '\t' + u0.pretty_read())

	# u00
	u00 = geneCluster("u00")
	geneList = ['C', '?', '?', 'A']
	strandList = ['-','-','-','-']
	u00.load(geneList, strandList)
	print(u00.name + '\t' + u00.read())





	# b1
	b1 = geneCluster("b1")
	geneList = ['A', 'B', 'C', 'D']
	strandList = ['+','+','+','+']
	b1.load(geneList, strandList)

	# c1
	c1 = a0
	c1.name='c1'
	c1.add('D', '+')
	c1.add('E', '+')
	print(c1.name + '\t' + c1.read() + ' after the addition')
	

	# d1
	d1 = geneCluster("d1")
	geneList = ['A', 'C', 'D']
	strandList = ['+','+','+']
	d1.load(geneList, strandList)
	print(d1.name + '\t' + d1.read())


	print ('--Testing operator overloading--')

	if a1 == b1:
		print('c1 equal a1')
	else:
		print('c1 not equal a1')

	if a0 != a1:
		print('a0 not equal a1')
	else:
		print('a0 equal a1')



	print ('--Testing isin fn--')


	# a1 vs r1
	if a1.isin(r1):
		print ('yes a1 is in r1')
	else:
		print ('nope a1 is not in r1')
	

	# d1 vs a1
	if d1.isin(a1):
		print ('yes d1 is in a1')
	else:
		print ('nope d1 is not in a1')


	


	# Tentons de travailler avec notre nouvelle classe : dock

	my_dock = dock()


	my_dock.add(a0)
	my_dock.add(a1)
	my_dock.add(c1)
	my_dock.add(r1)

	print('dock size\t' + str(my_dock.size))
	print(my_dock.elems[3].cluster)		# marche!


	# pour avoir le header
	print(my_dock.head.cluster)		# marche!


	print ('testing remove function')
	new_obj_after_removal = u0.remove('?')
	print (new_obj_after_removal.read())


	print ('testing inclusion function')
	# test u0 in u00 (because unknown genes are ignored it should be included)
	if u0.isin(u00):
		print ('yes u0 is in u00')
	else:
		print ('nope u0 is not in u00')




	fromages = ['Cheddar', 'Fin renard', 'brocoli', 'Suisse', 'Gruyere', 'Gouda', 'Emmenthal', 'Brie', 'Oka', 'Camembert', 'Crottes', 'Riopelle']



	index = 4



	for i in range(index, 0, -1):
		print (fromages[i])

	
	for i in range(index, 7, 1):
		print (fromages[i])











