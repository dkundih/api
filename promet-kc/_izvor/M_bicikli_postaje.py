import json

točke = ['LENIŠĆE', 'CERINE', 'KAMPUS', 'ŽELJEZNIČKI KOLODVOR', 'GROBLJE', 'ZRINSKI TRG', 'DOM MLADIH']

fotografije = ['slike/bicikli.jpg']

T_M_BICIKLI_OUTPUT = {}

# in case locations are imported from geojson format
with open('promet-kc/_izvor/T_M_bicikli.geojson') as f:
    gj = json.load(f)
features = gj['features']


for i in range(len(features)):
    tmp = features[i]['geometry']['coordinates']
    T_M_BICIKLI_OUTPUT[točke[i]] = {
        'X' : tmp[1],
        'Y' : tmp[0],
        'FOTOGRAFIJA' : fotografije[0]
        }
    
with open("promet-kc/bicikl/mehanički/T_M_BICIKLI.json", "w", encoding = "utf-8",) as of:
    json.dump(T_M_BICIKLI_OUTPUT, of, indent = 4)
