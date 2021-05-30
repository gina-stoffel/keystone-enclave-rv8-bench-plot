#!/bin/bash

DATA_DIR="/home/gina/semester-thesis-benchmarks"
WORKING_DIR="/home/gina/semester-thesis-benchmarks/keystone-enclave-rv8-bench-plot"

# path where the benchmark logs are stored
BASELINE_LOD_DIR=${DATA_DIR}"/logs-vanilla"
SPICY_LOG_DIR=${DATA_DIR}"/logs-spicy"

for test in aes dhrystone norx primes qsort sha512; do

    # remove old data
    if [[ -f ${WORKING_DIR}/data/vanilla_base_${test}.csv  ]]; then
        rm ${WORKING_DIR}/data/vanilla_base_${test}.csv
    fi

    if [[ -f ${WORKING_DIR}/data/vanilla_keystone_${test}.csv  ]]; then
        rm ${WORKING_DIR}/data/vanilla_keystone_${test}.csv
    fi

    if [[ -f ${WORKING_DIR}/data/spicy_base_${test}.csv ]]; then
        rm ${WORKING_DIR}/data/spicy_base_${test}.csv
    fi

    if [[ -f ${WORKING_DIR}/data/spicy_keystone_${test}.csv  ]]; then
        rm ${WORKING_DIR}/data/spicy_keystone_${test}.csv
    fi

    ###################################
    #       PLAIN VANILLA SETUP       #
    ###################################

    # Process benchmarks run without keystone
    # cheap regex, but hey, if its fits I sits
    awk '/iruntime\s[0-9]*/ {print $2}' ${BASELINE_LOD_DIR}/base_${test}_*.log >> ${WORKING_DIR}/data/vanilla_base_${test}.csv
    # Process benchmarks on vanilla keystone
    awk '/iruntime\s[0-9]*/ {print $2}' ${BASELINE_LOD_DIR}/keystone_${test}_*.log >> ${WORKING_DIR}/data/vanilla_keystone_${test}.csv

    ###################################
    #      SPICY KEYSTONE SETUP      #
    ###################################
    # Process benchmarks run without keystone
    awk '/iruntime\s[0-9]*/ {print $2}' ${SPICY_LOG_DIR}/base_${test}_*.log >> ${WORKING_DIR}/data/spicy_base_${test}.csv
    # Process benchmarks on spicy keystone
    awk '/iruntime\s[0-9]*/ {print $2}' ${SPICY_LOG_DIR}/keystone_${test}_*.log >> ${WORKING_DIR}/data/spicy_keystone_${test}.csv
    
done;