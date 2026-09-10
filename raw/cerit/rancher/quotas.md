#

Our container platform uses resource quotas on *Projects* and *Namespaces*. Quota is limitation on how much resources can user or group of users utilize. Kubernetes use two kinds of resource quotas: *requests* and *limits*. See [kubernetes documentation](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/) for more information about this concept. Currently applied quotas are on *CPU* and *Memory* resources. These quotas are set on both *Project* and *Namespace*.

*Personal* Project and default *Namespace* has 20 CPUs *request*, 32 CPUs *limit*, 40GB Memory *requests*, and 64GB Memory *limits*. Other types of quotas are not set. User can request a new project with significantly larger quotas at [IT Service desk](mailto:k8s@ics.muni.cz).

## [Namespaces](#namespaces)

Without requesting explicit project, user is given a *Personal* project with limits mentioned above. Together with the *Personal* project, default *Namespace* is created. Both the *Personal* project and the default *Namespace* have the mentioned quotas. The default *Namespace* is set to the exact quota as the *Personal* project which means that **any new** *Namespace* is out of available quotas. It is not possible to extend *Personal* project quotas so two options are here:

- Request explicit project.

- Decrease quotas for the default *Namespaces* and give spare resources to a new *Namespace*.

### [Changing Namespace Quotas](#changing-namespace-quotas)

To change resource quotas for existing namespace, navigate through `Cluster` (1), `Projects/Namespaces` (2), select the `Namespace` (3) context menu and `Edit Config`.

![quotaedit1](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fquotaedit1.3yzxjkwhhnwyg.png&w=3840&q=75)

Then you can change `Resource Quotas` for the *Namespace* as desired and `Save` them.

![quotaedit2](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fquotaedit2.39hsrejuskszc.png&w=3840&q=75)

### [Creating New Namespaces](#creating-new-namespaces)

To make things work properly, do not create a *Namespace* using `kubectl` or `helm` or any other tools. It is possible but you will not see this *Namespace* in Rancher UI. Instead, use the Rancher UI to create the *Namespace*. Most tools like `helm`, `kustomize` should deal with already existing *Namespaces* just fine.

-

Firstly, in a project where you want to create new namespace, lower namespace resource quotas of some of the existing namespaces so you create space for new namespace. Perform this according to the previous section.

-

Create a new namespace in the project via UI button and set some resource quotas.

![create-ns](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fcreate-ns.0l9r-4_ymbva-.png&w=3840&q=75)

- Create the following role binding in the new namespace. New namespaces are forbidden to perform any action so to ensure you can deploy objects, this role binding is necessary. You can create rolebinding via UI or using kubectl.

YAML rolebinding:

rolebinding.yaml

```
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: [new_namespace_name]-sa-rb
  namespace: [new_namespace_name]
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: grant-namespace-permissions
subjects:
- kind: ServiceAccount
  name: default
  namespace: [new_namespace_name]

```

Kubectl: Change `[new_namespace_name]` for the actual name of your new namespace, save it as e.g. `rolebinding.yaml`, and deploy via `kubectl create -f rolebinding.yaml`

UI: Navigate according to the image and import the same YAML as above, changing `[new_namespace_name]` for the actual name of your new namespace.

![rolebinding](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Frolebinding.3dcdxy8v6zh1r.png&w=3840&q=75)

## [Resource Limits](#resource-limits)

If running container exceeds limits, result depends on resource type. If resource is CPU, container continues to run only the CPU is limited, i.e., it runs slower. If resource is Memory or ephemeral-storage, container is *evicted*, it can be restarted in case of *Deployment* but resource is not extended automatically, so eviction is likely to happen again.

## [Consequences](#consequences)

- Every Pod, Job, Deployment, and any other kind that runs a container needs *resources* attribute to be set otherwise deploy is rejected with similar error:

```
Pods "master-685f855ff-gg9sr" is forbidden: failed quota: default-w2qv7: must specify limits.cpu,limits.memory,requests.cpu,requests.memory:Deployment does not have minimum availability.

```

However, this should not happen for user as we set default container resources to 1 CPU and 512MB Memory for both *requests* and *limits*. This default is applied only in the case that user did not specify resources.

-

Quotas cannot be overbooked, so sum of quotas for all namespaces within a project must not be larger than the project quota. As we set initial *namespace* quota to be equal to *Project*, there is no room for additional namespaces. Users can create additional namespace but they need to decrease quotas on initial *namespace* first or request extending *project* quotas.

-

If users deploy more containers than quota allows, *Pods* are rejected immediately, *Jobs* and other types of deployment are pending until there are free resources within the quota.

-

Setting quotas on GPU resource is currently not possible.

![publicity banner](/_next/static/media/einfra_cerit-zapati.04hjcx2t12mah.svg)

### On this page
[Namespaces](#namespaces)[Changing Namespace Quotas](#changing-namespace-quotas)[Creating New Namespaces](#creating-new-namespaces)[Resource Limits](#resource-limits)[Consequences](#consequences)

![einfra banner](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fheader03.0ikyctvi6x5ki.png&w=384&q=75)
