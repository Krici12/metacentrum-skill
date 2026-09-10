#

The job array is submitted as:

```
# general command
$ qsub -J X-Y[:Z] script.sh
# example
$ qsub -J 2-7:2 script.sh

```

`X` is first index of a job, `Y` is upper border of an index and `Z` in optional parameter of an index step, therefore the example command will generate subjobs with indexes 2,4,6.

The job array is represented by a single job whose job number is followed by ”[]”, this main job provides an overview of unfinished sub jobs.

```
$ qstat -f 969390'[]' -x | grep array\_state\_count
array_state_count = Queued:0 Running:0 Exiting:0 Expired:0

```

An example of sub job ID is `969390[1].pbs-m1.metacentrum.cz`.

The sub job can be queried by a qstat command (`qstat -t`).

PBS uses `PBS_ARRAY_INDEX` variable inside of a sub job. The varibale `PBS_ARRAY_ID` contains job ID of the main job.

![publicity banner](/_next/static/media/einfra_meta-zapati.0m5s8338yq376.svg)

### On this page
No Headings

![einfra banner](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fheader03.0ikyctvi6x5ki.png&w=384&q=75)
