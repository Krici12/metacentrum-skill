#

`kubectl` is a powerful tool for interacting with Kubernetes clusters. For installation, see the [official documentation](https://kubernetes.io/docs/tasks/tools/#kubectl). Once installed, kubectl requires a `kubeconfig` file to function. You can download this file from the cluster overview dashboard (click on the cluster name in the upper left dropdown menu).

![kube config](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fconfig.4144v-pmckk83.jpg&w=3840&q=75)

Copy the downloaded file’s contents into `$HOME/.kube/config`, then set the file permissions to 700:

```
chmod 700 $HOME/.kube/config

```

If the file `$HOME/.kube/config` does not exist, create it before copying the contents.

You can store multiple cluster configurations in a single config file.

![publicity banner](/_next/static/media/einfra_cerit-zapati.04hjcx2t12mah.svg)

### On this page
No Headings

![einfra banner](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fheader03.0ikyctvi6x5ki.png&w=384&q=75)
