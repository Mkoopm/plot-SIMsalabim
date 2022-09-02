import streamlit as st
import os
import time
from subprocess import run

dev_par_init = []
with open('SimSS/device_parameters_backup.txt') as fp:
    for line in fp:
        dev_par_init.append(line)

dev_par_init = ''.join(dev_par_init)

dev_par_text = st.text_area(
    'These are the device parameters for SIMsalabim, change them as you like',
    value=dev_par_init,
    height=600,
)
with open('SimSS/device_parameters.txt', 'w') as fp:
    fp.write(dev_par_text)

with st.spinner('SIMulating...'):
    result = run('./simss', cwd='SimSS')

if result.returncode != 0:
    st.error('SIMsalabim raised an error')
#st.success('Done!')