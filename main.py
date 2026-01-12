import streamlit as st
import pandas as pd
from numpy.random import default_rng as rng

st.title("Car Sales Data Analysis")


with st.sidebar:
     st.header("About App")
     st.write("This App is for Data Analysis")

st.header("_Streamlit_ is :blue[cool] :sunglasses:")
st.header("This is a header with a divider", divider="gray")
st.header("These headers have rotating dividers", divider=True)
st.header("One", divider=True)
st.header("Two", divider=True)
st.header("Three", divider=True)
st.header("Four", divider=True)

print("####################################")

st.markdown("*Streamlit* is **really** ***cool***.")
st.markdown('''
    :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
    :gray[pretty] :rainbow[colors] and :blue-background[highlight] text.''')
st.markdown("Here's a bouquet &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

multi = '''If you end a line with two spaces,
a soft return is used for the next line.

Two (or more) newline characters in a row will result in a hard return.
'''
st.markdown(multi)


print("########################################")


x=st.slider("Choose an x value", 1, 10)
st.write("The value of :blue[***x***] is", x)


print("#########################")

st.subheader("st.column demo")

col1, col2=st.columns(2)

with col1: 
     z=st.slider("Choose an z value", 1, 10)

with col2:
    st.write("The value of :blue[***z***] is", z)



print("##############################")

st.subheader(" Area Chart Demo")

import pandas as pd
import streamlit as st
from numpy.random import default_rng as rng

df = pd.DataFrame(rng(0).standard_normal((20, 3)), columns=["a", "b", "c"])

st.area_chart(df)