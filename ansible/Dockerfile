FROM alpine:3.11

RUN apk add --no-cache openssh-client openssh-server ansible sshpass
RUN mkdir -p /root/.ssh
RUN echo "HOST *" > /root/.ssh/config && echo "StrictHostKeyChecking no" >> /root/.ssh/config

COPY . .

CMD [""]