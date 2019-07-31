
from nltk.translate.bleu_score import sentence_bleu
import xlrd

# Give the location of the file
#if sheet.cell_value(i,0)==0:
#   score= str(sentence_bleu(reference, candidate, weights=(1, 0, 0, 0)))+ ','+ str(sentence_bleu(reference, candidate, weights=(0, 1, 0, 0)))+','+ str(sentence_bleu(reference, candidate, weights=(0, 0, 1, 0)))+','+ str(sentence_bleu(reference, candidate, weights=(0, 0, 0, 1)))+','+ str(sentence_bleu(reference, candidate, weights=(0.5, 0.5, 0, 0)))+','+ str(sentence_bleu(reference, candidate, weights=(0.33, 0.33, 0.33, 0)))+','+ str(sentence_bleu(reference, candidate, weights=(0.25, 0.25, 0.25, 0.25)))+',Human-generated' '''''' else:
#       score= str(sentence_bleu(reference, candidate, weights=(1, 0, 0, 0)))+ ','+ str(sentence_bleu(reference, candidate, weights=(0, 1, 0, 0)))+','+ str(sentence_bleu(reference, candidate, weights=(0, 0, 1, 0)))+','+ str(sentence_bleu(reference, candidate, weights=(0, 0, 0, 1)))+','+ str(sentence_bleu(reference, candidate, weights=(0.5, 0.5, 0, 0)))+','+ str(sentence_bleu(reference, candidate, weights=(0.33, 0.33, 0.33, 0)))+','+ str(sentence_bleu(reference, candidate, weights=(0.25, 0.25, 0.25, 0.25)))+',Machine-generated' '''

loc = ("/Users/ishitagupta/Desktop/kashgari_data.xlsx")

# To open Workbook
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(1)
i=0
for i in range(1,3999):
    textreference = sheet.cell_value(i, 0)
    textcandidate = sheet.cell_value(i, 1)
    print(textreference.split())
    print(textcandidate.split())
    
    reference = [textreference.split()]
    candidate = textcandidate.split()
    
    score= str(round(1000*sentence_bleu(reference, candidate, weights=(1, 0, 0, 0))))+ ','+ str(round(1000*sentence_bleu(reference, candidate, weights=(0, 1, 0, 0))))+','+ str(round(1000*sentence_bleu(reference, candidate, weights=(0, 0, 1, 0))))
    print(score)





