FROM drug_classification:ubuntu
RUN apt update && apt upgrade
RUN apt-get -y install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev
RUN mkdir home/drug_classification
COPY ./decistion_tree.png drug200.csv main.py README.md requirement.txt home/drug_classification/
RUN pip3 install -r /home/drug_classification/requirement.txt
RUN python3.10 -V
CMD ["bin/bash"]

