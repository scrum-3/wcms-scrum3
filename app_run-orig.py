from flask import *

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def group():
    output = ""
    with open("2a_raw.txt") as fh:
        # 逐行讀出檔案資料, 並放入數列中
        lines = fh.readlines()
        # 設法用迴圈逐數列內容取出字串
        # 組序變數 g 起始值設為 0
        g = 0
        for i in range(len(lines)):
            # 利用 strip() 去除各行字串最末端的跳行符號
            #print(lines[i].strip())
            line = lines[i].strip()
            # 利用 split() 將以 \t 區隔的字串資料分離後納入 groups 字串
            groups = line.split("\t")
            #print(groups)
            for i in range(len(groups)):
                # 每組有三名組員
                if i%3 == 0:
                    # 每三位組員組序增量 1
                    g += 1
                    #print()
                    output += "<br />"
                    #print("第" + str(g) + "組:")
                    output += "第" + str(g) + "組:"
                    #print(groups[i])
                    output += groups[i] + " "
                else:
                   output += groups[i] + " "
    return output


@app.route('/w5cdb')
def w5cdb():
    output = "W5b 第一節點名時未到者:<br />"
    with open("cd_w5b.txt", "r", encoding="utf-8") as fh:
        # 逐行讀出檔案資料, 並放入數列中
        lines = fh.readlines()
        raw_data = lines[1:]
        #print(raw_data)
        # 設法用迴圈逐數列內容取出字串
        # k 為集合所有檔案中的學號字串, 先設為空字串
        k = []
        for i in range(len(raw_data)):
            # 利用 strip() 去除各行字串最末端的跳行符號
            raw_line = raw_data[i].strip()
            # 利用 split() 將以 \t 區隔的字串資料分離後納入 groups 字串
            groups = raw_line.split("\t")
            #print(groups)
            # 逐一進入各行中的各字串去除空字串
            for j in range(len(groups)):
                if groups[j] != "":
                    # 除了空字串外, 其餘字串放入 k 數列中
                    k.append(groups[j])
    # 將 k 中只出現一次的字串印出, 即為缺席者名單
    absent = [x for x in k if k.count(x) == 1]
    #print(absent)
    for i in absent:
        output += i + "<br />"
    return output


if __name__ == '__main__':
    app.run(debug=True)
