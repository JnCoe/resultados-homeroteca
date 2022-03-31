# Importing libraries
import sys
from bs4 import BeautifulSoup
import pandas as pd

# Open html file passed as argument
with open(sys.argv[1], 'r') as f:
    soup = BeautifulSoup(f, 'html.parser')

# Create pandas dataframe with columns: ano, edicao, count
df = pd.DataFrame(columns=['ano', 'edicao', 'count'])

# Get all divs from results
div_list = soup.find_all('div', class_=['rtTop', 'rtMid'])

for div in div_list:
    # Check if div.text contains string
    if 'Ano' in div.text.strip():
        # Split div.text.strip
        title = div.text.strip().split(' ')
        ano = title[1]

    else:
        if div.img:
            # Filtering positive results
            if div.img['src'] == '/DocReader/Skin/BN/FolderGreenClose.png':
                # Save text of div trimmed into variable
                edicao = div.text.strip()
                # Split edicao at space
                edicao = edicao.split(' ')

                # Remove parenthesis from count
                edicao[2] = edicao[2].replace('(', '')
                edicao[2] = edicao[2].replace(')', '')

                # Concat results to df
                df = df.append({'ano': ano, 'edicao': edicao[1], 'count': edicao[2]}, ignore_index=True)

            # Filtering negative results
            elif div.img['src'] == '/DocReader/Skin/BN/FolderYellowClose.png':
                # Save text of div trimmed into variable
                edicao = div.text.strip()
                # Split edicao at space
                edicao = edicao.split(' ')

                # Concat results to df
                df = df.append({'ano': ano, 'edicao': edicao[1], 'count': 0}, ignore_index=True)

# Export df to clipboard
df.to_clipboard()