#

In Kubernetes, [namespaces](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/) isolate groups of resources within a single cluster. Resource names must be unique within a namespace, but not across namespaces.

Namespace names must be unique within a cluster. Avoid creating namespaces called *test* or similar generic names.

When a user logs into the Rancher GUI for the first time, a *Personal Project* and a *Namespace* are created automatically. If you do not see them, reload the web page.

You can view your namespaces in the Rancher GUI under the `Project/Namespaces` tab in the left sidebar.

![Namespace view in Rancher GUI](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fns.1r8co2itcd96k.jpg&w=3840&q=75)

You can create additional namespaces either with kubectl or in the Rancher GUI. However, creating namespaces with kubectl is not recommended because these namespaces are not linked to the user’s *Project*. Instead, create a namespace in the Rancher GUI’s Namespace overview page by clicking the `Create Namespace` button.

![publicity banner](/_next/static/media/einfra_cerit-zapati.04hjcx2t12mah.svg)

### On this page
No Headings

![einfra banner](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fheader03.0ikyctvi6x5ki.png&w=384&q=75)
