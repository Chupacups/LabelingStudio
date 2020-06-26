import json

datas = []
levels = []
biomes = []
kinds = []

with open('../Json/labellingResult.json') as json_file:
    loaded = json.load(json_file)
    for JsonData in loaded:
        if 'image_src' in JsonData:
            src = JsonData['image_src']
            if 'Level of Organization' in JsonData:
                level = JsonData['Level of Organization']

            if 'Terrestrial Biome' in JsonData:
                biome = JsonData['Terrestrial Biome']
            if 'Aquatic Biome' in JsonData:
                biome = JsonData['Aquatic Biome']

            biome = biome.replace(" ", "-")

            if 'tag' in JsonData:
                kind = ""
                for temp in JsonData['tag']:
                    if kind.find(temp['polygonlabels'][0]) == -1:
                        kind += temp['polygonlabels'][0] + " "
                kind = kind.strip()

            tags = level + " " + biome + " " + kind

            datas.append({
                'src': src,
                'srct' : src,
                'title' : "",
                'tags' : tags
            })

            levels.append({
                'src': src,
                'srct' : src,
                'title' : "",
                'tags' : level
            })

            biomes.append({
                'src': src,
                'srct' : src,
                'title' : "",
                'tags' : biome
            })

            kinds.append({
                'src': src,
                'srct' : src,
                'title' : "",
                'tags' : kind
            })

with open("../Json/newResult.json", "w") as json_file:
    json.dump(datas, json_file, indent=4)

with open("../Json/levels.json", "w") as json_file:
    json.dump(levels, json_file, indent=4)
    
with open("../Json/biomes.json", "w") as json_file:
    json.dump(biomes, json_file, indent=4)
    
with open("../Json/kinds.json", "w") as json_file:
    json.dump(kinds, json_file, indent=4)