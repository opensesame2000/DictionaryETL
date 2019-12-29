# coding=utf-8
import json
import datetime

totalist = []
# list of (1 word to meaninglists)
def convert_csv_to_wmlist(file):

    # Open file
    fileHandler = open(file, "r")
    # Get list of all lines in file
    listOfLines = fileHandler.readlines()
    # Close file
    fileHandler.close()

    cnt = 0
    for line in listOfLines:
        wordl = []
        meaningsl = []
        wmdict1 = {}
        values = line.split("\t")
        word = values[0].strip()
        data = values[1].strip()
        if (data.find(";")):
            data = data.split(";")
        data = [x.strip() for x in data]
        meaningsl = data
        cnt = cnt + 1
        wmdict1["Word"] = word
        #compose meanings
        tlist = get_list_of_mdicts(meaningsl)
        wmdict1["Meanings"] = tlist
        totalist.append(wmdict1)
    return totalist


def get_list_of_mdicts(mlistrow):
    # composing [meandict, meandict, meandict, ....]
    mlist = []
    # iterating mlistrow
    for i in range(0, len(mlistrow)):
        md = {}
        md["Example"] = "None"
        md["Qualifier"] = "None"
        md["Source"] = "தமிழ் - தமிழ் அகர முதலி"
        print(mlistrow[i])
        md["Meaning"] = mlistrow[i]
        mlist.append(md)
    return mlist

def get_json(tlist1):
    totallist = []
    for j in range(0, len(tlist1)):
        wmdict2 = tlist1[j]
        jrow_dict = {}
        jrow_dict["d_id"] = str(j)
        #composing all JSON -> n jrow_dict
        for i in range(0, len(wmdict2)):
            jrow_dict["Word"] = wmdict2["Word"]
            jrow_dict["Meanings"] = wmdict2["Meanings"]
            now = str(datetime.datetime.utcnow())
            jrow_dict["Created"] = now
            jrow_dict["Updated"] = now
        totallist.append(jrow_dict)
    return totallist


def get_json_file(jdata):
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(jdata, f, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    templist = convert_csv_to_wmlist("input.csv")
    res_json = get_json(templist)
    get_json_file(res_json)


