FROM amazonlinux
MAINTAINER Yuvaraj
RUN yum install wget -y
RUN yum install tar -y
RUN yum install xz -y
RUN yum intall telnet -y
RUN wget https://nodejs.org/dist/v16.18.0/node-v16.18.0-linux-x64.tar.xz
RUN tar -xvf node-v16.18.0-linux-x64.tar.xz
ENV PATH $PATH:/node-v16.18.0-linux-x64/bin
RUN mkdir /opt/dist
RUN mkdir /opt/node_modules
COPY ./dist/ /opt/dist
COPY ./node_modules /opt/node_modules
COPY ./index.js /opt/
COPY ./package.json /opt/
WORKDIR /opt
EXPOSE 3000
CMD ["npm", "start"]