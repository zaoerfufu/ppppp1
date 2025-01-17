'''我的主页'''
import streamlit as st
from PIL import Image
page = st.sidebar.radio('我的首页', ['我的兴趣推荐', '我的图片处理工具', '我的智能词典', '我的留言区', '久幺视频网'])

def page_1():
    '''我的兴趣推荐'''
    st.markdown("欢迎来到我的主页")
    st.write("------------------------------------")
    st.text("空")
    st.write("--------------------------------------")
    s = st.slider('一键打分：', 0, 10, 1)
    st.write("当前分值：", s)
    with open("st.txt", 'r', encoding='utf-8') as f:
        sl = f.read().split("\n")
    su = 0
    for i in sl:
        su  += int(i)
    av = su/len(sl)
    a = str(av).split(".")
    b = int(a[1][0])
    if b <= 4:
        a[1] = a[1][0:1]
    else:
        a[1] = str(int(a[1][0:1])+1)
    av = a[0] + "." + a[1] + "\n"
    st.write("平均分值：", av)
    if st.button("打分"):
        sl.append(str(s))
        with open("st.txt", "w", encoding="utf-8") as f:
            ss = ""
            for i in sl:
                ss += i + "\n"
            ss = ss[:-1]
            f.write(ss)
    
    st.image("水池.png")

def img_change_1(img1, cr, cg, cb, c):
    '''图片处理'''
    w1, h1 = img1.size
    img_array = img1.load()
    for x in range(w1):
        for y in range(h1):
            R = img_array[x, y][cr]
            G = img_array[x, y][cg]
            B = img_array[x, y][cb]
            img_array[x, y] = (R+c, G+c, B+c)
    return img1
    
def page_2():
    '''我的图片处理工具'''
    st.write(":sunglasses:图片换色小程序:sunglasses:")
    uploaded_file_1 = st.file_uploader("上传图片", type=["png", "jpg", "jpeg"])
    if uploaded_file_1:
        file_size = uploaded_file_1.size
        img1 = Image.open(uploaded_file_1)
        tab1, tab2, tab3, tab4=st.tabs(['原图', '换色', '变暗', '变亮'])
        with tab1:
            st.image(img1)
        with tab2:
            st.image(img_change_1(img1, 0, 2, 1, 0)) 
        with tab3:
            st.image(img_change_1(img1, 0, 1, 2, -50))
        with tab4:
            st.image(img_change_1(img1, 0, 1, 2, 150))

def page_3():
    '''我的智能词典'''
    st.write("飞舞词典")
    with open("words_space.txt", 'r', encoding='utf-8') as f:
        words_list = f.read().split('\n')
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split('#')
        #print(words_list[i])
    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [(int(i[0]), i[2])]
    with open('ct.txt', 'r', encoding='utf-8') as f:
        times_list = f.read().split("\n")
    for i in range(len(times_list)):
        times_list[i] = times_list[i].split("#")
    times_dict = {}
    for i in times_list:
        times_dict = {}
    #print(times_dict)
    word = st.text_input('请输入要查询的单词（禁止输入任何非英文字符）：')
    if word in words_dict:
        st.write(words_dict[word])
        n = words_dict[word][0]
        if n in times_dict:
            times_dict[n] += 1
        else:
            times_dict[n] = 1
        with open('ct.txt', 'w', encoding='utf-8') as f:
            message = ''
            for k, v in times_dict.items():
                message  += str(k) + "#" + str(v) + '\n'
            message = message[:-1]
            f.write(message)
        st.write('查询次数:',times_dict[n])

        if word == 'python':
            st.code('''print("hello world!)''')
        elif word == 'snow': 
            st.snow()
        elif word == 'congratulate':
            st.markdown(':red[恭]:orange[喜]<span style="color:GoldenRod">你</span><span style="color:#FFAA00">啊，</span>:red[被]:orange[我]:red[恭]:orange[喜]:red[到]:orange[了]', unsafe_allow_html = True)

def page_4():
    '''我的留言区'''
    st.write(":-1:β留言区:-1:")
    with open('leave_messages.txt', 'r', encoding='utf-8') as f:
        messages_list = f.read().split("\n")
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split('#')
    for i in messages_list:
        if i[1] == '那艺娜':
            with st.chat_message('🌞'):
                st.write(i[1], ':', i[2])
        elif i[1] == '张兵':
            with st.chat_message('🍥'):
                st.write(i[1], ':', i[2])
    name = st.selectbox('我是',['那艺娜', '张兵'])
    new_message = st.text_input('想要留言的内容')
    if st.button('砰'):
        messages_list.append([str(int(messages_list[-1][0])+1), name, new_message])
        with open('leave_messages.txt', 'w', encoding='utf-8') as f:
            messages = ""
            for i in messages_list:
                messages += i[0] + '#' + i[1] + '#' + i[2] + "\n"
            messages = messages[:-1]
            f.write(messages)
    st.image("nyn.png")
                
def page_5():
    st.markdown("<span style='color:cyan'>想啥呢</span>:-1:", unsafe_allow_html = True)
    st.link_button('久幺视频', 'https://www.bilibili.com/video/BV1Pv4y1z7A1/?share_source=copy_web')
if page == '我的兴趣推荐':
    page_1()
elif page == '我的图片处理工具':
    page_2()
elif page == '我的智能词典':
    page_3()
elif page == '我的留言区':
    page_4()
elif page == '久幺视频网':
    page_5()
