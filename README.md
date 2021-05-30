# Keystone-enclave-rv8-bench-plot
A framework for plotting these fucking benchmarks.

# Workflow
I added the rv8-bench benchmarks provided by Keystone to the examples from the Keystone-SDK. I compiled them with the musl toolchain, then let them run on QEMU. 

* First, process the logs with the script `processing/process_bench_logs.sh`. A condensed list of logs will be generated, containing the field `iruntime`. These generated logs can be found in the `data` directory.

* Then generate the plots using the `plotting/boxplot-bench.py` script.

## Useful commands for retrieving the logs from QEMU and Docker
If you have a setup using QEMU, you need to copy the generated benchmarks to the workspace where you wanna process them. The following commands might be useful for that.

 - QEMU can be accessed through ssh. Thus, secure file copy is available.
```
# this shell is in the docker container that contains keystone and runs QEMU

# copy the files from qemu's /root/logs directory to the docker containers /dest/path
$ scp -P <port_on_which_qemu_runs> -r root@localhost:/root/logs /dest/path
```
 - If you run the whole setup on a docker container, you probably want to download the logs to your local machine. Use docker copy for that.
```
# this shell is on your local computer

# this command copies the files from your docker containers path /dest/path (where <container> is the container name or ID) to your local machines /local/dest/path
$ docker cp <contianer>:/dest/path /local/dest/path
```