import csv        
#青 161,187,230 肌色 253, 247, 234 赤 250, 128, 114 緑 144, 238, 144 濃い青106, 90, 205 茶色184, 134, 11
def setup():
    size(1080,800)
    frameRate(30)
    detail_im = loadImage("../date/detail.png")
    graph_im = loadImage("../date/graph.png")
    all_im = loadImage("../date/file.png")
    mo_im = loadImage("../date/mouse.png")
    pl_im = loadImage("../date/play.png")
    st_im = loadImage("../date/stop.png")
    cb_im = loadImage("../date/cb.png")
    rcb_im = loadImage("../date/cb_r.png")
    i_im = loadImage("../date/i.png")
    ba_im = loadImage("../date/back.png")
    ba2_im = loadImage("../date/ba2.png")
    de_im = loadImage("../date/detail_word.png")
    br_im = loadImage("../date/braha.png")
    zb_im = loadImage("../date/zibu.png")
    li_im = loadImage("../date/life.png")
    ps_im = loadImage("../date/pas.png")
    ri_im = loadImage("../date/rei.png")
    bn_im = loadImage("../date/bang.png")
    mr_im = loadImage("../date/mira.png")
    ko_im = loadImage("../date/poison.png")
    oc_im = loadImage("../date/oct.png")
    wt_im = loadImage("../date/what.png")
    kr_im = loadImage("../date/kuript.png")
    rv_im = loadImage("../date/revu.png")
    rb_im = loadImage("../date/rb.png")
    mn_im = loadImage("../date/my.png")
    m1_im = loadImage("../date/mi1.png")
    m2_im = loadImage("../date/mi2.png")
    m_bar = 0
    g_pl = 1 #0=停止　1=再生
    g_dr = 0 #0=停止　1=ドラッグ
    sc_mode = 0 #0=初期画面 1=Info画面 2=グラフ描画 3=全データ描画
    ka_max = 0
    rp_max = 0
    p_3 = 1 #全データ画面のページ数
    with open("../date/asjis.csv","r",) as ta:
        table = list(csv.reader(ta))
    global detail_im,graph_im,all_im,mo_im,sc_mode,m_bar,table,g_pl\
           ,st_im,pl_im,rcb_im,cb_im,g_dr,i_im,ba_im,ba2_im,p_3,de_im\
           ,br_im,zb_im,li_im,ps_im,ri_im,bn_im,mr_im,ko_im,oc_im\
           ,wt_im,kr_im,rv_im,rb_im,mn_im,m1_im,m2_im
 
def draw():
    global m_bar
    if sc_mode == 0:
        #初期画面
        #画面表示
        background(253, 247, 234)
        textAlign(CENTER, TOP)
        fill(50)
        textSize(200)
        text("Analysis", width/2,80)
        textSize(80)
        text("detail",   width/2,380)
        text("graph",    width/2,480)
        text("all data", width/2,580)
        image(detail_im, 300, 405)#de
        image(graph_im,  300, 505)#gr
        image(all_im,    300, 605)#al
        image(mo_im,     800, 500)#x=750

        
        #mode選択処理
        strokeWeight(5)
        stroke(161,187,230)
        noFill()
        if mouseX>=280 and mouseX<=690:
            if mouseY>=385 and mouseY<=475:#detail
                rect(280, 385, 410, 90)
            elif mouseY>=485 and mouseY<=575:#graph
                rect(280, 485, 410, 90)
            elif mouseY>=585 and mouseY<=685:#all date
                rect(280, 585, 410, 90)
                
    elif sc_mode == 1:
        #detail画面
        background(253, 247, 234)
        tost_im()
        image(de_im,50,70)
        
        
    elif sc_mode == 2:
        #グラフ画面
        cp = 0
        background(253, 247, 234)
        frameRate(20)
        tost_im()
        
        #線
        strokeWeight(5)
        stroke(50)
        line(220, 750, 1040, 750)
        strokeWeight(2)
        line(320,20,320,80)
        line(495,20,495,80)
        line(710,20,710,80)
        strokeWeight(5)
        stroke(144, 238, 144)
        line(350,85,470,85)
        stroke(106, 90, 205)
        line(525,85,690,85)
        stroke(184, 134, 11)
        line(10,165,110,165)
        
        #円
        strokeWeight(5)
        if sqrt(sq(mouseX - map(m_bar,0,140,220,1040))+sq(mouseY-750)) <= 20 or g_dr == 1:
            noStroke()
            fill(161,187,230)
            ellipse(map(m_bar,0,140,220,1040), 750, 45, 45)
        fill(253, 247, 234)
        stroke(50)
        ellipse(map(m_bar,0,140,220,1040), 750, 30, 30)
        
        #再生ボタン関連
        fill(161,187,230)
        noStroke()
        if mouseY>=725 and mouseY<=775:
            if mouseX>=80 and mouseX<=130:
                rect(79,725,50,50)
            elif mouseX>=140 and mouseX<=190:
                rect(139,725,50,50)
            elif mouseX>=18 and mouseX<=68:
                noFill()
                strokeWeight(8)
                stroke(161,187,230)
                ellipse(43,750,50,50)
        if g_pl == 1:
            image(st_im,20,727)
        elif g_pl == 0:
            image(pl_im,20,727)
        image(rcb_im,80,727)
        image(cb_im,140,727)
        stroke(161,187,230)
        
        #番号
        textAlign(LEFT, TOP)
        textSize(40)
        fill(0)
        text("#"+str(int(m_bar)),10,0)
    
        #順位
        if m_bar < 1:
            pass
        elif int(table[int(m_bar)+1][5]) == 1:
            fill(250, 128, 114)
            cp = 1
        elif int(table[int(m_bar)+1][5]) <= 3:
            fill(161,187,727)
        textAlign(RIGHT, TOP)
        textSize(80)
        text(table[int(m_bar)+1][5],233,0)
        image(i_im,238,10)
        
        #kill
        textAlign(RIGHT, TOP)
        textSize(80)
        fill(0)
        if m_bar < 1:
            pass
        elif int(table[int(m_bar)+1][6]) >= 5:
            fill(250, 128, 114)
        elif int(table[int(m_bar)+1][6]) >= 3:
            fill(161,187,727)
        text(table[int(m_bar)+1][6],400,0)
        fill(0)
        textSize(40)
        textAlign(LEFT,TOP)
        text("kill",410,40)
        
        #assist
        textAlign(LEFT, TOP)
        textSize(80)
        fill(0)
        if m_bar < 1:
            pass
        elif int(table[int(m_bar)+1][7]) >= 5:
            fill(250, 128, 114)
        elif int(table[int(m_bar)+1][7]) >= 3:
            fill(161,187,727)
        text(table[int(m_bar)+1][7],520,0)
        fill(0)
        textSize(40)
        text("assist",580,40)
        
        #damage
        textAlign(LEFT, TOP)
        textSize(80)
        fill(0)
        if m_bar < 1:
            pass
        elif int(table[int(m_bar)+1][8])>2000:
            fill(250, 128, 114)
        elif int(table[int(m_bar)+1][8])>1000:
            fill(161,187,727)
        text(table[int(m_bar)+1][8],730,0)
        textSize(20)
        fill(0)
        text("damage",935,60)
        
        #日時
        textAlign(LEFT, TOP)
        textSize(15)
        text(table[int(m_bar)+1][15],5,60)
        
        #RP表示
        textSize(30)
        fill(0)
        textAlign(LEFT,TOP)
        text("RANK",10,80)
        textSize(40)
        fill(0)
        text(table[int(m_bar)+1][4],10,120)
        
        #自キャラ表示
        image(mn_im,5,300)
        ch(table[int(m_bar)+1][9],40,345)
        
        #味方キャラ1
        image(m1_im,5,400)
        noStroke()
        fill(253, 247, 234)
        rect(130,400,60,60)
        ch(table[int(m_bar)+1][10],40,445)
        
        #味方キャラ2
        image(m2_im,5,500)
        noStroke()
        fill(253, 247, 234)
        rect(130,500,60,60)
        ch(table[int(m_bar)+1][11],40,545)
        
        
        #バー移動
        if g_dr == 1:
            if mouseX>=220 and mouseX<=1040:
                m_bar = map(mouseX,220,1040,0,140)
            elif mouseX<220:
                m_bar = 0
            elif mouseX>1040:
                m_bar = 140
        elif m_bar > 140:
            pass
        elif g_pl == 0:
            pass
        else:
            m_bar += 0.1
            
        
        #グラフ描画
        noStroke()
        fill(255)
        rect(170,90,880,625)
        #メモリ右描画
        for g in range(1,14):
            stroke(50)
            strokeWeight(1)
            line(1045,715-((715-90)/14)*g,1055,715-((715-90)/14)*g)
        textSize(20)
        textAlign(LEFT, CENTER)
        fill(50)
        text("5",1060,715-((715-90)/14)*5-2)
        text("10",1054,715-((715-90)/14)*10-2)
        if m_bar < 1:
            pass
        else:
            stroke(50)
            strokeWeight(2)
            for i in range(0,int(m_bar)):
                #今更新しているグラフ位置の描画
                x_now = map(m_bar-1,0,m_bar,170,1030)
                strokeWeight(1)
                stroke(50)
                if not(m_bar >= 140):
                    line(x_now,90,x_now,715)
                #更新x軸
                x = map(i,0,m_bar,170,1030)
                #キルアシグラフ
                k_y = ((715-90)/14)*(int(table[int(i)+2][6]))
                k_a = ((715-90)/14)*(int(table[int(i)+2][7]))
                fill(144, 238, 144)
                noStroke()
                if k_y >= 1:
                    rect(x,715,20 - m_bar/9,-k_y)
                fill(106, 90, 205)
                if k_a >= 1:
                    rect(x,715-k_y,20 - m_bar/9,-k_a)
                #RPグラフ
                strokeWeight(3)
                stroke(184, 134, 11)
                g_be = int(table[int(i)+1][4])
                be_X = map(i-1,-1,m_bar,170,1030)
                be_Y = map(g_be,3200,3650+16*m_bar,495,134)
                now_X = map(i,-1,m_bar,170,1030)
                now_Y = map(int(table[int(i)+2][4]),3200,3650+16*m_bar,495,134)
                line(be_X, be_Y, now_X, now_Y)
                #メモリ左描画
                for p in range(3000,6500,500):
                    y_lm = map(p,3200,3650+16*m_bar,495,134)
                    if y_lm < 100:
                        y_lm = -100 
                    stroke(184, 134, 11)
                    strokeWeight(1)
                    line(165,y_lm,175,y_lm)
                textSize(15)
                textAlign(RIGHT, CENTER)
                fill(184, 134, 11)
                text("3000",165,map(3000,3200,3650+16*m_bar,495,134)-2)
                if map(4000,3200,3650+16*m_bar,495,134)-2 > 100:
                    text("4000",165,map(4000,3200,3650+16*m_bar,495,134)-2)
                if map(5000,3200,3650+16*m_bar,495,134)-2 > 100:
                    text("5000",165,map(5000,3200,3650+16*m_bar,495,134)-2)
                if map(6000,3200,3650+16*m_bar,495,134)-2 > 100:
                    text("6000",165,map(6000,3200,3650+16*m_bar,495,134)-2)
                
    
        
        
    elif sc_mode == 3:
        #キャラ画像一覧
        #全データ画面
        background(253, 247, 234)
        tost_im()
        for i in range(17,29):
            ch(table[0][i],380+(i-17)*50,20)
        
        #ページ送り画像
        if mouseY>=720 and mouseY<=768:
            if mouseX>=439 and mouseX<=488:
                if p_3 != 1:
                    noStroke()
                    fill(161,187,230)
                    rect(439,720,49,48)
            elif mouseX>639 and mouseX<=688:
                if p_3 != 13:
                    noStroke()
                    fill(161,187,230)
                    rect(639,720,49,48)
        if p_3 != 1:
            image(rcb_im,440,720)
        if p_3 != 13:
            image(cb_im,640,720)
        textAlign(CENTER,TOP)
        textSize(60)
        fill(50)
        text(p_3,width/2 + 20,710)
        
        #表
        image(all_im, 30, 20)
        image(mn_im,  620,110)
        image(m1_im,  730,107)
        image(m2_im,  885,110)
        strokeWeight(2)
        stroke(100)
        image(i_im,158,80)
        for t in range(200,700,50):
            line(30,t,1040,t)
        stroke(50)
        strokeWeight(5)
        line(30, 100, 1040, 100)
        line(30, 700, 1040, 700)
        line(30, 150, 1040, 150)
        for c in [30,160,220,350,400,470,615,730,880,1040]:
            l_var(c)
        
        textAlign(LEFT,TOP)
        fill(50)
        textSize(40)
        text("all data", 100,20)
        text(" DATE",30,100)
        text(" RANK",220,100)
        textSize(30)
        text(" DAMAGE",470,110)
        textSize(20)
        text(" kill",352,115)
        text(" assist",402,115)
        
        
        #日付
        textAlign(LEFT, TOP)
        textSize(13)
        fill(50)
        for i in range(11):
            text(table[(p_3 - 1)*11+i+2][15],35,170 + i * 50)
        
        #順位
        textAlign(CENTER, TOP)
        textSize(30)
        for i in range(11):
            fill(50)
            if p_3 == 13 and i >= 9:
                pass
            else:
                if int(table[(p_3 - 1)*11+i+2][5]) == 1:
                    fill(250, 128, 114)
                elif int(table[(p_3 - 1)*11+i+2][5]) <= 3:
                    fill(161,187,727)
                text(table[(p_3 - 1)*11+i+2][5],190,160 + i * 50)
                
        #RANK
        textAlign(LEFT, TOP)
        textSize(30)
        fill(50)
        for i in range(11):
            text(table[(p_3 - 1)*11+i+2][4],250,160 + i * 50)
        
        #kill
        textAlign(LEFT, TOP)
        textSize(30)
        for i in range(11):
            fill(50)
            if p_3 == 13 and i >= 9:
                pass
            else:
                if int(table[(p_3 - 1)*11+i+2][6]) >= 5:
                    fill(250, 128, 114)
                elif int(table[(p_3 - 1)*11+i+2][6]) >= 3:
                    fill(161,187,727)
                text(table[(p_3 - 1)*11+i+2][6],365,160 + i * 50)
        
        #assist
        textAlign(LEFT, TOP)
        textSize(30)
        for i in range(11):
            fill(50)
            if p_3 == 13 and i >= 9:
                pass
            else:
                if int(table[(p_3 - 1)*11+i+2][7]) >= 5:
                    fill(250, 128, 114)
                elif int(table[(p_3 - 1)*11+i+2][7]) >= 3:
                    fill(161,187,727)
                text(table[(p_3 - 1)*11+i+2][7],425,160 + i * 50)
                
        #damage
        textAlign(RIGHT, TOP)
        textSize(30)
        for i in range(11):
            fill(50)
            if p_3 == 13 and i >= 9:
                pass
            else:
                if int(table[(p_3 - 1)*11+i+2][8]) >= 2000:
                    fill(250, 128, 114)
                elif int(table[(p_3 - 1)*11+i+2][8]) >= 1000:
                    fill(161,187,727)
                text(table[(p_3 - 1)*11+i+2][8],600,160 + i * 50)
        
        #自分のキャラ
        for i in range(11):
            ch(table[(p_3 - 1)*11+i+2][9],645,152 + i * 50)
        #味方1
        for i in range(11):
            ch(table[(p_3 - 1)*11+i+2][10],780,152 + i * 50)
        #味方2
        for i in range(11):
            ch(table[(p_3 - 1)*11+i+2][11],940,152 + i * 50)
        


def mousePressed():
    global sc_mode,g_pl,m_bar,g_dr,p_3
    if sc_mode >= 1:
        if mouseX>=1000 and mouseY<80:
            sc_mode = 0
    if sc_mode == 0:
        if mouseX>=280 and mouseX<=690:
                if mouseY>=385 and mouseY<=475:#detail
                    sc_mode = 1
                elif mouseY>=485 and mouseY<=575:#graph
                    sc_mode = 2
                elif mouseY>=585 and mouseY<=685:#all date
                    sc_mode = 3
    if sc_mode == 2:
        if mouseY>=725 and mouseY<775:
            if mouseX>=18 and mouseX<=68:
                if g_pl == 1:
                    g_pl = 0
                elif g_pl == 0:
                    g_pl = 1
            elif mouseX>=80 and mouseX<=130:
                g_pl = 0
                if m_bar >= 1:
                    m_bar = floor(m_bar - 1)
                elif m_bar < 1:
                    m_bar = 0
            elif mouseX>=140 and mouseX<=190:
                g_pl = 0
                if m_bar <= 139:
                    m_bar = floor(m_bar + 1)
                elif m_bar > 139:
                    m_bar = 140
        if sqrt(sq(mouseX - map(m_bar,0,140,220,1040))+sq(mouseY-750)) <= 20:
            g_dr = 1
    if sc_mode == 3:
        if mouseY>=720 and mouseY<=768:
            if mouseX>=439 and mouseX<=488:
                if p_3 != 1:
                    p_3 -= 1
            elif mouseX>639 and mouseX<=688:
                if p_3 != 13:
                    p_3 += 1
                
                

def mouseReleased():
    global g_dr
    if g_dr == 1:
        g_dr = 0    

def tost_im(): #初期画面へ
    if mouseX>=1000 and mouseY<80:
        image(ba2_im,width-70,5)
    else:
        image(ba_im,width-70,5)

def l_var(asc):#縦線表示
    stroke(50)
    strokeWeight(5)
    line(asc,100,asc,700)

def ch(name,x_c,y_c):#キャラ表示の条件分岐
    if name == "\x83u\x83\x89\x83n":
        image(br_im,x_c,y_c)
    elif name == "\x83W\x83u":
        image(zb_im,x_c,y_c)
    elif name == "\x83\x89\x83C\x83t\x83\x89":
        image(li_im,x_c,y_c)
    elif name == "\x83p\x83X":
        image(ps_im,x_c,y_c)
    elif name == "\x83\x8c\x83C\x83X":
        image(ri_im,x_c,y_c)
    elif name == "\x83o\x83\x93\x83K":
        image(bn_im,x_c,y_c)
    elif name == "\x83~\x83\x89\x83I\x83W":
        image(mr_im,x_c,y_c)
    elif name == "\x93\xc5\x83I\x83W":
        image(ko_im,x_c,y_c)
    elif name == "\x83I\x83N\x83^\x83\x93":
        image(oc_im,x_c,y_c)
    elif name == "\x83\x8f\x83b\x83g\x83\\\x83\x93":
        image(wt_im,x_c,y_c)
    elif name == "\x83N\x83\x8a\x83v\x83g":
        image(kr_im,x_c,y_c)
    elif name == "\x83\x8c\x83\x94":
        image(rv_im,x_c,y_c)
    elif name == "\x83\x8d\x81[\x83o":
        image(rb_im,x_c,y_c)
