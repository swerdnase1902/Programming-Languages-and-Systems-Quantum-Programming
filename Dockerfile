FROM ubuntu:latest

RUN apt-get update && DEBIAN_FRONTEND="noninteractive" apt-get install -y aria2 openssh-server xrdp xfce4 xfce4-power-manager xfce4-terminal sudo && apt-get clean
RUN mkdir /var/run/sshd
RUN adduser --disabled-password --gecos '' vagrant
RUN adduser vagrant sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
RUN chown -R vagrant /home/vagrant
RUN echo 'vagrant:vagrant' | chpasswd
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN echo "xfce4-session" > /home/vagrant/.xsession

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile
RUN cd /home/vagrant && aria2c -q "https://download.jetbrains.com/product?code=PC&latest&distribution=linux" && tar xf *.tar.gz && rm *.tar.gz
RUN cd /home/vagrant && aria2c -q "https://go.microsoft.com/fwlink/?LinkID=760868" && DEBIAN_FRONTEND="noninteractive" apt install ./*.deb && rm *.deb

# Maple
RUN apt-get update && DEBIAN_FRONTEND="noninteractive" apt-get install -y lsb python3 python3-pip && apt-get clean
RUN python3 -m pip install gdown
RUN cd /home/vagrant && gdown https://drive.google.com/uc?id=1SenEe57qei5AmOMwnqpBduWCEmCUAuTt && tar xf *tgz && rm *tgz && mv Maplesoft* mapleinstall
COPY installer.properties '/home/vagrant/mapleinstall/'
RUN cd /home/vagrant/mapleinstall/ && chmod +x  ./Maple2019.0LinuxX64Installer_Downloadly.ir.run && ./Maple2019.0LinuxX64Installer_Downloadly.ir.run --mode unattended --optionfile installer.properties

EXPOSE 22
EXPOSE 3389
CMD ["/usr/sbin/sshd", "-D"]
