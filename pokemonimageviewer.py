##################
#Comp593 lab 9
#created Aaron Gumba
#april 22,2022
#python script that uses Gui to set desktop background after it gets its info from PokeAPI
#usage python pokemonimageviewer.py path
##############


from tkinter import *
from tkinter import ttk
import sys
import os
import ctypes
from pokeapi import get_pokemon_list, get_pokemon_image_url
import requests

def main():
    
    
    #path of the user directory
    script_dir = sys.path[0]
    
    #path to save the pokemon pics
    image_dir = os.path.join(script_dir,'images')
    
    #check if directory exist, if not creates it
    if not os.path.isdir(image_dir):
        os.makedirs(image_dir)
    
    
    #creates the window
    root =Tk()
    root.title('Pokemon Image Viewer')
   
    
    #set the task manager icons and adjust according to the user's expansion of the page
    app_id = 'COMP593.PokemonImageViewer'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id) 
    root.iconbitmap(os.path.join(script_dir,'Poke-Ball.ico'))
    root.columnconfigure(0,weight =1) 
    root.rowconfigure(0,weight =1) 
    
    
    #creates the frame that adjust according to the user's expansion of the page
    frm = ttk.Frame(root)
    frm.grid(sticky = (N,S,E,W))
    frm.columnconfigure(0,weight =1) 
    frm.rowconfigure(0,weight =1) 
    
    #displaying the image
    img_pokemon = PhotoImage(file=os.path.join(script_dir,'pokeball.png'))
    lbl_image = Label(frm, image=img_pokemon)
    lbl_image.grid(row=0,column=0,padx =10, pady =10)
    
    pokemon_list = get_pokemon_list(limit=1000)
    
    pokemon_list.sort()

    #the bar for entering pokemon 
    cbo_pokemon_sel =ttk.Combobox(frm,values = pokemon_list, state='readonly')
    cbo_pokemon_sel.set = ('Select a Pokemon')
    cbo_pokemon_sel.grid(row=1,column=0)
    
    
    def handle_cbo_pokemon_sel(event):
        """
        this gets the url when the user put the pokemon name and download it 
        params:
        return:

        
        """
        pokemon_name = cbo_pokemon_sel.get()
        image_url = get_pokemon_image_url(pokemon_name)
        image_path =os.path.join(image_dir,pokemon_name + '.png')
        if download_image_from_url(image_url, image_path):
        
         img_pokemon ['file'] = image_path
         btn_set_desktop.state(['!disabled']) #enable 
        
        
    cbo_pokemon_sel.bind('<<ComboboxSelected>>', handle_cbo_pokemon_sel)
    
    def btn_set_desktop_click():
        """gives the button a job when clicked
        """
        
        pokemon_name = cbo_pokemon_sel.get()
        
        image_path =os.path.join(image_dir,pokemon_name + '.png')
        
        set_desktop_background_image(image_path)
      
    
    #button creation
    btn_set_desktop = ttk.Button (frm, text = 'Set as Desktop Image',command = btn_set_desktop_click)
    btn_set_desktop.state(['disabled'])
    btn_set_desktop.grid(row=2,column=0,padx =10, pady =10)
    
    root.mainloop()
    
def set_desktop_background_image(path):
    """
    this set the selected image as background 

    params path :where the photo resides
    """
    try:
        ctypes.windll.user32.SystemParametersInfoW(20,0,path,3)
    
    except:
        print("Error Setting desktop image")
def download_image_from_url(url,path):
    """
    This download the photo of the pokemon
    
    param url : the url of the pokemon
    param path : the location to save it

    """
    
    if os.path.isfile(path):
        return(path)
    
    
    #download
    resp_msg = requests.get(url)
    
    #check if succesful
    if resp_msg.status_code == 200:
        #open the file and save it  and return the path where it resides
        try:
            img_data = resp_msg.content
            with open (path,'wb') as fp:
                fp.write(img_data)
            return path
        except:
             
            print("Failed to download pokemon.")
            print("Response code:", resp_msg.status_code)
            print(resp_msg.text)
        
        

    
main()