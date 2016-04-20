App Deployer
============

<!---
[![image](https://img.shields.io/pypi/v/app-deployer.svg)](https://pypi.python.org/pypi/app-deployer)
-->

[![image](https://img.shields.io/travis/noaa-nws-cpc/app-deployer.svg)](https://travis-ci.org/noaa-nws-cpc/app-deployer)

App Deployer deploys all types of applications using [Ansible](https://www.ansible.com) and [Ansistrano](https://github.com/ansistrano). It supports deploying (and rolling back) applications using the applications own `make install` target or Ansible deployment files. If your app has one of those, then it's ready to be deployed. What *is* needed is an inventory of apps that you want to be able to deploy with App Deployer.

When you have an inventory of apps, you can deploy any app like this:

    deploy [OPTIONS] <app-name>

You can rollback any release like this:

    rollback [OPTIONS] <app-name>

Install
-------

### Ansible

First you'll need Ansible. At the current date Ansible only supports Python 2. So you should create a Python 2 virtual environment with either [virtualenv](https://virtualenv.pypa.io/en/latest):

    virtualenv -p /usr/bin/python2.7 ansible-env

You can also use [Anaconda](https://www.continuum.io) to create a virtual environment:

    conda create -n ansible-env python=2.7

Note that in this example we're calling the new environment `ansible-env`, but you can call yours anything.

Now you can enter your new virtualenv environment:

    source ansible-env/bin/activate

or Anaconda environment:

    source activate ansible-env

Refer to their [installation instructions](http://docs.ansible.com/ansible/intro_installation.html) for details, but you can install Ansible simply using pip:

    pip install ansible

### Ansible Galaxy roles

[Ansible Galaxy](https://galaxy.ansible.com) is an online repository of Ansible roles. You don't need to know what these are to use App Deployer, but you'll have to install a few Ansible Galaxy roles in order to use it. If you have `sudo` privileges you can do it right away. Assuming you're in your new virtual environment from above:

    sudo ansible-galaxy install carlosbuenosvinos.ansistrano-deploy carlosbuenosvinos.ansistrano-rollback noaa-nws-cpc.miniconda

If you don't have `sudo` privileges, you can use a [config file](http://docs.ansible.com/ansible/intro_configuration.html) to tell Ansible where to install Galaxy roles (by default it's `/etc/ansible/roles`, requiring `sudo`), and specify a directory you have write permissions to. Then install the roles:

    ansible-galaxy install carlosbuenosvinos.ansistrano-deploy carlosbuenosvinos.ansistrano-rollback noaa-nws-cpc.miniconda

### App Deployer

Now you should be able to install App Deployer. Clone the repository:

    git clone https://github.com/noaa-nws-cpc/app-deployer.git

And install it:

    make install
