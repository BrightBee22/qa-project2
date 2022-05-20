from flask import Flask, Response, request


app = Flask(__name__)

@app.route('/post/recweapon', methods= ['POST', 'GET'])
def get_threat():

    fortune = request.data.decode('utf 8') 
    guide = fortune.split(",")

    if guide[0] == "Bishaten" and guide[1] == "Great Sword":
        recweapon =  "Bishaten is weak to Ice, therefore I'd recommend the Abominable Great Sword (from the Goss Harag tree)"
    elif guide[0] == "Bishaten" and guide[1] == "Hammer":
        recweapon =  "Bishaten is weak to Ice, therefore I'd recommend the Glacial Crunch (from the Barioth tree)"
    elif guide[0] == "Bishaten" and guide[1] == "Charge Blade":
        recweapon =  "Bishaten is weak to Ice, therefore I'd recommend the Pavadira (from the Barioth tree)" 
    elif guide[0] == "Bishaten" and guide[1] == "Insect Glaive":
        recweapon =  "Bishaten is weak to Ice, therefore I'd recommend the Lagombavarice (from the Lagombi tree)"
    elif guide[0] == "Bishaten" and guide[1] == "Bow":
        recweapon =  "Bishaten is weak to Ice, therefore I'd recommend the Heaven's Glaze (from the Ice tree)"
    elif guide[0] == "Magnamalo" and guide[1] == "Great Sword":
        recweapon =  "Magnamalo is weak to Water, therefore I'd recommend the Akanesasu (from the Mizutsune tree)"
    elif guide[0] == "Magnamalo" and guide[1] == "Hammer":
        recweapon =  "Magnamalo is weak to Water, therefore I'd recommend the Doom Bringer Hammer (from the Almudron tree)"
    elif guide[0] == "Magnamalo" and guide[1] == "Charge Blade":
        recweapon =  "Magnamalo is weak to Water, therefore I'd recommend the Final FieldBlade (from the Mizutsune tree)" 
    elif guide[0] == "Magnamalo" and guide[1] == "Insect Glaive":
        recweapon =  "Magnamalo is weak to Water, therefore I'd recommend the Watercolor Glaive (from the Smithy tree)"
    elif guide[0] == "Magnamalo" and guide[1] == "Bow":
        recweapon =  "Magnamalo is weak to Water, therefore I'd recommend the Hail of Mud (from the Almudron tree)"
    elif guide[0] == "Rathalos" and guide[1] == "Great Sword":
        recweapon =  "Rathalos is weak to Thunder, therefore I'd recommend the Great Demon Rod (from the Rajang tree)"
    elif guide[0] == "Rathalos" and guide[1] == "Hammer":
        recweapon =  "Rathalos is weak to Thunder, therefore I'd recommend the Super Nova (from the Thunder tree)"
    elif guide[0] == "Rathalos" and guide[1] == "Charge Blade":
        recweapon =  "Rathalos is weak to Thunder, therefore I'd recommend the Despot's Thundergale (from the Zingore tree)" 
    elif guide[0] == "Rathalos" and guide[1] == "Insect Glaive":
        recweapon =  "Rathalos is weak to Thunder, therefore I'd recommend the Full Bolt Chamber (from the Khezu tree)"
    elif guide[0] == "Rathalos" and guide[1] == "Bow":
        recweapon =  "Rathalos is weak to Thunder, therefore I'd recommend the Flying Kadachi Striker (from the Tobi-Kadachi tree)"
    elif guide[0] == "Valstrax" and guide[1] == "Great Sword":
        recweapon =  "Valstrax is weak to Blast, therefore I'd recommend the Sinister Shadeblade (from the Magnamalo tree)"
    elif guide[0] == "Valstrax" and guide[1] == "Hammer":
        recweapon =  "Valstrax is weak to Blast, therefore I'd recommend the Teostra Cratergouger (from the Teostra tree)"
    elif guide[0] == "Valstrax" and guide[1] == "Charge Blade":
        recweapon =  "Valstrax is weak to Blast, therefore I'd recommend the Sinister Shade Axe (from the Magnamalo tree)"  
    elif guide[0] == "Valstrax" and guide[1] == "Insect Glaive":
        recweapon =  "Valstrax is weak to Blast, therefore I'd recommend the Sinister Shadowstaff (from the Magnamalo tree)"
    elif guide[0] == "Valstrax" and guide[1] == "Bow":
        recweapon =  "Valstrax is weak to Blast, therefore I'd recommend the Bow of Light & Courage (from the Teostra tree)"
    elif guide[0] == "Chameleos" and guide[1] == "Great Sword":
        recweapon =  "Chameleos is weak to Fire, therefore I'd recommend the Rathalos Firesword (from the Rathalos tree)"
    elif guide[0] == "Chameleos" and guide[1] == "Hammer":
        recweapon =  "Chameleos is weak to Fire, therefore I'd recommend the Pheonix Fury (from the Anjanath tree)"
    elif guide[0] == "Chameleos" and guide[1] == "Charge Blade":
        recweapon =  "Chameleos is weak to Fire, therefore I'd recommend the Biting Edge II (from the Rakna-Kadaki tree)"  
    elif guide[0] == "Chameleos" and guide[1] == "Insect Glaive":
        recweapon =  "Chameleos is weak to Fire, therefore I'd recommend the Rielle Vermiglio (from the Bnahabra tree)"
    elif guide[0] == "Chameleos" and guide[1] == "Bow":
        recweapon =  "Chameleos is weak to Fire, therefore I'd recommend the Dark Filamant (from the Rathalos tree)"
    return Response(recweapon, mimetype = 'text/plain')

if __name__ == '__main__':
    app.run(port=5003, debug=True, host='0.0.0.0')