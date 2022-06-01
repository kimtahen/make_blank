from konlpy.tag import Kkma
import random
import pandas as pd
module = Kkma()
def make_blank(target):
    strArr = target.split(" ");
    list = [];

    for word in strArr:
        tmp = module.nouns(word)
        if len(tmp) > 0 and len(tmp[-1])>=2:
            list.append(tmp[-1]);

    idx = 0;

    result = "";

    for word in strArr:
        choice = random.randrange(1,11);
        if(idx<len(list) and word.find(list[idx])!=-1):
            if 1<=choice<=10:
                result+= word.replace(list[idx], "(    )") + " ";
            else :
                result+= word + " ";
            idx += 1;
        else:
            result+= word + " ";
    return result;

def main():
    df = pd.read_csv('./data.csv',delimiter='|');    
    for row in df.itertuples():
        df.iloc[row[0]] = (row[1],make_blank(row[2]));
    for row in df.itertuples():
        print(row);
    
    return;
if __name__ == "__main__":
    main();

