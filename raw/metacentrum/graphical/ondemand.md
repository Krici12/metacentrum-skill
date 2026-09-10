#

[Metacentrum Open OnDemand instance](https://ondemand.metacentrum.cz) is a service that enables users to access Metacentrum via web browser.

![pic](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fondemand_dashboard.1ql_b3lrrfbrr.png&w=3840&q=75)

OnDemand enables users to

- **access files** and directories using a graphical File manager,

- **run graphical applications**,

- setup, modify and **run batch jobs**.

Among the pre-installed applications available are Matlab, ANSYS, Jupyter notebook and RStudio server.

Authorization

**Remember!** OnDemand is a web service, and login is done by the user’s [academic identity](./access/log-in#web-services-login).

Supported browsers are Google Chrome, Mozilla Firefox or Microsoft Edge.

## [Files](#files)

- **browse** Metacentrum **storages**,

- **upload/download files** from/to local PC,

- **move files** between storages,

- **edit files** on storages.

In the rolldown menu, there are pre-defined shortcut links to three homes on different storages.

![pic](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Ffiles-rolldown.1_2ru3ny135qf.png&w=3840&q=75)

By default, the **Home Directory** link points to storage **brno2**.

## [Jobs](#jobs)

### [Active jobs](#active-jobs)

Under this tab, you will find a list of **all running or queued jobs** on the PBS server.

In the contrary to [list of interactive sessions](#my-interactive-sessions), you will see all jobs no matter whether they were submitted via the OnDemand interface or otherwise.

By clicking on the chosen job, you will find the job’s details.

![pic](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Factive-jobs-top.1z0jby_8duspf.png&w=3840&q=75)

At the bottom of the job details table, you can get the location of the output files:

![pic](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Factive-jobs-bottom.2syrk1qfwyt_8.png&w=3840&q=75)

### [Job composer](#job-composer)

Job composer is a GUI wizard to set up a batch job.

## [Clusters](#clusters)

The Clusters tab is OnDemand’s way to **provide CLI access** to MetaCentrum [frontends](../computing/infrastructure/frontends). Currently, there are links to:

- **zuphux.metacentrum.cz**

- **perian.metacentrum.cz**

- **elmo.metacentrum.cz**

![pic](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fclusters-rolldown.0-nbfjjzyobe_.png&w=3840&q=75)

Clicking on “Shell access” will open an SSH connection in your browser:

![pic](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fshell-login.3a6haa3dol9hy.png&w=3840&q=75)

## [Interactive apps](#interactive-apps)

The “Interactive apps” tab lists all **environments**, **shell access** buttons, as well as **graphical software** that can be run from the OnDemand interface.

The “Interactive Apps” tab lists **all graphical software** that can be run as an interactive job.

![pic](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fapps.2_btcl6_5-26p.png&w=3840&q=75)

After it starts, the application runs as an [interactive job](../computing/run-basic-job#interactive-job) on any node within the [MetaCentrum infrastructure](../computing/infrastructure/frontend-storage).

In consequence, the location of the home directory (location=`city_XY` in `/storage/city_XY/home/user_123`) can be different for every new run of an application.

In case you need, e.g. to upload some data to work on, it may be necessary to change the directory to the right storage.

### [Data directory](#data-directory)

To store its own files, OnDemand creates automatically a directory `ondemand` in the current **home directory**. You will find there output files, error files and other data for batch jobs submitted from the OnDemand interface.

For example, after running the VMD Desktop, all output from the session will be in `~/ondemand/data/sys/dashboard/batch_connect/sys/bc_desktop/vmd/output/ONDEMAND_SESSION_ID` directory.

Warning

The **ONDEMAND_SESSION_ID** is OnDemand’s internal hash for the session, not PBS job ID! It looks like e.g. `9a8b3f2b-0c6d-4cbd-922b-c587f2c2f0fb`.

You can remove the content of OnDemand data directories, or even the `~/ondemand` directory itself, at any time you wish.

Every time you run OnDemand, it will first look for the existing directory `~/ondemand`. When it does not find any, it creates a new one.

### [RStudio issues](#rstudio-issues)

As the *home-on-any-storage* feature of OnDemand was causing problems for RStudio users, we applied a workaround for this.

The default location *for the RStudio interactive app* is set to `brno2`.

Moreover, users can overwrite this setting by choosing a different location from the drop-down menu:

![pic](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Frstudio-dir-fix.2pf6_ljm3m71b.png&w=3840&q=75)

## [My Interactive Sessions](#my-interactive-sessions)

Under this tab, you will see a list of your sessions running in OnDemand.

You can launch or delete running sessions. By closing the tab in the browser, you will not lose your session - it can be relaunched, even on another computer, using the blue Launch button if the time reserved for the session is not up yet.

Next to the ‘Launch button is the grey *View only* (shareable link) button, which is useful if you want to share a live view of your desktop application with a colleague.

![pic](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Finteract-sessions.3pdx39o1k8uoq.png&w=3840&q=75)

## [Kerberos ticket expiration](#kerberos-ticket-expiration)

In a long-term open session, Kerber’s ticket may expire. This situation is typically reported by an error message.

`Key has expired @ dir_s_mkdir - /storage/brno2/home/user_name`

An ordinary page reload is insufficient to renew a user’s Kerberos ticket. The user must click the `Help` button in the menu (upper right corner) and continue with `Restart Web Server`.

![publicity banner](/_next/static/media/einfra_meta-zapati.0m5s8338yq376.svg)

### On this page
[Files](#files)[Jobs](#jobs)[Active jobs](#active-jobs)[Job composer](#job-composer)[Clusters](#clusters)[Interactive apps](#interactive-apps)[Data directory](#data-directory)[RStudio issues](#rstudio-issues)[My Interactive Sessions](#my-interactive-sessions)[Kerberos ticket expiration](#kerberos-ticket-expiration)

![einfra banner](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fheader03.0ikyctvi6x5ki.png&w=384&q=75)
