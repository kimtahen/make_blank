from konlpy.tag import Kkma
import random
module = Kkma()

def make_blank(target, isJosa, percent):
    if(target==""):
        return ""
    strArr = target.split(" ");
    list = [];

    for word in strArr:
        tmp = module.nouns(word)
        if len(tmp) > 0 and len(tmp[-1])>=2:
            list.append(tmp[-1]);
    
    deleteNum = int(len(list) * (1-percent));
    while deleteNum!=0 :
        list.pop(random.randrange(0,len(list)));
        deleteNum -= 1;
        
    idx = 0;
    result = "";

    for word in strArr:
        if(idx<len(list) and word.find(list[idx])!=-1):
            if(isJosa):
                result+= word.replace(list[idx], "(    )") + " ";
            else :
                result+= "(    )" + " ";
            idx += 1;
        else:
            result+= word + " ";
    return result;