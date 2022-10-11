import json

# path destination source/destination, NOT MAP ONES !!!
sources_train = ['promet-kc/_izvor/Ž_BT-KC_source.geojson', 'promet-kc/_izvor/Ž_ČK-KC_source.geojson', 'promet-kc/_izvor/Ž_VT-KC_source.geojson', 'promet-kc/_izvor/Ž_ZG-KC_source.geojson']
destinations_train = ['promet-kc/vlak/Ž_BT-KC.json', 'promet-kc/vlak/Ž_ČK-KC.json', 'promet-kc/vlak/Ž_VT-KC.json', 'promet-kc/vlak/Ž_ZG-KC.json']

# path destination source/destination, NOT MAP ONES !!!
sources_bus = ['promet-kc/_izvor/B_B_L1_source.geojson']
destinations_bus = ['promet-kc/bus/B_B_L1.json']


def reformat(source, destination, count = 0):
    with open(source) as f:
        gj = json.load(f)
    features = gj['features']

    nd = []

    for i in features[0]["geometry"]["coordinates"]:
        nd.append([i[1], i[0]])
        count += 1

    print(nd)
        
    with open(destination, "w", encoding = "utf-8",) as of:
        json.dump(nd, of, indent = 4)


for i in range(len(sources_train)):
    reformat(sources_train[i], destinations_train[i])
    
for i in range(len(sources_bus)):
    reformat(sources_bus[i], destinations_bus[i])
    