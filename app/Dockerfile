FROM python:3.12

RUN apt-get update
RUN apt-get install -y openssh-server sshpass openssh-client git

RUN awk '{ sub(/#PermitRootLogin prohibit-password/, "PermitRootLogin yes"); } 1' /etc/ssh/sshd_config > /tmp/sshd_config \
    && mv /tmp/sshd_config /etc/ssh/sshd_config \
    && echo "root:root" | chpasswd \
    && service ssh restart

CMD ["/usr/sbin/sshd","-D"]