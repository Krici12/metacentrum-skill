#

To run GPU calculation, the user needs to specify **number of GPU cards** only. The PBS scheduler will route the job automatically into one of the **[gpu queues](https://my.metacentrum.cz/queues)**.

User group `iti` has a reserved GPU queue

Members of the ``[iti group](https://metavo.metacentrum.cz/pbsmon2/group/pbs-m1.metacentrum.cz/iti) (Institute of Theoretical Informatics, University of West Bohemia) have their own GPU cluster `konos` with priority access through direct submit to `iti@pbs-m1.metacentrum.cz` queue.

## [PBS resources](#pbs-resources)

### [ngpus](#ngpus)

Parameter `ngpus` specifies how many GPU cards the job will use. Default value: `0`.

```
qsub -l select=1:ncpus=1:ngpus=2 ...

```

### [gpu mem](#gpu-mem)

PBS parameter `gpu_mem` specifies minimum amount of memory that the GPU card will have.

```
qsub -l select=1:ncpus=1:ngpus=1:gpu_mem=10gb -l walltime=1:00:00

```

### [gpu_cap](#gpu_cap)

PBS parameter `gpu_cap` is [Cuda compute capability as defined on this page](https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html#compute-capabilities).

### [Architecture](#architecture)

The user can specify a *minimal required architecture* (`compute_XY`), or a *minimal required version within a given architecture* (`sm_XY`).

Minimal architecture:

```
gpu_cap=compute_70   # will give you 7.0, 7.1, ... 7.5, but also 8.0, 9.0 ...

```

Minimal version of a chosen architecture, e.g. 7 (“Volta”):

```
gpu_cap=sm_72        # will give you 7.2 till 7.5, but not 8.0 and higher

```

The requirements can be combined in a comma-separated string.

Note

The commas are evaluated as an OR operand.

Example:

```
qsub -l select=1:ngpus=1:gpu_cap="sm_65,compute_70":mem=4gb -l walltime=1:00:00  # 6.5 or 7.0 and higher
qsub -l 'select=1:ngpus=1:gpu_cap="sm_65,compute_70":mem=4gb' -l walltime=1:00:00  # dtto

```

Note

Note that the quotes enclosing the `gpu_cap` options must be protected against shell expansion either by escaping them or by enclosing the whole `qsub` command into single quotes.

### [cuda_version](#cuda_version)

PBS parameter `cuda_version` is version of CUDA installed.

## [GPU usage data](#gpu-usage-data)

To be able to monitor GPU usage effectivity, we offer 3 parameters. To find out about them from CLI, use PBS command `qstat -fw`.

```
(BOOKWORM)user_123@skirit:~$ qstat -fw job_ID | grep gpu
    resources_used.gpupercent = 332
    resources_used.gpupowerusage = 38.7777
    resources_used.gpumemmaxpercent = 149

```

### [gpupercent](#gpupercent)

- how much the GPU(s) have been used during the job

- measured in %

For more GPUs, the percentages sum up.

For jobs with more than 1 GPU, the values for respective card are summed up. I.e. the value can be > 100 %, but not > 100 * `ngpus` %.

### [gpupowerusage](#gpupowerusage)

- how much energy was burned on all GPUs for a given job

- measured in Wh

### [gpumemmaxpercent](#gpumemmaxpercent)

- the maximum peak of GPU memory usage

- measured in %

For more GPUs, the percentages sum up.

For jobs with more than 1 GPU, the values for respective card are summed up. I.e. the value can be > 100 %, but not > 100 * `ngpus` %.

## [System variables](#system-variables)

IDs of GPU cards are stored in `CUDA_VISIBLE_DEVICES` variable.

These IDs are mapped to CUDA tools virtual IDs. Though if `CUDA_VISIBLE_DEVICES` contains value 2, 3 then CUDA tools will report IDs 0, 1.

![publicity banner](/_next/static/media/einfra_meta-zapati.0m5s8338yq376.svg)

### On this page
[PBS resources](#pbs-resources)[ngpus](#ngpus)[gpu mem](#gpu-mem)[gpu_cap](#gpu_cap)[Architecture](#architecture)[cuda_version](#cuda_version)[GPU usage data](#gpu-usage-data)[gpupercent](#gpupercent)[gpupowerusage](#gpupowerusage)[gpumemmaxpercent](#gpumemmaxpercent)[System variables](#system-variables)

![einfra banner](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fheader03.0ikyctvi6x5ki.png&w=384&q=75)
