import PySimpleGUI as sg
import os.path
import RetrieveShowdown as rsd
import Showdown as sd
import pokeapi as pa
import webbrowser

#2 column window layout
file_list_column = [
    [
        sg.Text("Type in the index of the pokemon you want to view (1-151):"),
        sg.In(size = (25,1), enable_events = True, key = "-SEARCH-ITEM-"),
        sg.Button("Search")
        #sg.FolderBrowse()
    ],
]

#Shows the name of the chosen file
image_viewer_column = [
    [sg.Text( key="-NAME-")],
    [sg.Text(size=(40,1), key="-JPNAME-")],
    [sg.Text(size=(40,1), key="-TYPE-")],
    [sg.Text(key="-STAT-")],
    [sg.Text(size=(40,1), key="-WEIGHT-")],
    [sg.Text(size=(40,1), key="-HEIGHT-")],
    [sg.Text(key="-MOVES-")],
    [sg.Text(size=(40,10), key="-CRY-")],
    [sg.Image(key="-IMAGE-")],
]

#full layout
layout = [
    [
        sg.Column(file_list_column),
        sg.VSeperator(),
        sg.Column(image_viewer_column)
    ]
]

window = sg.Window("Image Viewer", layout)

#event loop
while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break

    # pokemon index was filled in
    if event == "Search":
        print(os.getcwd()+"\pokeImg")
        searchItem = values["-SEARCH-ITEM-"]
        print (searchItem)

        if int(searchItem) in range (1, 152):
            try:
                name = rsd.getDex(int(searchItem))
                types =" ".join(rsd.getTypes(name))
                stats =rsd.getStats(name)
                moves =pa.getEntry(name)

                window["-NAME-"].update("NAME "+name)
                window["-JPNAME-"].update("JAPANESE NAME "+pa.getJpnname(name))
                window["-TYPE-"].update("TYPES "+types)
                window["-STAT-"].update("STATS "+stats)
                window["-WEIGHT-"].update("WEIGHT "+str(rsd.getWeight(name)))
                window["-HEIGHT-"].update("HEIGHT "+str(rsd.getHeight(name)))
                window["-MOVES-"].update("DESC "+moves)
                webbrowser.open('https://unpkg.com/pokeapi-sprites@2.0.2/sprites/pokemon/other/dream-world/' + str(searchItem) + '.svg', new = 1)
                #window["-IMAGE-"].update(filename = os.getcwd()+"\pokeImg\/"+searchItem+".png")
 
            except:
                pass

window.close()