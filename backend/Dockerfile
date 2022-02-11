FROM python:3.9-slim-bullseye

RUN pip3 install --upgrade pip
RUN apt-get update
RUN apt-get install -y dnsutils 

# create app folder
RUN mkdir -p /app

# copy requirements file
COPY ./app/requirements.txt /app/requirements.txt

# set the working directory
WORKDIR /app

# install requirements from requirements file
RUN pip3 install -r ./requirements.txt

# copy remaining app files
COPY ./app /app
RUN mkdir /app/log /app/data /app/data/logs /app/data/media /app/data/profile

# # create group and user
# RUN groupadd -r pyuser && useradd -g pyuser pyuser

# # set ownership and permissions
# RUN chown -R pyuser:pyuser /app

# # switch to user pyuser
# USER pyuser

# expose container port
EXPOSE 5000

# start application with specified user
ENTRYPOINT [ "python" ]
CMD [ "-u", "server.py" ] 