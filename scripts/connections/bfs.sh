python run.py \
    --task connections \
    --backend gpt-3.5-turbo \
    --task_start_index 5 \
    --task_end_index 6 \
    --method_generate propose \
    --method_evaluate value \
    --method_select greedy \
    --n_evaluate_sample 3 \
    --n_select_sample 5 \
    ${@}
~
