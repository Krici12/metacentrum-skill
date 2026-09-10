#

There are 4 basic resources to be specified with each job: **ncpus** (number of CPUs), **mem** (size of RAM), **walltime** (maximal duration of the job) and **scratch_XY** (scratch directory; type and size of space for temporary job data).

The basic command for runninng a job is

```
qsub  -I -l select=1:ncpus=1 -l walltime=1:00:00 # interactive job
qsub  -l select=1:ncpus=1 -l walltime=1:00:00 batch_job.sh # batch job

```

There is no default scratch

As opposed to **ncpus**, **mem** and **walltime**, there is no default size for **scratch directory**. If not specified, a symbolic scratch directory is always created with the start of the job, however a very small one. If you need to guarantee a certain space for data, we strongly recommend to specify type and size of a scratch dir.

For a quick start, download [PBS cheatsheet (2026)](/img/meta/tutorials/PBS_cheatsheet.pdf).
![PBS pdf](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2FPBS_cheatsheet_view.072vyemhnbt2o.png&w=3840&q=75)

## [CPUs](#cpus)

Resource name: `ncpus`. Default value: `1`.

Example:

```
-l select=1:ncpus=2 # request 2 CPUs

```

## [Memory](#memory)

Resource name: `mem`. Default value: `400 MB`.

Example:

```
-l select=1:ncpus=1:mem=10gb # request 10 GB memory job

```

## [Walltime](#walltime)

Resource name: `walltime`. Default value: `24:00:00` (24 hours).

Maximal duration of a job is set in format `hh:mm:ss`.

Example:

```
-l walltime=1:00:00 # one hour job

```

Users can to a certain extent prolong walltime in running jobs - see ``[qextend command](../../computing/jobs/extend-walltime)

## [Scratch directory](#scratch-directory)

Resource names: `scratch_local`, `scratch_shared`, `scratch_ssd`, `scratch_shm`.

Multijob scratch (in preparation)

By September/October 2026, a new type of scratch, so-called **multijob scratch** (PBS resource `multijob`) will be released. This scratch is taylored for consecutive, independent jobs working upon the same large datasets. The purpose is to reduce the need to repeatedly copy large data to/from a storage by the start/end of each job.

Default value: none.

See [description of scratch types](../../computing/infrastructure/scratch-storages) for more information.

## [Queue and/or PBS server](#queue-andor-pbs-server)

Resource name: `. Default value: `.
If you need to send the job to a specific queue and/or specific PBS server, use the `qsub -q` option.

```
qsub -q queue@server # specific queue on specific server
qsub -q queue # specific queue on the current (default) server
qsub -q @server # default queue on specific server

```

## [GPU-related resources](#gpu-related-resources)

A complete description of GPU-related PBS resources can be found in [chapter on running GPU jobs](../../computing/gpu-comput/gpu-job).

## [CPU type](#cpu-type)

Resource name: `cpu_vendor`.

In the Metacentrum grid there are both machines with AMD as well as Intel processors. Some software may be sensitive to the processor used (although most applications run seamlessly on both). Therefore you can request a specific CPU vendor:

```
qsub -l select=1:ncpus=1:cpu_vendor=amd  # use machine with AMD processor
qsub -l select=1:ncpus=1:cpu_vendor=intel # dtto with Intel

```

## [CPU speed](#cpu-speed)

Resource name: `spec`.

CPUs across Metacentrum grid differ in their how fast they are. Therefore they are classed by parameter `spec` according to methodology of [SPEC CPU2017](https://www.spec.org/cpu2017/). To see the `spec` values, go to [qsub assembler](https://my.metacentrum.cz/qsub-assembler) and see the drop-down menu in the `spec` parameter.

Example:

```
qsub -l select=:spec=4.8 # 1 CPU with speed class 4.8 or higher

```

## [OS](#os)

Resource name: `os`, `osfamily`.

To submit a job to a machine with specific operation system, use `os=OS_name`:

```
zuphux$ qsub -l select=1:ncpus=2:mem=1gb:scratch_local=1gb:os=debian11 …

```

To submit a job to a machine with a specific OS type, use `osfamily=OS_type_name`

```
zuphux$ qsub -l select=1:ncpus=2:mem=1gb:scratch_local=1gb:osfamily=debian …

```

## [Cluster](#cluster)

Resource name: `cluster`, `cl_NAME`. Default value: none.

PBS allows you to choose a particular cluster (using either resource `cluster` or `cl_NAME`:

```
qsub -l select=1:ncpus=2:cluster=halmir # run the job on cluster "halmir"
qsub -l select=1:ncpus=2:cl_halmir=True # same as above

```

Alternatively, you can avoid a particular cluster:

```
qsub -l select=1:ncpus=2:cluster=^halmir
qsub -l select=1:ncpus=2:cl_halmir=False

```

However it is not possible to combine conditions. If you e.g. want to avoid both `adan` and `halmir`, the following

```
qsub -l select=1:ncpus=2:cluster=^adan:cluster=^halmir # DOES NOT WORK

```

will not work. This is based on the principle that in PBS, every resource (in this case `cluster` resource) can be specified only once.

On the other hand, `cl_adan` and `cl_halmir` are different resources, so:

```
qsub -l select=1:ncpus=2:cl_adan=False:cl_halmir=False

```

will work and will avoid both `adan` and `halmir` clusters.

The same can be done with

```
qsub -l select=1:ncpus=2:cluster=^adan:cl_halmir=False

```

## [Location](#location)

Resource names: `brno`, `budejovice`, `liberec`, `olomouc`, `plzen`, `praha`, `pruhonice`, `vestec`.

Default value: none.

As the physical machines are distributed over multiple locations in Czech republic, it may be useful to be able to specify the location of the machine(s)

```
qsub -l select=1:ncpus=1:brno=True # run on machines located in Brno.

```

## [MPI processes](#mpi-processes)

Resource name: `mpiprocs`, `ompthreads`.

How many MPI processes would run on one chunk is specified by `mpiprocs=[number]`:

```
-l select=3:ncpus=2:mpiprocs=2 # 6 MPI processes (nodefile contains 6 lines with names of vnodes), 2 MPI processes always share 1 vnode with 2 CPU

```

How many OpenMP threads would run in 1 chunk `ompthreads=[number]`, 2 omp threads on 1 chunks is default behaviour (`ompthreads = ncpus`).

## [Licence](#licence)

Some software requires licence to run. Licence is set by parameter `-l`

```
-l select=3:ncpus=1 -l walltime=1:00:00 -l matlab=1 # one licence for Matlab

```

## [Paths for output](#paths-for-output)

By default the job output (output, and error files) is saved in a folder from which the job was submitted (variable `PBS_O_WORKDIR`).

This behaviour for output, resp. error files can be changed by parameters -o, resp -e.

```
-o /custom-path/myOutputFile
-e /custom-path/myErrorFile

```

![publicity banner](/_next/static/media/einfra_meta-zapati.0m5s8338yq376.svg)

### On this page
[CPUs](#cpus)[Memory](#memory)[Walltime](#walltime)[Scratch directory](#scratch-directory)[Queue and/or PBS server](#queue-andor-pbs-server)[GPU-related resources](#gpu-related-resources)[CPU type](#cpu-type)[CPU speed](#cpu-speed)[OS](#os)[Cluster](#cluster)[Location](#location)[MPI processes](#mpi-processes)[Licence](#licence)[Paths for output](#paths-for-output)

![einfra banner](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fheader03.0ikyctvi6x5ki.png&w=384&q=75)
