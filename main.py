import streamlit as st
import time

st.title('Streamlit 超入門')

st.write('プログレスバーの表示')
'Start!!'

latest_interation = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_interation.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!!!!!'


left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')


expander = st.expander('問い合せ1')
expander.write('問い合わせ内容を書く')
expander = st.expander('問い合せ2')
expander.write('問い合わせ内容を書く')
expander = st.expander('問い合せ3')
expander.write('問い合わせ内容を書く')



# text = st.sidebar.text_input('あなたの趣味を教えてください。')
# condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)

# 'あなたの趣味:', text, ''
# 'コンディション:', condition, ''

# if st.checkbox('Show Image'):
#     img = Image.open('sample.png')
#     st.image(img, caption='Conan', use_column_width=True)

# df = pd.DataFrame(
#     np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
#     columns = ['lat', 'lon']
# )

# st.map(df)
# st.write(df)
# st.table(df.style.highlight_max(axis=0))
