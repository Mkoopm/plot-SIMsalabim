# Slim version of Python
FROM python:3.10.0a7-slim-buster

# Download Package Information
RUN apt-get update -y

# Install Tkinter
RUN apt-get install tk -y

RUN git clone git@github.com:Mkoopm/plot-SIMsalabim.git
RUN git clone git@github.com:kostergroup/SIMsalabim.git

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt


# Commands to run Tkinter application
CMD ["steamlit", "run", "app.py"]
ENTRYPOINT ["python3"]