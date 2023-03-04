import streamlit as st
st.balloons()
st.snow()
st.title('Giải phương trình bậc nhất')
a = st.number_input('Tham số a' )
b = st.number_input('Tham số b')
if st.button('Giải'):
  if(a==0 and b != 0) : 
    st.write("Không có x nào là nghiệm")
  else : 
    if(a==0 and b==0) :
     st.write("Có vô số x thỏa là nghiệm")
    else : 
      st.write("Phương trình có nghiệm là",-b/a)