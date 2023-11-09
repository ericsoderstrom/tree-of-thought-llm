python run.py \
    --task connections \
    --backend gpt-3.5-turbo \
    --task_start_index 0 \
    --task_end_index 6 \
    --naive_run \
    --prompt_sample standard \
    --n_generate_sample 100 \
    ${@}

