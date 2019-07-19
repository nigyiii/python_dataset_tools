#!/bin/bash

python csv_to_tfrecords.py --base_dir=/home/niguangyi/data/jj_person --csv_input=csv/jj_train_labels.csv --output_path=tfrecords/jj_train.tfrecord
python csv_to_tfrecords.py --base_dir=/home/niguangyi/data/jj_person --csv_input=csv/jj_validation_labels.csv --output_path=tfrecords/jj_validation.tfrecord
python csv_to_tfrecords.py --base_dir=/home/niguangyi/data/jj_person --csv_input=csv/jj_test_labels.csv --output_path=tfrecords/jj_test.tfrecord