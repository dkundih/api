import json

točke = ['SVEUČILIŠTE SJEVER']

fotografije = ['slike/ebicikli.jpg']

T_E_BICIKLI_OUTPUT = {}

# in case locations are imported from geojson format
with open('promet-kc/_izvor/T_E_bicikli.geojson') as f:
    gj = json.load(f)
features = gj['features']


for i in range(len(features)):
    tmp = features[i]['geometry']['coordinates']
    T_E_BICIKLI_OUTPUT[točke[i]] = {
        'X' : tmp[1],
        'Y' : tmp[0],
        'FOTOGRAFIJA' : fotografije[0]
        }
    
with open("promet-kc/bicikl/električni/T_E_BICIKLI.json", "w", encoding = "utf-8",) as of:
    json.dump(T_E_BICIKLI_OUTPUT, of, indent = 4)
