# base image
FROM python:3.7.11-stretch

# making directory of app
WORKDIR /usr/src/app

# OS Update
RUN apt-get update --allow-unauthenticated -y

# copy over requirements
 COPY requirements.txt ./requirements.txt

# install pip then packages
RUN pip install -r requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# exposing default port for streamlit
EXPOSE 8501

# copying all files over
 COPY user_number.py user_number.py

# streamlit-specific commands for config
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8echo 

RUN mkdir -p /.streamlit
RUN chmod 777 /.streamlit

RUN bash -c 'echo -e "\
[general]\n\
email = \"\"\n\
" > /.streamlit/credentials.toml'

RUN bash -c 'echo -e "\
[server]\n\
enableCORS = false\n\
enableXsrfProtection = false\n\
enableWebsocketCompression = false\n\
" > /.streamlit/config.toml'

EXPOSE 8501

# cmd to launch app when container is run
ENTRYPOINT ["streamlit", "run"]

 CMD ["user_number.py"]
