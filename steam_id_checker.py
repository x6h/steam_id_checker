import requests

# path to a steam id list
STEAM_ID_LIST_PATH = "C:\\idlist.txt"
# path to store available id's
STEAM_ID_AVAILABLE_LIST_PATH = "C:\\available_list.txt"
# str.find returns -1 if the string searched for is not found
NOT_FOUND = -1

def is_steam_id_available(steam_id):
    req = requests.get("https://steamcommunity.com/id/{}".format(steam_id), headers={"User-Agent": ""})
    # get raw html
    req_html = req.text

    # search for a string that shows on non-existent profiles
    if req_html.find("The specified profile could not be found.") == NOT_FOUND:
        return False

    return True

if __name__ == "__main__":
    id_list = open(STEAM_ID_LIST_PATH, "rt")
    available_list = open(STEAM_ID_AVAILABLE_LIST_PATH, "at")

    for id in id_list:
        # remove trailing character (a newline character; messes up the request and probably the output)
        id = id.rstrip()

        if is_steam_id_available(id):
            available_list.write("{}\n".format(id))
            print("\t[!] available: {}".format(id))
        else:
            print("[-] taken: {}".format(id))

    available_list.close()
    id_list.close()
