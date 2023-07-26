import json, os
from CreamyUI.object.normal import *
from CreamyUI.function import *

necessary = ["reload", "caption", "background", "objects", "connector"]
mapper = {
    "image":image,
    "text":text
}

def loader(path:str) -> dict:
    loaded:dict = {
        "caption":"Creamy Window",
        "objects":[],
        "connector":{}
    }

    exist = os.path.isfile(path)
    if (not exist): print("File Doesn't Exist"); return loaded
    if (not path.endswith(".json")): print("Not Json File"); return loaded

    opened:dict
    with open(path, 'r', encoding='utf8') as j:
        opened = json.load(j)

    # check is correct file
    validity = False not in [bool(n in opened) for n in necessary]
    if (not validity): print("Invalid File"); return loaded

    CleanedObject = []
    for object in opened.get("objects", []):
        tag = object.get("tag", "dummy")
        function = mapper.get(tag, dummy)


        CleanedObject.append(
            function(pos=object.get("pos", (0, 0)),
                     size=object.get("size", (0, 0)),
                     path=object.get("path", ""),
                     text=object.get("text", ""),
                     font=object.get("font", "Arial"),
                     fontsize=object.get("fontsize", 16),
                     color=object.get("color", (0, 0, 0)),
                     align=object.get("align", "left")
                     ))

    opened["objects"] = CleanedObject

    return opened