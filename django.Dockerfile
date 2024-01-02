FROM debian:latest

ARG UID 1000
ARG GID 1000

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

RUN apt-get update --fix-missing && apt-get install -y wget bzip2 ca-certificates \
    libglib2.0-0 libxext6 libsm6 libxrender1 \
    git mercurial subversion && apt-get clean

RUN groupadd -g ${UID} jupyter
RUN useradd jupyter -m -u ${UID} -g ${GID}

USER jupyter
ENV PATH ~/anaconda3/bin:$PATH
RUN wget https://repo.anaconda.com/archive/Anaconda3-2023.03-1-Linux-x86_64.sh -O ~/anaconda.sh
RUN /bin/bash ~/anaconda.sh -b # -p ~/anaconda3/
RUN rm ~/anaconda.sh
RUN /bin/bash ~/anaconda3/etc/profile.d/conda.sh init
RUN /bin/bash ~/anaconda3/etc/profile.d/conda.sh conda -n base -c defaults conda
RUN /bin/bash ~/anaconda3/etc/profile.d/conda.sh create --name py3.9 python=3.9
RUN echo ". ~/anaconda3/etc/profile.d/conda.sh" >> ~/.bashrc
RUN echo "conda activate py3.9" >> ~/.bashrc
RUN echo "export PATH=~/anaconda3/bin/:~/anaconda3/condabin/:${PATH}" >> ~/.bashrc

USER root
RUN apt-get update --fix-missing && apt-get install -y sudo && apt-get clean
RUN adduser jupyter sudo
RUN passwd -d jupyter
RUN echo "jupyter ALL=(ALL)  ALL" > /etc/sudoers

USER jupyter
ENV PATH ~/anaconda3/bin:$PATH
COPY ./requirements.txt .
#RUN pip install -r ./requirements.txt
#RUN python -m pip install -r ./requirements.txt
RUN ~/anaconda3/bin/python -m pip install -r ./requirements.txt

COPY ./boot.sh .
ENTRYPOINT /bin/bash ./boot.sh
CMD [ "/bin/bash" ]
