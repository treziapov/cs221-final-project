#Linux retraining command
python3 retrain.py \
--bottleneck_dir=bottlenecks \
--how_many_training_steps 1000 \
--model_dir=model_dir \
--output_graph=retrained_graph.pb \
--output_labels=retrained_labels.txt \
--summaries_dir=retrain_logs \
--image_dir=images \
--train_batch_size 42 \
--validation_batch_size 10 \
--test_batch_size 20


#Windows retraining command
#python retrain.py --bottleneck_dir=bottlenecks --how_many_training_steps 500 --model_dir=model_dir --output_graph=retrained_graph.pb --output_labels=retrained_labels.txt --summaries_dir=retrain_logs --image_dir=images