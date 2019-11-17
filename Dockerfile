FROM Ubuntu

RUN apt update
RUN apt install python3

COPY requirements.txt /

RUN pip3 install -r requirements.txt
RUN ln -s main.py pma
RUN ln -s pma /bin/pma
