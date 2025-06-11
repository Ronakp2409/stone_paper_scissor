import os

from PyPDF2 import PdfMerger

folder_path = 'C:\Users\Ronak\Downloads'
merger = PdfMerger()

pdf_file = sorted([
  os.path.join(folder_path, file)
  for file in os.listdir(folder_path)
  if file.endswith('.pdf')
])

if not pdf_file:
  print(f"files are not in {folder_path}")

else :
  for file in pdf_file:
    merger.append(file)
    print(f"Merged {file}")