FROM python:3.8-slim-buster
RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y python-pip
RUN apt-get install -y texlive-latex-extra
RUN pip3 install matplotlib~=3.5.1
RUN pip3 install networkx~=2.6.3
RUN pip3 install megaserg01-astBuilder==1.6
RUN pip3 install pdflatex~=0.1.3
COPY . .
CMD echo "start" && python3 mediumTask.py && cd artifacts && bash