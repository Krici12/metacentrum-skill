#

## [Technical Parameters](#technical-parameters)

The system consists of a single compute node, **capy.cerit-sc.cz**, with the following specifications:

- **112 CPU cores**

- **2 TB RAM**

- **8× NVIDIA H100 GPU accelerators** (each with **80 GB GPU memory**)

## [Access Conditions](#access-conditions)

Users can apply for computational resources for a **3-month period** through the **DGX Grant Competition**, which is open to research, scientific, and educational organization employees, as well as PhD students. To renew access after its expiration, a new application must be submitted.

**Applicants must demonstrate:**

- The ability to utilize **at least 2, but preferably 4 or all 8 GPUs**

- Effective use of **NVLink** (Multi-GPU) and **large GPU memory**

- Research potential and expected results

### [Approval Process](#approval-process)

The application review consists of **three steps**:

- Submission of a **PDF file** containing the OpenAccess Application request to [meta@cesnet.cz](mailto:meta@cesnet.cz)

- **Internal review** of the request

- **Notification** of competition results within **5 working days**

## [OpenAccess Application](#openaccess-application)

- OpenAccess Application requests must follow the structure specified below.

- The total length must not exceed **5 pages**, including figures and tables.

- Submit a **PDF file** with the proposal to [meta@cesnet.cz](mailto:meta@cesnet.cz).

### [Popular Abstract](#popular-abstract)

Provide a **popular abstract** that can be published on a website, in newspapers, or on similar platforms. This abstract should describe:

- The proposed research

- The methodologies used

- The expected impact

The abstract should be written in a way that is easily understandable by the general public.

### [Methods and State-of-the-Art](#methods-and-state-of-the-art)

- Clearly define the research aims and objectives.

- Provide sufficient detail for reviewers to understand the proposal.

- Specify if the research is part of an approved **H2020, ERC, EuroHPC, GAČR**, or other peer-reviewed **national or international projects**.

- Describe the theoretical and computational methods to be used, comparing them with the current **state-of-the-art**.

- Outline expected results, including planned publications.

### [Computational Approach, Parallelization, and Scalability](#computational-approach-parallelization-and-scalability)

- Describe the **computational techniques** and platforms to be used.

- Include details on **codes, programming languages, libraries, and other software**.

- Explain **parallelization and scalability**, preferably in relation to NVLink (proving that your jobs can effectively utilize **4 or 8 GPUs** simultaneously).

- If possible, provide references and data on your application’s **parallel performance, speedup, and scalability**.

### [Computational Resources](#computational-resources)

- Justify the **requested computational resources**.

- Provide an estimate of the required **CPU, RAM, and GPU hours** in total and also for a typical job.

- Explain how the estimated resources were calculated.

## [Usage](#usage)

Once your request is **approved**, the **DGX H100 cluster** is accessible **only via the `gpu_dgx` queue**:

```
gpu_dgx@pbs-m1.metacentrum.cz

```

in shared access mode.

To submit a job to the **gpu_dgx** queue, use the following command:

```
qsub -q gpu_dgx@pbs-m1.metacentrum.cz -l select=1:ngpus=4 -l walltime=10:00:00

```

### [Example Job Submission](#example-job-submission)

If you require **8 GPUs for 10 hours**, request the entire node by adding the following parameters to your `qsub` command:

```
qsub -q gpu_dgx -l select=1:ngpus=8:ncpus=112:mem=2000g:scratch.ssd=1tb -l place=exclhost -l walltime=10:00:00

```

For additional support, contact [meta@cesnet.cz](mailto:meta@cesnet.cz).

![publicity banner](/_next/static/media/einfra_meta-zapati.0m5s8338yq376.svg)

### On this page
[Technical Parameters](#technical-parameters)[Access Conditions](#access-conditions)[Approval Process](#approval-process)[OpenAccess Application](#openaccess-application)[Popular Abstract](#popular-abstract)[Methods and State-of-the-Art](#methods-and-state-of-the-art)[Computational Approach, Parallelization, and Scalability](#computational-approach-parallelization-and-scalability)[Computational Resources](#computational-resources)[Usage](#usage)[Example Job Submission](#example-job-submission)

![einfra banner](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fheader03.0ikyctvi6x5ki.png&w=384&q=75)
