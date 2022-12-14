import json

A_K = {
    'AUTOBUSNI KOLODVOR' : ['07-45', '08:50','11:50', '12:30', '13:30', '13:50', '14:45', '18:40', '19:20'],
    'TRG MLADOSTI' : ['07:48', '08:53', '11:53', '12:33', '13:33', '13:53', '14:48', '18:43', '19:23'],
    'BOLNICA' : ['07:54', '08:59', '11:59', '12:39', '13:39', '13:59', '14:54', '18:49', '19:29'],
    'STADION' : ['07:58', '09:03', '12:03', '12:43', '13:43', '14:03', '14:59', '18:54', '19:32'],
    'KAMPUS' : ['08:02', '09:07', '12:07', '12:47', '13:47', '14:07', '15:03', '18:58', '19:34'],
}

K_A = {
    'AUTOBUSNI KOLODVOR' : ['06:50', '08:10', '11:20', '12:10', '13:10', '13:30', '14:10', '18:15', '19:00', '19:35'],
    'TRG MLADOSTI' : ['06:53', '08:13', '11:23', '12:13', '13:13', '13:33', '14:13', '18:18', '19:03', '19:37'],
    'BOLNICA' : ['06:57', '08:17', '11:27', '12:17', '13:17', '13:37', '14:19', '18:20', '19:07', '19:41'],
    'STADION' : ['07:02', '08:22', '11:32', '12:22', '13:23', '13:42', '14:23', '18:25', '19:13', '19:46'],
    'KAMPUS' : ['07:06', '08:26', '11:36', '12:26', '13:27', '13:46', '14:26', '18:29', '19:16', '19:49'],
}


točke = ['AUTOBUSNI KOLODVOR', 'TRG MLADOSTI', 'BOLNICA', 'STADION', 'KAMPUS']


fotografije = {
    "AUTOBUSNI KOLODVOR" : "slike/autobusni.jpg",
    "TRG MLADOSTI" : "slike/mladosti.jpg",
    "BOLNICA" : "slike/bolnica.jpg",
    "STADION" : "slike/stadion.jpg",
    "KAMPUS" : "slike/kampus.jpg"
}


T_B_L1_OUTPUT = {}

# in case locations are imported from geojson format
with open('promet-kc/_izvor/T_B_L1.geojson') as f:
    gj = json.load(f)
features = gj['features']


for i in range(len(features)):
    tmp = features[i]['geometry']['coordinates']
    T_B_L1_OUTPUT[točke[i]] = {
        'X' : tmp[1],
        'Y' : tmp[0],
        'K-A' : K_A[točke[i]],
        'A-K' : A_K[točke[i]],
        'FOTOGRAFIJA' : fotografije[točke[i]]
        }
    
    
with open("promet-kc/bus/T_B_L1.json", "w", encoding = "utf-8",) as of:
    json.dump(T_B_L1_OUTPUT, of, indent = 4)