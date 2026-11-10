FROM ros:jazzy

#ARG USERNAME=ros2user
#ARG USER_UID=1000
#ARG USER_GID=$USER_UID

# Create the user
#RUN groupadd --gid $USER_GID $USERNAME
#RUN useradd --uid $USER_UID --gid $USER_GID -m $USERNAME

# Add sudo support
RUN apt-get -y update
RUN apt-get install -y sudo
#RUN echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME
#RUN chmod 0440 /etc/sudoers.d/$USERNAME
RUN echo "ubuntu ALL=(root) NOPASSWD:ALL" > /etc/sudoers.d/ubuntu
RUN chmod 0440 /etc/sudoers.d/ubuntu
RUN apt-get update && apt-get upgrade -y

# Install a few important dependencies
RUN apt-get install -y \
    #ament-cmake \
    ccls \
    python3-colcon-common-extensions \
    python3-pip \
    vim \
    clang \
    clang-format \
    clang-tidy \
    ros-jazzy-turtlesim \
    ros-jazzy-rqt* \
    && rm -rf /var/lib/apt/lists/*

RUN echo "source /opt/ros/jazzy/setup.bash" >> /home/ubuntu/.bashrc
ENV SHELL /bin/bash

# Workspace folder owned by ubuntu (the named volume copies this ownership)
RUN mkdir -p /home/ws/src && chown -R ubuntu:ubuntu /home/ws

# Set the default user
USER ubuntu
CMD ["/bin/bash"]
