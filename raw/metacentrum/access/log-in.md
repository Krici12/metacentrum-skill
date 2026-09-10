#

## [Frontend login](#frontend-login)

Users connect to the MetaCentrum system via the `SSH` protocol using any of the login nodes, which are referred to as ****[frontend servers](https://docs.metacentrum.cz/en/docs/computing/infrastructure/frontends). Like most computing and data centres, MetaCentrum’s compute nodes run exclusively on Linux (OS Debian).

Warning

Frontend servers are virtual machines with very limited computational power. They are primarily used for basic data inspection and manipulation, preparing shell scripts for batch jobs and very short compilations. Do not use them for long or demanding calculations. Use an [interactive](https://docs.metacentrum.cz/en/docs/computing/run-basic-job#interactive-job) or regular [batch](https://docs.metacentrum.cz/en/docs/computing/run-basic-job#batch-job) job instead.

![Grid overall scheme](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fgrid-overall-scheme_border.1qxwauemrkuig.jpg&w=3840&q=75)

In Linux, macOS, Windows PowerShell and MobaXterm, the `ssh` command can be given in the terminal.

Open the terminal and on the CLI type

```
ssh your_username@frontend

```

If you log in for the first time, you will be prompted by a query similar to the following:

```
The authenticity of host 'skirit.ics.muni.cz (2001:718:ff01:1:216:3eff:fe20:382)' can't be
established. ECDSA key fingerprint is SHA256:Splg9bGTNCeVSLE0E4tB30pcLS80sWuv0ezHrH1p0xE.
Are you sure you want to continue connecting (yes/no)?

```

Type “yes”. The public key of the frontend will be saved to your `~/.ssh/known_hosts` file.

💡
Tip

Strictly speaking, the user should always verify a new key before adding it to a list of known hosts. For a howto on SSH key verification, see [more detailed page on SSH key verification](../access/security/connect-auth).

Once the terminal connection to a frontend is open, you can start using it with the Linux command line tools (bash shell).

A complete list of frontends is given below. You can use any of them. We encourage users to pick one that is closest to their physical location (city) to minimise network lag.

💡
Tip

In case your favourite frontend is down or going just too slow, do not hesitate to use another one.

| Frontend address |Aliased as |Native home |OS |Physically located in |Note |
| charon.nti.tul.cz |charon.metacentrum.cz |/storage/liberec3-tul |Debian 12 |Liberec | |
| elmo.elixir-czech.cz |elmo.metacentrum.cz |/storage/praha5-elixir |Debian 12 |Praha |[Elixir users](https://docs.metacentrum.cz/en/docs/access/elixir) |
| nympha.meta.zcu.cz |nympha.metacentrum.cz, nympha.zcu.cz, minos.zcu.cz, minos.meta.zcu.cz, alfrid.meta.zcu.cz |/storage/plzen1 |Debian 12 |Plzen | |
| metafzu.fzu.cz |metafzu.metacentrum.cz |/storage/praha1 |Debian 12 |Praha |dedicated for FZU users |
| oven.metacentrum.cz | |/storage/brno2 |Debian 12 |Brno |[oven node](https://docs.metacentrum.cz/en/docs/computing/infrastructure/specific-nodes#oven-node) only |
| perian.grid.cesnet.cz |perian.metacentrum.cz, onyx.metacentrum.cz |/storage/brno2 |Debian 12 |Brno | |
| skirit.grid.cesnet.cz |skirit.metacentrum.cz |/storage/brno2 |Debian 12 |Brno | |
| skirit-lite.ics.muni.cz |skirit-lite.metacentrum.cz |/storage/brno2 |Debian 12 |Brno |for quick job management, script editing, or checking job status |
| tarkil.grid.cesnet.cz |tarkil.metacentrum.cz |/storage/praha1 |Debian 12 |Praha | |
| tilia.ibot.cas.cz |tilia.metacentrum.cz |/storage/pruhonice1-ibot |Debian 12 |Pruhonice | |
| zenith.cerit-sc.cz |zenith.metacentrum.cz |/storage/brno12-cerit |Debian 12 |Brno | |

Warning

The frontend nodes can be used for light pre- and postprocessing and manipulation of data. All other tasks must be submitted as jobs to the batch job system. If you need to run something interactively, submit an interactive job.

## [Web services login](#web-services-login)

Some web services require user authentication. While, for example, in [OnDemand service](../graphical/ondemand) users use their MetaCentrum login and password, other services login is done through the user’s institution identity.

For example, let’s say you are a ČZU user wanting to log in to see [a list of queues in MetaVO pages](https://my.metacentrum.cz/queues/).

In this case, choose the “ČZU” tab from the list and fill in ČZU credentials, not MetaCentrum login and username.

![Web login](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Flogin_web_001.2g7uey0s0m9l-.png&w=3840&q=75)
![Web login](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Flogin_web_002.3uguzfs80v35t.png&w=3840&q=75)

## [Kerberos](#kerberos)

After the user enters the MetaCentrum infrastructure by logging in, they will also need to be able to move between computational nodes, reach storage spaces residing on different machines, etc. It would be very inconvenient to authenticate by password every time. Therefore, the authentication of user **within** the MetaCentrum infrastructure is done by the [Kerberos protocol](https://en.wikipedia.org/wiki/Kerberos_(protocol)).

![Grid security protocols scheme](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fgrid-ssh-kerberos_border.2_lbzktaam2qe.jpg&w=3840&q=75)

After the user logs in, they automatically obtain a **Kerberos ticket**. As long as the ticket is valid, the user can move between machines, run jobs, and copy files without bothering about the authentication.

Warning

The ticket is valid for 10 hours. If you stay logged in for longer, you will need to re-generate your ticket with the `kinit` command.

**Basic Kerberos commands**

- `klist` - list all current tickets

- `kdestroy` - delete all tickets

- `kinit` - create a new Kerberos ticket

It is also possible to install Kerberos on your PC. For more in-depth info, see [Kerberos advanced page](./security/kerberos).

![publicity banner](/_next/static/media/einfra_meta-zapati.0m5s8338yq376.svg)

### On this page
[Frontend login](#frontend-login)[Web services login](#web-services-login)[Kerberos](#kerberos)

![einfra banner](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fheader03.0ikyctvi6x5ki.png&w=384&q=75)
