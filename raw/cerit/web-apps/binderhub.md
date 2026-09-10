#

BinderHub is a Binder instance running on Kubernetes at [binderhub.cloud.e-infra.cz](https://binderhub.cloud.e-infra.cz/). Binder turns a git repository into a collection of interactive notebooks. It is enough to fill in the git repository name (optionally specific notebook or branch) and binderhub will turn it into a web notebook.

## [Authentication](#authentication)

To use CERIT-SC BinderHub instance you need to authenticate. Authentication is done via SSO federated login.

## [Persistence](#persistence)

After the notebook is created, a persistent volume is mounted to the path `/home/{username}-nfs-pvc`. The same persistent volume will be mounted to that path in each notebook you spawn. So if you want to use data generated in BinderHub instance *A* in BinderHub instance *B*, you can write the data to path `/home/{username}-nfs-pvc` and it will be available for use.

Note: Be careful with paths used in notebooks. Imagine you have two BinderHubs running. In both you write output to the `/home/{username}-nfs-pvc/test` location. If both notebooks create a file named `result.txt`, you would overwrite the file. It is a good practice to create a new directory in the path `/home/{username}-nfs-pvc` for each BinderHub instance.

## [Resources](#resources)

Each user on your JupyterHub can use a certain amount of memory and CPU. You are guaranteed **1G of RAM** and **1 CPU** and you can use up to **16G of RAM** and **8 CPU**. Resource limits are a hard limit on the available resources.

### [Custom resources](#custom-resources)

If you need to specify other resource amounts or attach GPU, you can create a *.resources* file in the root of git repository. The file can look like:

```
# This file is for resource requests in CERIT-SC
# Do not change
gpu=1
cpur=2
cpul=4
memr=1
meml=4

```

Lines starting with `#` are ignored (useful for commens); other stand for:

- `gpu=[number_of_gpu_request]`

- `cpur=[number_of_cpu_request]`

- `cpul=[number_of_cpu_limit]`

- `memr=[GB_of_RAM_request]`

- `meml=[GB_of_RAM_limit]`

RAM is assigned in *GB*, do not specify any units. By default, no GPU is assigned. If the *.resources* file does not contain any of the lines, defaults are used. Similarly, if the file specifies only some lines, the defaults for the missing lines are used.

The setting currently works for repositories hosted on `github.com`. If you use another git service (gitlab, zenodo, …), please contact us at [IT Service desk](mailto:k8s@ics.muni.cz).

## [SSH keys inside the instance](#ssh-keys-inside-the-instance)

For more flexibility, we generate an SSH key pair for everyone who spawns at least one Jupyter notebook via BinderHub. This SSH keypair is mounted on the notebook instance (`/home/jovyan/.ssh/ssh.priv` and `/home/jovyan/.ssh/ssh.pub`) and can be used to import public key to GitHub account. This way you can update and work with your Git repositories directly from your notebook.

The same SSH key pair is mounted on all your BinderHub notebooks.

## [Where to find running notebooks](#where-to-find-running-notebooks)

You can find your running notebooks at `https://bhub.cloud.e-infra.cz/`. Clicking on the address will redirect you to the notebook instance. Because redirection links contain random strings, it is recommended to use a browser that can store cookies and does not require you to remember long notebook addresses. Also, avoid incognito windows because the session cookie won’t be saved and when you close the tab, you won’t find the instance in Control Panel.

## [Limits](#limits)

Currently, each user is limited to spawning 5 projects. If you reach the quota and try to deploy a new instance, an error will appear below the loading bar of the BinderHub index page.

![projects_limit](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Flimit.2niisoy60591s.png&w=3840&q=75)

To spawn a new instance, you need to delete one of your running instances. This can be done in the JupyterHub control panel (JupyterHub is used under BinderHub). Navigate to `https://bhub.cloud.e-infra.cz/` and stop any instance you don’t need. If you see a red `Delete` button, click it. After that you should be able to spawn a new instance at [binderhub.cloud.e-infra.cz](https://binderhub.cloud.e-infra.cz/).

![projects_panel](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fhubpanel.2bs3vhgbxiwxt.png&w=3840&q=75)

![projects_stop](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fstop.2fj8mknj57-gu.png&w=3840&q=75)

![projects_delete](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fdelete.0ovz21j62uyd2.png&w=3840&q=75)

❗️Notebooks are automatically deleted after one week of inactivity (inactivity = idle kernel or no connection to notebook).❗️

## [Customizations](#customizations)

### [Custom Dockerfile](#custom-dockerfile)

The Hub spawns notebook instances with a default image that does not contain any special libraries. However, you can create a custom `Dockerfile` with all dependencies that will be used as the base image. The `Dockerfile` must be located in the repository you want to launch in Binder.

When creating the `Dockerfile` keep in mind that it must be executable as *user*. It is also important to `chown` all directories used to user, e.g. :

```
RUN chown -R 1000:1000 /work /home/jovyan

```

### [Installing Miscellaneous Libraries and Software](#installing-miscellaneous-libraries-and-software)

Creating a custom dockerfile might be overkill for your needs, so there are several other ways to install e.g. the `conda' environment, `Python’ packages or some `Debian’ packages (e.g. vim).

See [all possible file types](https://repo2docker.readthedocs.io/en/latest/config_files.html) for a full description and intended use that can be included in the repository. These files will be resolved at startup. You can include multiple files in the repo, so if you need to install `Python` packages as well as some `Debian` packages, both `apt.txt` and `requirements.txt` may be present.

Short list of files:

- `environment.yml` - conda env, [example](https://github.com/binder-examples/python-conda_pip/tree/3b7126f39253f92bb13ce7ea155fd8a121082afe)

- pipfile` - Python env, [example](https://github.com/binder-examples/pipfile)

- setup.py` - Python packages, [example](https://github.com/binder-examples/setup.py)

- requirements.txt` - Python packages, [example](https://github.com/binder-examples/requirements)

- `project.toml` - Julia environment, [example](https://github.com/binder-examples/demo-julia)

- `apt.txt` - Debian packages, [example](https://github.com/binder-examples/apt_install)

- install.R` - R packages, [example](https://github.com/binder-examples/r)

See [binder examples repository](https://github.com/orgs/binder-examples/repositories?page=1&type=all) for many types of repositories, file combinations and interesting uses.

## [Unknown Error During Spawning](#unknown-error-during-spawning)

If you encounter an unknown error while spawning a notebook (or if your notebook does not spawn at all), please send an email to [IT Service Desk](mailto:k8s@ics.muni.cz).

![publicity banner](/_next/static/media/einfra_cerit-zapati.04hjcx2t12mah.svg)

### On this page
[Authentication](#authentication)[Persistence](#persistence)[Resources](#resources)[Custom resources](#custom-resources)[SSH keys inside the instance](#ssh-keys-inside-the-instance)[Where to find running notebooks](#where-to-find-running-notebooks)[Limits](#limits)[Customizations](#customizations)[Custom Dockerfile](#custom-dockerfile)[Installing Miscellaneous Libraries and Software](#installing-miscellaneous-libraries-and-software)[Unknown Error During Spawning](#unknown-error-during-spawning)

![einfra banner](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fheader03.0ikyctvi6x5ki.png&w=384&q=75)
