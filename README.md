# CMLM

This is the PyTorch implementation of the paper: Bi-Granularity Contrastive Learning for Post-Training in Few-Shot Scene.

## Usage

### Preprocessing

For back-translation, we need to translate the sentences and save them as files.
```bash
python translation_with_Marian.py
```
requirements for back-translation:
- torch==1.7.0
- transformer==4.2.2

Our translated dataset will be also provided in the future.

### Training

We provide codes for CMLM and related approaches.

For CMLM,
```bash
python run_glue.py 
--model_name_or_path $YOUR_RoBERTa_PATH$ 
--model_type roberta 
--task_name mnli 
--data_dir $YOUR_DATA_PATH$ 
--output_dir $YOUR_OUTPUT_PATH$ 
--do_train 
--do_post 
--evaluate_during_training 
--per_gpu_train_batch_size 16 
--per_gpu_post_batch_size 8 
--per_gpu_eval_batch_size 16 
--num_train_epochs 10 
--fp16 
--learning_rate 2e-05 
--post_learning_rate 1e-05 
--post_train_epochs 5 
--mlm_probability 0.15 
--cl_probability 0.7 
--alpha 0.5 
--logging_steps 100 
--save_steps 100 
--seed 42 
--warmup_prop 0 
--mlm 
--cl
```
You can easily replace "--cl" with "--ocl" to implement CMLM with SimCLR, replace "--mlm --cl" with "--mlm" to implement TAPT, replace "--mlm --cl" with "--ocl --enable_backtranslation" to implement CSSL, replace "--mlm --cl" with "--ocl --enable_eda" to implement using EDA for sentence augment.

For only fine-tuning(FT),
```bash
python run_glue_bl.py 
--model_name_or_path $YOUR_RoBERTa_PATH$ 
--model_type roberta 
--task_name mnli 
--data_dir $YOUR_DATA_PATH$ 
--output_dir $YOUR_OUTPUT_PATH$ 
--do_train 
--do_post 
--evaluate_during_training 
--per_gpu_train_batch_size 16 
--per_gpu_post_batch_size 8 
--per_gpu_eval_batch_size 16 
--num_train_epochs 10 
--fp16 
--learning_rate 2e-05 
--post_learning_rate 1e-05 
--post_train_epochs 5 
--mlm_probability 0.15 
--cl_probability 0.7 
--alpha 0.5 
--logging_steps 100 
--save_steps 100 
--seed 42 
--warmup_prop 0 
```

For SCL,
```bash
python run_glue_scl.py 
--model_name_or_path $YOUR_RoBERTa_PATH$ 
--model_type roberta 
--task_name mnli 
--data_dir $YOUR_DATA_PATH$ 
--output_dir $YOUR_OUTPUT_PATH$ 
--do_train 
--do_post 
--evaluate_during_training 
--per_gpu_train_batch_size 16 
--per_gpu_post_batch_size 8 
--per_gpu_eval_batch_size 16 
--num_train_epochs 10 
--fp16 
--learning_rate 2e-05 
--post_learning_rate 1e-05 
--post_train_epochs 5 
--mlm_probability 0.15 
--cl_probability 0.7 
--alpha 0.5 
--logging_steps 100 
--save_steps 100 
--seed 42 
--warmup_prop 0 
```

### Testing

还没写

### Requirements
- torch==1.0.0
- transformers==2.8.0
