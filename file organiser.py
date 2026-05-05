import os
from pathlib import Path



# ##SETTING THE PATH FOR WORK
# path_dir = input("input the path that you want to organise -- ")
# path = os.chdir(path_dir)
# # print(f"current path is -- {Path.cwd()}")

##LIST OF EXTENSIONS BASED ON FILE TYPE
docs = [".docx", ".pdf", ".txt", ".xlsx", ".pptx", ".csv", ".md", ".rtf", ".odt", ".pages"]
pics = [".jpg", ".jpeg", ".png", ".webp", ".svg", ".gif", ".heic", ".tiff", ".avif", ".psd", ".raw"]
vids = [".mp4", ".mkv", ".mov", ".webm", ".avi", ".wmv", ".flv", ".m4v", ".mpeg", ".vob"]
audio = [".mp3", ".wav", ".m4a", ".flac", ".aac", ".ogg", ".wma", ".aiff", ".opus", ".mid"]


while True:
    ##SETTING THE PATH FOR WORK
    path_dir = input("input the path that you want to organise(input x to cancel) -- ")
    # path = os.chdir(path_dir)

    if path_dir == "x":
        break
    else:
        while True:
            try:
                path = os.chdir(path_dir)
                break
            except FileNotFoundError:
                print(f"{path_dir} not found")
                path_dir = input("input the path that you want to organise(input x to cancel) -- ")


    step2 = input("w=how do u want to sort ur file? ")
    a = "by type"
    b = "by size"
    c = "by date modified"
    print(f"{a}\n{b}\n{c}")

    
    #moving the file
    def move(filename,destination_folder):
        source = Path(f"{path_dir}/{filename}")
        move_to = Path(f"{path_dir}/{destination_folder}")
        move_to.mkdir(exist_ok=True)
        dest = move_to/source.name
        source.rename(dest)
        print(f"moved {filename} to {destination_folder} succesfully !!!")

    
    ##CATEGORISING ACCORDING TO FILETYPE
    #working on the path
    def by_type():
        for p in Path().iterdir():
            if p.suffix in docs:
                move(p, "document")
            elif p.suffix in pics:
                move(p, "picture")
            elif p.suffix in vids:
                move(p, "videos")
            elif p.suffix in audio:
                move(p, "audios")
            else:
                move(p, "others") 
            
    ##CATEGORISING ACCORDING TO TIME

    #date modified
    def by_date_mod():
        time_dict = {}
        mod_time1 = os.stat("PRES_2.jpg").st_mtime

        files_list = [i for a,b,c in os.walk(".") for i in c]
        # date_mod_list = 
        for i in files_list:
            date_mod = os.stat(i).st_mtime
            time_dict[i] = date_mod 

        sorted = dict(sorted(time_dict.items(), key=lambda x: x[1]))

        for i in sorted.keys():
            move(i, path_dir)

    if step2 == a:
        by_type()
    if step2 == c:
        by_date_mod()

