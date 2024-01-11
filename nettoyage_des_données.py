import pandas as pd

# Fonction pour convertir les chaînes de pourcentage et de monnaie en numérique
def convert_to_numeric(s):
    # Enlever '%' et ',' puis convertir en float
    if isinstance(s, str):
        return float(s.replace('%', '').replace(',', '').replace('+', '').replace('$', ''))
    else:
        return s

# Convertir 'Following' et 'Followers' en entiers
df['Following'] = df['Following'].astype(int)
df['Followers'] = df['Followers'].astype(int)

# Supprimer le texte de 'Weekly Ranking' et convertir en entier
df['Weekly Ranking'] = df['Weekly Ranking'].str.extract('(\d+)').astype(int)

# Appliquer la conversion aux autres colonnes
for col in ['Daily ROI', 'Daily PNL (USD)', 'Weekly ROI', 'Weekly PNL (USD)', 'Monthly ROI', 'Monthly PNL (USD)', 'Total ROI', 'Total PNL']:
    df[col] = df[col].apply(convert_to_numeric)

# Afficher le DataFrame mis à jour
df
